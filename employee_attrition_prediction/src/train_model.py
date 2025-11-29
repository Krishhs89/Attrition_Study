import csv
import math
import random

# --- Helper Functions ---

def load_csv(filename):
    data = []
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        headers = next(reader)
        for row in reader:
            data.append(row)
    return headers, data

def one_hot_encode(headers, data):
    """
    Simple One-Hot Encoding for categorical variables.
    Returns: new_headers, new_data (all numeric)
    """
    # Identify column types
    n_cols = len(headers)
    col_types = [] # 'num' or 'cat'
    
    # Check first few rows to guess type
    for i in range(n_cols):
        is_numeric = True
        for row in data[:10]: # Check first 10
            try:
                float(row[i])
            except ValueError:
                is_numeric = False
                break
        col_types.append('num' if is_numeric else 'cat')
        
    # Build maps for categorical columns
    cat_maps = {} # {col_idx: {value: new_col_idx}}
    new_headers = []
    
    for i in range(n_cols):
        if col_types[i] == 'num':
            new_headers.append(headers[i])
        else:
            # Find unique values
            unique_vals = set([row[i] for row in data])
            # Create a column for each unique value (simple OHE)
            # To keep it manageable, maybe limit? But let's try full.
            for val in unique_vals:
                new_headers.append("{}_{}".format(headers[i], val))
                
    print "Expanded features from {} to {}...".format(n_cols, len(new_headers))
    
    new_data = []
    for row in data:
        new_row = []
        for i in range(n_cols):
            if col_types[i] == 'num':
                new_row.append(float(row[i]))
            else:
                # OHE
                unique_vals = set([r[i] for r in data]) # Re-calculating is inefficient but safe for this scale
                # Wait, we need consistent mapping.
                # Let's do it properly.
                pass
        # This loop is getting messy. Let's restart the logic below.
        pass

    # --- Better OHE Logic ---
    # 1. Collect all unique values for cat columns
    cat_values = {} # {col_idx: [val1, val2...]}
    for i in range(n_cols):
        if col_types[i] == 'cat':
            unique = sorted(list(set([row[i] for row in data])))
            cat_values[i] = unique
            
    # 2. Create new headers
    final_headers = []
    for i in range(n_cols):
        if col_types[i] == 'num':
            final_headers.append(headers[i])
        else:
            for val in cat_values[i]:
                final_headers.append("{}_{}".format(headers[i], val))
                
    # 3. Transform data
    final_data = []
    for row in data:
        new_row = []
        for i in range(n_cols):
            if col_types[i] == 'num':
                new_row.append(float(row[i]))
            else:
                # Add 1 for match, 0 for others
                for val in cat_values[i]:
                    new_row.append(1.0 if row[i] == val else 0.0)
        final_data.append(new_row)
        
    return final_headers, final_data

def train_test_split(data, test_size=0.2):
    random.shuffle(data)
    split_idx = int(len(data) * (1 - test_size))
    return data[:split_idx], data[split_idx:]

def sigmoid(z):
    try:
        return 1.0 / (1.0 + math.exp(-z))
    except OverflowError:
        return 0.0 if z < 0 else 1.0

def predict_proba(row, coefficients, intercept):
    z = intercept
    for i in range(len(row)):
        z += coefficients[i] * row[i]
    return sigmoid(z)

def train_logistic_regression(train_data, learning_rate=0.01, epochs=50):
    n_features = len(train_data[0]) - 1
    coefficients = [0.0] * n_features
    intercept = 0.0
    
    for epoch in range(epochs):
        sum_error = 0
        for row in train_data:
            features = row[:-1]
            target = row[-1]
            
            y_pred = predict_proba(features, coefficients, intercept)
            error = target - y_pred
            sum_error += error**2
            
            intercept += learning_rate * error * y_pred * (1.0 - y_pred)
            for i in range(n_features):
                coefficients[i] += learning_rate * error * y_pred * (1.0 - y_pred) * features[i]
        
        # print "Epoch %d, Error: %.3f" % (epoch, sum_error)
    
    return coefficients, intercept

def evaluate(model, test_data):
    coefficients, intercept = model
    tp, tn, fp, fn = 0, 0, 0, 0
    
    y_true = []
    y_pred = []
    
    for row in test_data:
        features = row[:-1]
        target = row[-1]
        prob = predict_proba(features, coefficients, intercept)
        prediction = 1 if prob >= 0.5 else 0
        
        y_true.append(target)
        y_pred.append(prediction)
        
        if target == 1 and prediction == 1: tp += 1
        elif target == 0 and prediction == 0: tn += 1
        elif target == 0 and prediction == 1: fp += 1
        elif target == 1 and prediction == 0: fn += 1
        
    accuracy = float(tp + tn) / len(test_data)
    precision = float(tp) / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = float(tp) / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
    
    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'cm': [[tn, fp], [fn, tp]]
    }

def save_svg_bar_chart(features, coefficients, filename):
    # Sort by absolute value
    combined = sorted(zip(features, coefficients), key=lambda x: abs(x[1]), reverse=True)[:15]
    features = [x[0] for x in combined]
    coefficients = [x[1] for x in combined]
    
    width = 800
    height = 600
    margin_left = 350 # Increased margin for long variable names
    margin_bottom = 50
    bar_height = 20
    gap = 10
    
    max_val = max([abs(c) for c in coefficients]) if coefficients else 1.0
    scale = (width - margin_left - 50) / max_val
    
    svg = ['<svg width="{}" height="{}" xmlns="http://www.w3.org/2000/svg">'.format(width, height)]
    svg.append('<rect width="100%" height="100%" fill="white"/>')
    svg.append('<text x="{}" y="30" font-family="Arial" font-size="20" text-anchor="middle">Top Feature Determinants</text>'.format(width/2))
    
    y = 60
    for i, (feat, coef) in enumerate(zip(features, coefficients)):
        bar_width = abs(coef) * scale
        color = "blue" if coef > 0 else "red"
        
        # Truncate long names
        display_feat = (feat[:45] + '..') if len(feat) > 45 else feat
        
        svg.append('<text x="{}" y="{}" font-family="Arial" font-size="12" text-anchor="end">{}</text>'.format(margin_left - 10, y + 15, display_feat))
        svg.append('<rect x="{}" y="{}" width="{}" height="{}" fill="{}"/>'.format(margin_left, y, bar_width, bar_height, color))
        svg.append('<text x="{}" y="{}" font-family="Arial" font-size="10">  {:.3f}</text>'.format(margin_left + bar_width + 5, y + 15, coef))
        
        y += bar_height + gap
        
    svg.append('</svg>')
    
    with open(filename, 'w') as f:
        f.write('\n'.join(svg))
    print "Saved {}".format(filename)

def save_svg_confusion_matrix(cm, filename):
    tn, fp = cm[0]
    fn, tp = cm[1]
    
    width = 500
    height = 500
    
    svg = ['<svg width="{}" height="{}" xmlns="http://www.w3.org/2000/svg">'.format(width, height)]
    svg.append('<rect width="100%" height="100%" fill="white"/>')
    svg.append('<text x="{}" y="40" font-family="Arial" font-size="20" text-anchor="middle">Confusion Matrix</text>'.format(width/2))
    
    # Grid
    start_x, start_y = 100, 100
    cell_size = 150
    
    # Labels
    svg.append('<text x="{}" y="{}" font-family="Arial" font-size="14" text-anchor="middle">Predicted: No</text>'.format(start_x + cell_size/2, start_y - 10))
    svg.append('<text x="{}" y="{}" font-family="Arial" font-size="14" text-anchor="middle">Predicted: Yes</text>'.format(start_x + cell_size*1.5, start_y - 10))
    
    svg.append('<text x="{}" y="{}" font-family="Arial" font-size="14" text-anchor="middle" transform="rotate(-90, {}, {})">Actual: No</text>'.format(start_x - 20, start_y + cell_size/2, start_x - 20, start_y + cell_size/2))
    svg.append('<text x="{}" y="{}" font-family="Arial" font-size="14" text-anchor="middle" transform="rotate(-90, {}, {})">Actual: Yes</text>'.format(start_x - 20, start_y + cell_size*1.5, start_x - 20, start_y + cell_size*1.5))
    
    # Cells
    # TN
    svg.append('<rect x="{}" y="{}" width="{}" height="{}" fill="#cce5ff" stroke="black"/>'.format(start_x, start_y, cell_size, cell_size))
    svg.append('<text x="{}" y="{}" font-family="Arial" font-size="20" text-anchor="middle">{}</text>'.format(start_x + cell_size/2, start_y + cell_size/2, tn))
    
    # FP
    svg.append('<rect x="{}" y="{}" width="{}" height="{}" fill="#e6f2ff" stroke="black"/>'.format(start_x + cell_size, start_y, cell_size, cell_size))
    svg.append('<text x="{}" y="{}" font-family="Arial" font-size="20" text-anchor="middle">{}</text>'.format(start_x + cell_size*1.5, start_y + cell_size/2, fp))
    
    # FN
    svg.append('<rect x="{}" y="{}" width="{}" height="{}" fill="#e6f2ff" stroke="black"/>'.format(start_x, start_y + cell_size, cell_size, cell_size))
    svg.append('<text x="{}" y="{}" font-family="Arial" font-size="20" text-anchor="middle">{}</text>'.format(start_x + cell_size/2, start_y + cell_size*1.5, fn))
    
    # TP
    svg.append('<rect x="{}" y="{}" width="{}" height="{}" fill="#004080" stroke="black"/>'.format(start_x + cell_size, start_y + cell_size, cell_size, cell_size))
    svg.append('<text x="{}" y="{}" font-family="Arial" font-size="20" fill="white" text-anchor="middle">{}</text>'.format(start_x + cell_size*1.5, start_y + cell_size*1.5, tp))
    
    svg.append('</svg>')
    
    with open(filename, 'w') as f:
        f.write('\n'.join(svg))
    print "Saved {}".format(filename)

# --- Main ---

if __name__ == "__main__":
    print "Loading data..."
    headers, raw_data = load_csv("synthetic_attrition_data.csv")
    
    print "Preprocessing (One-Hot Encoding)..."
    # Separate target (Attrition) before encoding to keep it simple
    target_idx = len(headers) - 1
    features_headers = headers[:-1]
    
    # Split features and target
    X_raw = [row[:-1] for row in raw_data]
    y = [float(row[-1]) for row in raw_data]
    
    # Encode features
    encoded_headers, X_encoded = one_hot_encode(features_headers, X_raw)
    
    # Recombine for splitting
    data = []
    for i in range(len(X_encoded)):
        row = X_encoded[i] + [y[i]]
        data.append(row)
        
    print "Splitting data..."
    train_data, test_data = train_test_split(data)
    
    print "Training Logistic Regression (SGD)..."
    coefficients, intercept = train_logistic_regression(train_data)
    
    print "Evaluating..."
    metrics = evaluate((coefficients, intercept), test_data)
    
    print "\nModel Performance:"
    print "Accuracy:  {:.4f}".format(metrics['accuracy'])
    print "Precision: {:.4f}".format(metrics['precision'])
    print "Recall:    {:.4f}".format(metrics['recall'])
    print "F1 Score:  {:.4f}".format(metrics['f1'])
    
    print "\nGenerating presentation assets (SVG)..."
    save_svg_confusion_matrix(metrics['cm'], 'confusion_matrix.svg')
    save_svg_bar_chart(encoded_headers, coefficients, 'feature_importance.svg')
    
    # Save Model Artifacts for Deployment
    import json
    print "\nSaving model artifacts for deployment..."
    artifacts = {
        'coefficients': coefficients,
        'intercept': intercept,
        'features': encoded_headers
    }
    with open('model_artifacts.json', 'w') as f:
        json.dump(artifacts, f)
    print "Saved model_artifacts.json"

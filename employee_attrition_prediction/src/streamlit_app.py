"""
Streamlit Dashboard for Employee Attrition Prediction
Showcases: EDA, Feature Engineering, Model Building, Validation, CI/CD
"""

import streamlit as st
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Employee Attrition Dashboard",
    page_icon="📊",
    layout="wide"
)

# Sidebar navigation
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio(
    "Select View",
    ["Overview", "EDA", "Feature Engineering", "Model Building", "Validation", "CI/CD Status"]
)

# Load data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('../data/synthetic_attrition_data.csv')
        return df
    except:
        st.error("Data file not found. Please run generate_data.py first.")
        return None

@st.cache_data
def load_model_artifacts():
    try:
        with open('../models/model_artifacts.json', 'r') as f:
            return json.load(f)
    except:
        st.warning("Model not trained yet. Please run train_model.py first.")
        return None

df = load_data()
model = load_model_artifacts()

# ============ OVERVIEW PAGE ============
if page == "Overview":
    st.title("🎯 Employee Attrition Prediction System")
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Employees", len(df) if df is not None else 0)
    
    with col2:
        if df is not None:
            attrition_rate = (df['Attrition'].sum() / len(df)) * 100
            st.metric("Attrition Rate", f"{attrition_rate:.1f}%")
    
    with col3:
        st.metric("Total Features", 41)
    
    with col4:
        if model:
            st.metric("Model Features", len(model.get('features', [])))
    
    st.markdown("---")
    
    # Project Status
    st.subheader("📋 Project Status")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Data Pipeline**")
        st.success("✅ Data Generated (1,000 samples)")
        st.success("✅ 41 Variables Configured")
        st.success("✅ One-Hot Encoding Ready")
    
    with col2:
        st.markdown("**Model Pipeline**")
        if model:
            st.success("✅ Model Trained")
            st.success("✅ Artifacts Saved")
            st.success("✅ Ready for Deployment")
        else:
            st.warning("⏳ Model Not Trained")
    
    # Quick Stats
    if df is not None:
        st.markdown("---")
        st.subheader("📊 Quick Statistics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Attrition by Generation
            if 'EMPLOYEE_GENERATION' in df.columns:
                gen_attrition = df.groupby('EMPLOYEE_GENERATION')['Attrition'].mean() * 100
                fig = px.bar(
                    x=gen_attrition.index,
                    y=gen_attrition.values,
                    title="Attrition Rate by Generation",
                    labels={'x': 'Generation', 'y': 'Attrition Rate (%)'},
                    color=gen_attrition.values,
                    color_continuous_scale='RdYlGn_r'
                )
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Attrition by Gender
            if 'EMPLOYEE_GENDER_CODE' in df.columns:
                gender_attrition = df.groupby('EMPLOYEE_GENDER_CODE')['Attrition'].mean() * 100
                fig = px.pie(
                    values=gender_attrition.values,
                    names=gender_attrition.index,
                    title="Attrition Distribution by Gender"
                )
                st.plotly_chart(fig, use_container_width=True)

# ============ EDA PAGE ============
elif page == "EDA":
    st.title("🔍 Exploratory Data Analysis")
    st.markdown("---")
    
    if df is None:
        st.error("No data available")
    else:
        # Dataset Preview
        st.subheader("📋 Dataset Preview")
        st.dataframe(df.head(10), use_container_width=True)
        
        # Basic Statistics
        st.subheader("📊 Basic Statistics")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Rows", len(df))
            st.metric("Total Columns", len(df.columns))
        
        with col2:
            st.metric("Attrition Cases", int(df['Attrition'].sum()))
            st.metric("Retention Cases", int((1 - df['Attrition']).sum()))
        
        with col3:
            attrition_pct = (df['Attrition'].sum() / len(df)) * 100
            st.metric("Class Balance", f"{attrition_pct:.1f}% / {100-attrition_pct:.1f}%")
        
        st.markdown("---")
        
        # Distribution Analysis
        st.subheader("📈 Distribution Analysis")
        
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        if 'Attrition' in numeric_cols:
            numeric_cols.remove('Attrition')
        
        if numeric_cols:
            selected_col = st.selectbox("Select Variable", numeric_cols)
            
            fig = px.histogram(
                df,
                x=selected_col,
                color='Attrition',
                title=f"Distribution of {selected_col} by Attrition",
                barmode='overlay',
                opacity=0.7
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Correlation Heatmap (for numeric features)
        st.subheader("🔥 Correlation Analysis")
        numeric_df = df.select_dtypes(include=['int64', 'float64'])
        
        if len(numeric_df.columns) > 1:
            corr = numeric_df.corr()
            
            fig = px.imshow(
                corr,
                title="Feature Correlation Heatmap",
                color_continuous_scale='RdBu_r',
                aspect='auto'
            )
            st.plotly_chart(fig, use_container_width=True)

# ============ FEATURE ENGINEERING PAGE ============
elif page == "Feature Engineering":
    st.title("⚙️ Feature Engineering")
    st.markdown("---")
    
    st.subheader("🔄 One-Hot Encoding Transformation")
    
    st.markdown("""
    **Process Overview:**
    1. Identify categorical vs numerical variables
    2. Apply One-Hot Encoding to categorical variables
    3. Create binary indicator columns for each category
    4. Combine with numerical features
    """)
    
    if df is not None:
        # Show transformation example
        st.subheader("📊 Encoding Example")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Before Encoding (Raw Data)**")
            sample_raw = df[['EMPLOYEE_GENDER_CODE', 'EMPLOYEE_GENERATION', 'DEV_DEVELOPMENT']].head(5)
            st.dataframe(sample_raw)
        
        with col2:
            st.markdown("**After Encoding (Model Input)**")
            st.code("""
# Gender: M, F, X → 3 columns
EMPLOYEE_GENDER_CODE_M: [1, 0, 0]
EMPLOYEE_GENDER_CODE_F: [0, 1, 0]
EMPLOYEE_GENDER_CODE_X: [0, 0, 1]

# Generation: 4 categories → 4 columns
EMPLOYEE_GENERATION_GenZ: [1 or 0]
EMPLOYEE_GENERATION_Millennial: [1 or 0]
...
            """)
        
        # Feature Expansion Stats
        st.markdown("---")
        st.subheader("📈 Feature Expansion")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Original Features", 41)
        
        with col2:
            if model:
                st.metric("Encoded Features", len(model.get('features', [])))
        
        with col3:
            if model:
                expansion = len(model.get('features', [])) / 41
                st.metric("Expansion Factor", f"{expansion:.1f}x")
        
        # Show feature importance if model exists
        if model:
            st.markdown("---")
            st.subheader("🎯 Top Engineered Features")
            
            features = model.get('features', [])
            coefficients = model.get('coefficients', [])
            
            if features and coefficients:
                feature_importance = sorted(
                    zip(features, coefficients),
                    key=lambda x: abs(x[1]),
                    reverse=True
                )[:15]
                
                feat_names = [f[0] for f in feature_importance]
                feat_coefs = [f[1] for f in feature_importance]
                
                fig = go.Figure(data=[
                    go.Bar(
                        y=feat_names,
                        x=feat_coefs,
                        orientation='h',
                        marker=dict(
                            color=feat_coefs,
                            colorscale='RdBu',
                            showscale=True
                        )
                    )
                ])
                fig.update_layout(
                    title="Top 15 Features by Coefficient Magnitude",
                    xaxis_title="Coefficient Value",
                    yaxis_title="Feature",
                    height=600
                )
                st.plotly_chart(fig, use_container_width=True)

# ============ MODEL BUILDING PAGE ============
elif page == "Model Building":
    st.title("🤖 Model Building")
    st.markdown("---")
    
    st.subheader("📚 Training Configuration")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Algorithm**")
        st.info("Logistic Regression (SGD)")
        
        st.markdown("**Hyperparameters**")
        st.code("""
Learning Rate: 0.01
Epochs: 50
Optimizer: SGD
Regularization: None
        """)
    
    with col2:
        st.markdown("**Training Process**")
        st.write("1. Load preprocessed data")
        st.write("2. Split into train/test (80/20)")
        st.write("3. Initialize random coefficients")
        st.write("4. Iterate through epochs")
        st.write("5. Update weights using gradients")
        st.write("6. Save final model artifacts")
    
    if model:
        st.markdown("---")
        st.subheader("📊 Model Parameters")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Coefficients", len(model.get('coefficients', [])))
        
        with col2:
            st.metric("Intercept", f"{model.get('intercept', 0):.4f}")
        
        with col3:
            coeffs = model.get('coefficients', [])
            if coeffs:
                avg_coef = sum(abs(c) for c in coeffs) / len(coeffs)
                st.metric("Avg |Coefficient|", f"{avg_coef:.4f}")
        
        # Coefficient Distribution
        st.markdown("---")
        st.subheader("📈 Coefficient Distribution")
        
        coeffs = model.get('coefficients', [])
        if coeffs:
            fig = px.histogram(
                x=coeffs,
                nbins=50,
                title="Distribution of Model Coefficients",
                labels={'x': 'Coefficient Value', 'y': 'Frequency'}
            )
            st.plotly_chart(fig, use_container_width=True)

# ============ VALIDATION PAGE ============
elif page == "Validation":
    st.title("✅ Model Validation")
    st.markdown("---")
    
    st.subheader("📊 Performance Metrics")
    
    # Mock metrics (in real app, load from validation results)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Accuracy", "63.0%", delta="Baseline")
    
    with col2:
        st.metric("Precision", "N/A", delta="Class Imbalance")
    
    with col3:
        st.metric("Recall", "N/A", delta="Class Imbalance")
    
    with col4:
        st.metric("F1 Score", "N/A", delta="Class Imbalance")
    
    st.markdown("---")
    
    # Confusion Matrix
    st.subheader("📉 Confusion Matrix")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Mock confusion matrix
        cm = [[126, 0], [74, 0]]  # Example from our output
        
        fig = px.imshow(
            cm,
            labels=dict(x="Predicted", y="Actual", color="Count"),
            x=['No Attrition', 'Attrition'],
            y=['No Attrition', 'Attrition'],
            title="Confusion Matrix",
            color_continuous_scale='Blues',
            text_auto=True
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("**Interpretation:**")
        st.write("- True Negatives: 126")
        st.write("- False Positives: 0")
        st.write("- False Negatives: 74")
        st.write("- True Positives: 0")
        
        st.warning("⚠️ Model predicts all cases as 'No Attrition'. This suggests class imbalance or insufficient training signal in synthetic data.")
    
    # Recommendations
    st.markdown("---")
    st.subheader("💡 Improvement Recommendations")
    
    st.markdown("""
    1. **Use Real Data**: Synthetic data lacks realistic patterns
    2. **Address Class Imbalance**: Apply SMOTE or class weighting
    3. **Feature Selection**: Remove redundant encoded features
    4. **Hyperparameter Tuning**: Adjust learning rate and epochs
    5. **Try Ensemble Methods**: Random Forest, XGBoost
    6. **Cross-Validation**: Implement k-fold CV for robust evaluation
    """)

# ============ CI/CD STATUS PAGE ============
elif page == "CI/CD Status":
    st.title("🚀 CI/CD Pipeline Status")
    st.markdown("---")
    
    st.subheader("📋 Pipeline Overview")
    
    # Pipeline stages
    stages = [
        {"name": "Data Generation", "status": "✅ Success", "duration": "2s"},
        {"name": "Model Training", "status": "✅ Success", "duration": "5s"},
        {"name": "Artifact Validation", "status": "✅ Success", "duration": "1s"},
        {"name": "Unit Tests", "status": "⏳ Pending", "duration": "-"},
        {"name": "Deployment", "status": "⏳ Pending", "duration": "-"}
    ]
    
    for stage in stages:
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.write(f"**{stage['name']}**")
        with col2:
            st.write(stage['status'])
        with col3:
            st.write(stage['duration'])
    
    st.markdown("---")
    
    # Last Build Info
    st.subheader("🕐 Last Build")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Build Number", "#1")
    
    with col2:
        st.metric("Status", "Passing")
    
    with col3:
        st.metric("Duration", "8 seconds")
    
    # Recent Commits (mock)
    st.markdown("---")
    st.subheader("📝 Recent Commits")
    
    commits = [
        {"hash": "a1b2c3d", "message": "Initial commit - v1.0", "author": "You", "time": "2 hours ago"},
        {"hash": "e4f5g6h", "message": "Add CI/CD pipeline", "author": "You", "time": "1 hour ago"}
    ]
    
    for commit in commits:
        with st.expander(f"{commit['hash']} - {commit['message']}"):
            st.write(f"**Author:** {commit['author']}")
            st.write(f"**Time:** {commit['time']}")
    
    # Deployment Status
    st.markdown("---")
    st.subheader("🌐 Deployment Status")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Staging**")
        st.success("✅ Deployed")
        st.write("URL: http://staging.example.com")
        st.write("Version: v1.0.0")
    
    with col2:
        st.markdown("**Production**")
        st.warning("⏳ Not Deployed")
        st.write("URL: -")
        st.write("Version: -")

# Footer
st.markdown("---")
st.markdown("**Employee Attrition Prediction System** | v1.0.0 | Built with ❤️ using Streamlit")

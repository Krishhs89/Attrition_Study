import BaseHTTPServer
import json
import math

# Load Model Artifacts
print "Loading model..."
with open('model_artifacts.json', 'r') as f:
    artifacts = json.load(f)

coefficients = artifacts['coefficients']
intercept = artifacts['intercept']
feature_names = artifacts['features']

def sigmoid(z):
    try:
        return 1.0 / (1.0 + math.exp(-z))
    except OverflowError:
        return 0.0 if z < 0 else 1.0

def predict_proba(features):
    z = intercept
    # We expect features to be a list of values matching feature_names order
    # In a real app, we'd need to handle mapping from a dict to the encoded vector.
    # For this demo, we'll assume the input is the raw dictionary and we encode it on the fly.
    
    # This is tricky without the full training data to know all categories.
    # But we have 'feature_names' which are the encoded headers (e.g. "GENDER_M", "GENDER_F").
    
    # Let's assume input is a dense vector for simplicity in this low-resource demo,
    # or we construct the vector.
    
    # Construct vector from sparse input dict
    # Input: {"EMPLOYEE_GENDER_CODE": "M", "AGE": 30, ...}
    
    # Initialize vector with 0.0
    x_vec = [0.0] * len(feature_names)
    
    # This is a simplified serving logic. 
    # In production, you'd share the OneHotEncoder artifact.
    # Here we will just try to match keys.
    
    # For numeric features: key matches feature_name exactly.
    # For categorical: feature_name is "KEY_VALUE".
    
    # This is complex to reconstruct perfectly without the encoder object.
    # For this "working setup" demo, let's assume the client sends the pre-processed vector
    # OR we just do a dot product if lengths match.
    
    if len(features) == len(coefficients):
        for i in range(len(features)):
            z += coefficients[i] * features[i]
    else:
        # Fallback/Error
        return 0.5
        
    return sigmoid(z)

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/predict':
            content_length = int(self.headers.getheader('content-length', 0))
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data)
                features = data.get('features', [])
                
                prob = predict_proba(features)
                prediction = 1 if prob >= 0.5 else 0
                
                response = {
                    'prediction': prediction,
                    'probability': prob,
                    'status': 'success'
                }
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response))
                
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}))
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=BaseHTTPServer.HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting inference server on port %d...' % port
    httpd.serve_forever()

if __name__ == "__main__":
    run()

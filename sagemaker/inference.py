import os
import joblib
import pandas as pd
import json

def model_fn(model_dir):
    """Load the model from the model_dir path."""
    model_path = os.path.join(model_dir, "model.pkl")
    model = joblib.load(model_path)
    return model

def input_fn(request_body, request_content_type):
    """Convert input JSON string to pandas DataFrame."""
    if request_content_type == "application/json":
        
        input_data = json.loads(request_body)

        
        if isinstance(input_data, dict):
            input_data = [input_data]

        return pd.DataFrame(input_data)

def predict_fn(input_data, model):
    
    input_data = input_data[["temp", "humidity", "wind"]]
    prediction = model.predict(input_data)
    return prediction.tolist()
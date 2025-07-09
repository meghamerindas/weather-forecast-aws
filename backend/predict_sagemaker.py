

import boto3
import json

SAGEMAKER_ENDPOINT = "weather-forecast-endpoint"
runtime = boto3.client("sagemaker-runtime", region_name="ap-south-1")

def get_prediction(weather_features):
    
    payload = json.dumps({
        "temp": weather_features[0],
        "humidity": weather_features[1],
        "wind": weather_features[2]
    })

    response = runtime.invoke_endpoint(
        EndpointName=SAGEMAKER_ENDPOINT,
        ContentType="application/json",
        Body=payload
    )

    result = json.loads(response["Body"].read().decode())
    return result  

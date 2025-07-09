
import boto3
import json

client = boto3.client("sagemaker-runtime")

payload = {
    "city": "Delhi",
    "date": "2025-07-01",
    "temp": 30.5,
    "humidity": 78,
    "wind": 12.0,
    "target": 31.0
}

response = client.invoke_endpoint(
    EndpointName="weather-forecast-endpoint",
    ContentType="application/json",
    Body=json.dumps(payload)
)

print(response["Body"].read().decode("utf-8"))

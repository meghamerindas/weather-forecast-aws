import json
import urllib.request
import boto3
import os


SAGEMAKER_ENDPOINT = "weather-forecast-endpoint"
SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1:109249930734:weather-prediction-topic"

region = "ap-south-1"

runtime = boto3.client("sagemaker-runtime", region_name=region)
sns = boto3.client("sns", region_name=region)


CITY_COORDS = {
    "Kochi": {"lat": 9.9312, "lon": 76.2673},
    "Delhi": {"lat": 28.6139, "lon": 77.2090},
    "Mumbai": {"lat": 19.0760, "lon": 72.8777},
    "Bengaluru": {"lat": 12.9716, "lon": 77.5946},
    "Chennai": {"lat": 13.0827, "lon": 80.2707},
    "Hyderabad": {"lat": 17.3850, "lon": 78.4867},
    "Ahmedabad": {"lat": 23.0225, "lon": 72.5714},
    "Pune": {"lat": 18.5204, "lon": 73.8567},
    "Jaipur": {"lat": 26.9124, "lon": 75.7873},
    "Kolkata": {"lat": 22.5726, "lon": 88.3639},
}

def fetch_today_weather(city):
    coords = CITY_COORDS.get(city)
    if not coords:
        raise ValueError(f"City '{city}' not supported.")
    
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={coords['lat']}&longitude={coords['lon']}"
        f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
    )

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
        current = data["current"]
        return [
            current["temperature_2m"],
            current["relative_humidity_2m"],
            current["wind_speed_10m"]
        ]

def predict_weather(features):
    payload = json.dumps({
        "temp": features[0],
        "humidity": features[1],
        "wind": features[2]
    })

    response = runtime.invoke_endpoint(
        EndpointName=SAGEMAKER_ENDPOINT,
        ContentType="application/json",
        Body=payload
    )

    result = json.loads(response['Body'].read().decode())
    return result  

def send_email(to_email, city, prediction):
    temp = prediction[0]
    message = (
        f"🌤️ Weather Forecast for {city} (Tomorrow):\n"
        f"🌡️ Temperature: {temp:.2f}°C\n"
    )

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=message,
        Subject=f"Tomorrow's Weather Forecast: {city}",
        MessageAttributes={
            'email': {
                'DataType': 'String',
                'StringValue': to_email
            }
        }
    )

def lambda_handler(event, context):
    try:
        body = event.get("body")
        if isinstance(body, str):
            body = json.loads(body)
        city = body.get("city")
        email = body.get("email")

        if not city or not email:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing 'city' or 'email' in request."})
            }

        weather = fetch_today_weather(city)
        prediction = predict_weather(weather)
        send_email(email, city, prediction)

        return {
    "statusCode": 200,
    "headers": {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type"
    },
    "body": json.dumps({
        "city": city,
        "prediction": prediction,
        "message": f"Forecast sent to {email}"
    })
}


    except Exception as e:
        return {
    "statusCode": 500,
    "headers": {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type"
    },
    "body": json.dumps({"error": str(e)})
}



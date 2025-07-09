

import boto3


SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1:109249930734:weather-prediction-topic"


sns_client = boto3.client("sns", region_name="ap-south-1")

def send_forecast_email(email, city, forecast):
    temp = forecast[0]
    humidity = "N/A"
    wind = "N/A"


    message = (
    f"Tomorrow's forecast for {city}:\n"
    f"🌡️ Temperature: {temp:.2f}°C\n"
    f"💧 Humidity: {humidity}\n"
    f"🌬️ Wind Speed: {wind}"
    )


    sns_client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=message,
        Subject=f"Weather Forecast for {city}",
        MessageAttributes={
            'email': {
                'DataType': 'String',
                'StringValue': email
            }
        }
    )

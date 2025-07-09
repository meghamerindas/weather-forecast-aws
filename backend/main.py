from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from .fetch_weather import get_today_weather
from .predict_sagemaker import get_prediction
from .send_email import send_forecast_email


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/forecast")
async def forecast(city: str = Form(...), email: str = Form(...)):
    try:
        
        today_weather = get_today_weather(city)

        
        prediction = get_prediction(today_weather)

        
        send_forecast_email(email, city, prediction)

        return {
            "city": city,
            "forecast": prediction,
            "message": f"Forecast sent to {email}"
        }

    except Exception as e:
        return {"error": str(e)}

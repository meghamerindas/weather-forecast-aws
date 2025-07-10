# 🌦️ Weather Forecasting App (Deployed on AWS)

A full-stack weather forecasting web application that predicts tomorrow's temperature based on today's weather in India’s major cities. It is fully deployed using AWS services, making it fast, scalable, and cloud-native.

---

## 📋 Description

This app uses real-time weather data to predict tomorrow’s temperature using a machine learning model trained on historical data. The user selects a city and enters their email to receive the forecast.

---

## ☁️ Tech Stack

- **Frontend:** HTML, CSS (Frosted Glass UI), JavaScript
- **Backend:** FastAPI
- **Machine Learning:** Scikit-learn model deployed on **Amazon SageMaker**
- **Integration & Serverless:** AWS Lambda, API Gateway
- **Notifications:** AWS SNS (to email forecasts)
- **Hosting:** AWS S3 (static website hosting)

---

## 🧠 Machine Learning Model

- 📊 **Trained On:** One year of real Indian weather data (temperature, humidity, wind)
- 🎯 **Goal:** Predict **tomorrow’s temperature**
- ⚙️ **Algorithm:** Regression model (e.g., Linear Regression or RandomForest)
- 🔍 **Features:** Today's temperature, humidity, wind

---

## 🖼️ Frontend Screenshot

> 🔍 [Click here to view the full-sized UI image](images/Screenshot.png)

---


### 🔗 Live Frontend

🔗 **[Click here to visit the website](http://weather-forecast-frontend-megha.s3-website.ap-south-1.amazonaws.com)**


> 🌐 API Gateway Endpoint (Backend):  
`https://kqqvzl5hbf.execute-api.ap-south-1.amazonaws.com/forecast`

<!-- curl -X POST https://kqqvzl5hbf.execute-api.ap-south-1.amazonaws.com/forecast \ -->
  <!-- -H "Content-Type: application/json" \ -->
  <!-- -d '{"city": "Kochi", "email": "youremail@example.com"}' -->


---


## 📂 Folder Structure

```bash
weather_sagemaker_deploy/
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── backend/
│   ├── fetch_weather.py
│   ├── main.py
│   ├── predict_sagemaker.py
│   └── send_email.py
├── sagemaker/
│   ├── model.tar.gz
│   ├── inference.py
│   ├── create_model_and_endpoint.py
│   ├── test_sagemaker.py
│   ├── train_model.py
│   └── model.pkl
├── lambda/
│   └── lambda_function.py
├── dataset/
│   └── indian_weather_data.csv
├── images/
│   └── screenshot.png
├── requirements.txt
└── README.md
```


---
## 💻 Run Locally

### 🔧 1. Clone the project

```bash
git clone https://github.com/your-username/weather-forecast-aws.git
cd weather_sagemaker_deploy
```

### 🐍 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  
pip install -r requirements.txt
```

### 🚀 3. Start the FastAPI server

```bash
uvicorn backend.main:app --reload
```

### 🌐 4. Open `index.html` in your browser and test the form
---

## 🚀 AWS Deployment Workflow

| Step                  | Description                                                               |
|---------------------  |-------------------------------------------------------------------------- |
| ✅ Model Training    | Trained using `train_model.py`, exported to `model.pkl`                    |
| ✅ Model Deployment  | Packaged as `model.tar.gz`, deployed via `create_model_and_endpoint.py`    |
| ✅ Lambda Setup      | `lambda_function.py` handles prediction + email via SNS                    |
| ✅ API Gateway       | Connects Lambda to HTTP endpoint                                           |
| ✅ S3 Frontend       | HTML/CSS/JS hosted on S3 static website                                    |

---
## ✨ Features

- 🔁 Live weather fetched from Open-Meteo API
- 📈 Forecasts tomorrow’s temperature using ML
- 📬 Sends forecast to any user-supplied email
- 🧠 Model deployed on AWS SageMaker
- ☁️ Full AWS integration: Lambda, API Gateway, SNS, S3

---

## 👩‍💻 Contact

**Megha Merin Das**  
📧 Email: [smackeziya@gmail.com](mailto:smackeziya@gmail.com)  
📍 Kochi, Kerala, India  
🎓 Course: Data Science & AI, ExpertzLab
---

## 🏷️ Tags

#AWS #MachineLearning #SageMaker #Lambda #FastAPI #MLOps #WeatherForecast #CloudDeployment #PortfolioProject
---

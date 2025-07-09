import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib


df = pd.read_csv("indian_weather_data.csv")


df = df.dropna()


X = df[["temp", "humidity", "wind"]]  
y = df["target"]                       


model = LinearRegression()
model.fit(X, y)


joblib.dump(model, "model.pkl")
print("✅ model.pkl saved successfully.")

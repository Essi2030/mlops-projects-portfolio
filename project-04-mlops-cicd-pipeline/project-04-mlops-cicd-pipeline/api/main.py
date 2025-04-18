from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load the model and class names
model = joblib.load("iris_model.joblib")
with open("class_names.txt", "r") as f:
    class_names = [line.strip() for line in f.readlines()]

# Define input schema
class IrisInput(BaseModel):
    features: list  # Expecting a list of 4 float values

@app.get("/")
def read_root():
    return {"message": "Iris Classifier API is running!"}

@app.post("/predict")
def predict(input_data: IrisInput):
    X = np.array(input_data.features).reshape(1, -1)
    pred = model.predict(X)[0]
    label = class_names[pred]
    return {"prediction": label}


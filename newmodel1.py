from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import pickle
import pandas as pd

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Define input model
class House(BaseModel):
    area_sqft: float
    bedrooms: int
    age: int

# FastAPI app
app = FastAPI(title="House Prediction System")

@app.post("/predict")
def predict_house_price(h1: House):
    # Use user input for prediction
    input_data = pd.DataFrame([{
        "area_sqft": h1.area_sqft,
        "bedrooms": h1.bedrooms,
        "age": h1.age
    }])
    prediction = model.predict(input_data)[0]
    return JSONResponse(status_code=201, content={"prediction": round(prediction, 2)})

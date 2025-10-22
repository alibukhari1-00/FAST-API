# streamlit_app.py
import streamlit as st
import requests

st.set_page_config(page_title="House Price Prediction", layout="centered")
st.title("🏠 House Price Prediction System")

st.write("Enter house details to get the predicted price:")

# User inputs
area_sqft = st.number_input("Area (in sqft)", min_value=100.0, max_value=10000.0, value=500.0)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=2)
age = st.number_input("Age of the House", min_value=0, max_value=100, value=5)

# Predict button
if st.button("Predict Price"):
    # API URL (FastAPI should be running)
    url = "http://127.0.0.1:8000/predict"
    
    # Prepare input data for POST request
    payload = {
        "area_sqft": area_sqft,
        "bedrooms": bedrooms,
        "age": age
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 201:
            prediction = response.json()["prediction"]
            st.success(f"💰 Predicted House Price: ${prediction:,.2f}")
        else:
            st.error(f"Error: {response.text}")
    except Exception as e:
        st.error(f"API request failed: {e}")

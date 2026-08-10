import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("car_price_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Used Car Price Prediction",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 Used Car Price Prediction")
st.write("Enter the car details below to predict its price.")

# User inputs
model_name = st.text_input("Car Model", "Golf")

year = st.number_input(
    "Year",
    min_value=1990,
    max_value=2026,
    value=2018
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic", "Semi-Auto", "Other"]
)

mileage = st.number_input(
    "Mileage",
    min_value=0.0,
    value=30000.0
)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "Hybrid", "Electric", "Other"]
)

tax = st.number_input(
    "Tax",
    min_value=0.0,
    value=150.0
)

mpg = st.number_input(
    "MPG",
    min_value=0.0,
    value=50.0
)

engine_size = st.number_input(
    "Engine Size",
    min_value=0.0,
    value=1.4
)

make = st.text_input("Make", "Volkswagen")


# Prediction
if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "model": [model_name],
        "year": [year],
        "transmission": [transmission],
        "mileage": [mileage],
        "fuelType": [fuel_type],
        "tax": [tax],
        "mpg": [mpg],
        "engineSize": [engine_size],
        "Make": [make]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Car Price: {prediction[0]:,.2f}"
    )
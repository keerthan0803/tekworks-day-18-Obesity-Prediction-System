import streamlit as st
import pickle
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.preprocessing import MinMaxScaler

# Set page config with dark theme
st.set_page_config(
    page_title="Obesity Prediction",
    page_icon="🏥",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for black background
st.markdown("""
<style>
    [data-testid="stMainBlockContainer"] {
        background-color: #000000;
    }
    [data-testid="stAppViewBlockContainer"] {
        background-color: #000000;
    }
    .stApp {
        background-color: #000000;
    }
    [data-testid="stSidebarNav"] {
        background-color: #000000;
    }
    body {
        background-color: #000000;
    }
    .stTitle {
        color: #00FF00;
        text-align: center;
    }
    .stSubheader {
        color: #00FFFF;
    }
    .stText {
        color: #FFFFFF;
    }
</style>
""", unsafe_allow_html=True)

# Set background
page_bg_img = '''
<style>
[data-testid="stAppViewBlockContainer"] {
    background: linear-gradient(135deg, #000000 0%, #1a1a1a 100%);
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Create title
st.title("🏥 Obesity Prediction System")
st.markdown("---")

# Load models and scaler
@st.cache_resource
def load_models():
    model_path = Path("objects/rf.pkl")
    
    with open(model_path, 'rb') as f:
        rf_model = pickle.load(f)
    
    # Create and fit scaler using training data
    x_train = pd.read_csv("data/processed_data/x_train.csv")
    
    scaler = MinMaxScaler()
    scaler.fit(x_train[['Height', 'Weight']])
    
    return scaler, rf_model

scaler, rf_model = load_models()

# Obesity category mapping
obesity_map = {
    0: "🟢 Normal weight",
    1: "🔴 Obese",
    2: "🟡 Overweight",
    3: "🔵 Underweight"
}

# Create input form
st.subheader("Enter Your Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age (years)", min_value=1, max_value=120, value=25, step=1)
    height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0, step=0.1)
    bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=24.0, step=0.1)

with col2:
    gender = st.selectbox("Gender", ["Male", "Female"])
    weight = st.number_input("Weight (kg)", min_value=20.0, max_value=200.0, value=70.0, step=0.1)
    activity = st.slider("Physical Activity Level (1-5)", min_value=1, max_value=5, value=3)

# Prepare data for prediction
if st.button("🔮 Predict Obesity Category", use_container_width=True, key="predict"):
    # Encode gender
    gender_encoded = 1 if gender == "Male" else 0
    
    # Create dataframe with input values
    input_data = pd.DataFrame({
        'Age': [age],
        'Gender': [gender_encoded],
        'Height': [height],
        'Weight': [weight],
        'BMI': [bmi],
        'PhysicalActivityLevel': [activity]
    })
    
    # Scale Height and Weight
    input_data_scaled = input_data.copy()
    input_data_scaled[['Height', 'Weight']] = scaler.transform(input_data[['Height', 'Weight']])
    
    # Make prediction
    prediction = rf_model.predict(input_data_scaled)[0]
    prediction_proba = rf_model.predict_proba(input_data_scaled)[0]
    confidence = max(prediction_proba) * 100
    
    # Display results with balloon effect
    st.balloons()
    st.success(obesity_map[prediction])
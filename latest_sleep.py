import numpy as np
import pickle
import streamlit as st

# Load the saved model
loaded_model = pickle.load(open("sleep_disorder_prediction.pkl", "rb"))

# Streamlit App
st.title("Sleep Disorder Prediction App")

# Collect user inputs
gender = st.selectbox("Gender", [0, 1])  # Example: 0 = Female, 1 = Male
age = st.number_input("Age", min_value=0, max_value=100, value=25)
occupation = st.number_input("Occupation Code", min_value=0, value=0)
sleep_duration = st.number_input("Sleep Duration (hours)", min_value=0.0, value=7.0)
quality_of_sleep = st.number_input("Quality of Sleep", min_value=0.0, max_value=10.0, value=7.0)
physical_activity_level = st.number_input("Physical Activity Level", min_value=0.0, max_value=10.0, value=5.0)
stress_level = st.number_input("Stress Level", min_value=0.0, max_value=10.0, value=4.0)
bmi_category = st.number_input("BMI Category", min_value=0, max_value=3, value=1)  # Example: 0 = Underweight, 1 = Normal, etc.
heart_rate = st.number_input("Heart Rate (bpm)", min_value=30, max_value=150, value=70)
daily_steps = st.number_input("Daily Steps", min_value=0, value=5000)
systolic_bp = st.number_input("Systolic BP", min_value=80, max_value=200, value=120)
diastolic_bp = st.number_input("Diastolic BP", min_value=50, max_value=130, value=80)

# Prediction function
def predict_sleep_disorder():
    input_values = np.array([
        gender, age, occupation, sleep_duration,
        quality_of_sleep, physical_activity_level, stress_level,
        bmi_category, heart_rate, daily_steps,
        systolic_bp, diastolic_bp
    ]).reshape(1, -1)
    
    prediction = loaded_model.predict(input_values)
    
    if prediction[0] == 0:
        return "Patient has no sleep disorder."
    elif prediction[0] == 1 or prediction[0] == 2:
        return "Patient has a sleep disorder."

# Prediction button
if st.button("Predict"):
    result = predict_sleep_disorder()
    st.success(f"Prediction: {result}")

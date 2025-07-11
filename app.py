import streamlit as st
import pandas as pd
import joblib

# Load model, scaler, and expected columns
model = joblib.load("Logistic_regression_heart.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

# Page configuration
st.set_page_config(page_title="Heart Disease Predictor", page_icon="❤️", layout="centered")

# Title and description
st.title("❤️ Heart Disease Prediction App")
st.markdown("""
Welcome to the **Heart Disease Predictor** built by **Akarsh Jha**.
Fill out the patient's health details below and click **Predict** to know the risk level.
""")

# Sidebar - User Input
st.sidebar.header("📝 Enter Patient Details")

age = st.sidebar.slider("Age", 18, 100, 40)
resting_bp = st.sidebar.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
cholesterol = st.sidebar.number_input("Cholesterol (mg/dL)", 100, 600, 200)
fasting_bs = st.sidebar.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
max_hr = st.sidebar.slider("Max Heart Rate", 60, 220, 150)
oldpeak = st.sidebar.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
sex = st.sidebar.selectbox("Sex", ["M", "F"])
chest_pain = st.sidebar.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
resting_ecg = st.sidebar.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
exercise_angina = st.sidebar.selectbox("Exercise-Induced Angina", ["Y", "N"])
st_slope = st.sidebar.selectbox("ST Slope", ["Up", "Flat", "Down"])

# Predict button
if st.button("🔍 Predict Heart Disease Risk"):

    # Create raw input dict with manual one-hot encoding
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    # Convert to DataFrame
    input_df = pd.DataFrame([raw_input])

    # Fill in missing columns with 0s
    for col in columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns
    input_df = input_df[columns]

    # Scale input
    scaled_input = scaler.transform(input_df)

    # Predict
    prediction = model.predict(scaled_input)[0]
    probability = model.predict_proba(scaled_input)[0][1]

    # Display result
    st.subheader("📊 Prediction Result")
    st.metric("Risk Probability", f"{probability:.2%}")

    if prediction == 1:
        st.error("⚠️ The patient is at **high risk** of heart disease.")
    else:
        st.success("✅ The patient is at **low risk** of heart disease.")

    # Show input features (for review)
    with st.expander("📋 Input Features"):
        st.dataframe(input_df)

import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("rfr_model")

def preprocess_input(age, sex, bmi, children, smoker):
    data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker]
    })
    return data

def predict_insurance_charge(data):
    prediction = model.predict(data)
    return prediction

def main():
    st.title("Insurance Charge Estimation")
    st.sidebar.title("User Input")

    age = st.sidebar.slider("Age", 20, 100, step=1, value=30)
    sex = st.sidebar.selectbox("Sex", [0, 1], format_func=lambda x: "Male" if x == 0 else "Female")
    bmi = st.sidebar.slider("BMI", 10.0, 40.0, step=0.1, value=20.0)
    children = st.sidebar.slider("Number of Children", 0, 10, step=1, value=0)
    smoker = st.sidebar.selectbox("Smoker", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

    input_data = preprocess_input(age, sex, bmi, children, smoker)

    prediction = predict_insurance_charge(input_data)

    st.subheader("Estimated Insurance Charge:")
    result_placeholder = st.empty()
    result_placeholder.write(prediction[0])


if __name__ == "__main__":
    main()

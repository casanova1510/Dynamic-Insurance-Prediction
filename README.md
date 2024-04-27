# Dynamic Insurance Prediction

![Insurance](https://cdn.pixabay.com/photo/2017/09/03/11/19/insurance-2700812_960_720.jpg)

## Overview

Welcome to the dynamic insurance prediction web application! In this project, I used different machine learning techniques to predict insurance charges based on various customer conditions. I have employed a Random Forest Regressor model, which showed superior performance in this analysis.

## Installation

1. **Clone the repository:**
   
git clone <https://github.com/casanova1510/Dynamic-Insurance-Prediction.git>


2. **Navigate to the project directory:**  
cd dynamic-insurance-prediction


3. **Install dependencies:**  
Ensure you have Python and pip installed. Then, install the required Python packages by running:
pip install -r requirements.txt

This command will install necessary packages such as Streamlit for running the application.

## Data Preprocessing and Model Training

We start by loading the dataset and performing essential preprocessing operations to prepare the data for model training.

## Requirements

Ensure you have the following versions of packages specified in your `requirements.txt` file:

```text
pandas==1.5.3
numpy==1.22.4
joblib==1.2.0
streamlit==1.24.0

**Application**

Our application is built using Streamlit. You can interact with it to get predictions on insurance charges based on user input.

**Usage**

Run the application:

streamlit run app.py

This command will start the Streamlit server, and you can access the application through your web browser.

Input User Data:

Once the application is running, you can use the sliders and dropdowns on the sidebar to input user data such as age, sex, BMI, number of children, and smoking status.

View Prediction:

After entering the user data, the application will display the estimated insurance charge based on the input.

Feel free to explore and interact with the application to estimate insurance charges based on different scenarios!


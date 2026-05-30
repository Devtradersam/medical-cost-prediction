import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load('medical_cost_model.pkl')

# App title
st.title('Medical Cost Prediction App')
st.write('Fill in the details below to predict medical insurance charges')

# Input fields
age = st.slider('Age', min_value=18, max_value=64, value=30)
bmi = st.slider('BMI', min_value=15.0, max_value=55.0, value=30.0, step=0.1)
children = st.slider('Number of Children', min_value=0, max_value=5, value=0)

sex = st.selectbox('Sex', ['Female', 'Male'])
smoker = st.selectbox('Smoker?', ['No', 'Yes'])
region = st.selectbox('Region', ['Northeast', 'Northwest', 'Southeast', 'Southwest'])

# Convert inputs to numbers (same way we did in the notebook)
sex_male = 1 if sex == 'Male' else 0
smoker_yes = 1 if smoker == 'Yes' else 0
region_northwest = 1 if region == 'Northwest' else 0
region_southeast = 1 if region == 'Southeast' else 0
region_southwest = 1 if region == 'Southwest' else 0

# Predict button
if st.button('Predict Medical Cost'):
    input_data = np.array([[age, bmi, children, sex_male, smoker_yes,
                            region_northwest, region_southeast, region_southwest]])
    prediction = model.predict(input_data)
    st.success(f'Estimated Medical Cost: ${prediction[0]:,.2f}')
import streamlit as st
from predictions import predict

st.title("Healthcare Insurance Premium Prediction")

categorical_options = {
    "Gender": ['Male', 'Female'],
    "Region": ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    "Marital Status": ['Unmarried', 'Married'],
    "BMI Category": ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    "Smoking Status": ['No Smoking', 'Regular', 'Occasional'],
    "Employment Status" : ['Salaried', 'Self-Employed', 'Freelancer'],
    "Income Level" : ['<10L', '10L - 25L', '> 40L', '25L - 40L'],
    "Medical History": ['Diabetes', 'High blood pressure', 'No Disease',
       'Diabetes & High blood pressure', 'Thyroid', 'Heart disease',
       'High blood pressure & Heart disease', 'Diabetes & Thyroid',
       'Diabetes & Heart disease'],
    "Insurance Plan": ['Bronze', 'Silver', 'Gold']
}


row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)
row5 = st.columns(3)


with row1[0]:
    age = st.number_input('Age', min_value=18, max_value=100, step=1)
with row1[1]:
    number_of_dependants = st.number_input('Number of Dependents',min_value=0,max_value=20,step=1)
with row1[2]:
    income_lakhs = st.number_input('Income in Lakhs',min_value=0,max_value=200,step=1)

with row2[0]:
    genetical_risk = st.number_input('Genetical Risk',min_value=0,max_value=5,step=1)
with row2[1]:
    gender = st.selectbox('Gender',categorical_options['Gender'])
with row2[2]:
    region = st.selectbox('Region',categorical_options['Region'])

with row3[0]:
    marital_status = st.selectbox('Marital Status',categorical_options['Marital Status'])
with row3[1]:
    bmi_category = st.selectbox('BMI Category',categorical_options['BMI Category'])
with row3[2]:
    smoking_status = st.selectbox('Smoking Status',categorical_options['Smoking Status'])

with row4[0]:
    employment_status = st.selectbox('Employment Status',categorical_options['Employment Status'])
with row4[1]:
    income_level = st.selectbox('Income Level',categorical_options['Income Level'])
with row4[2]:
    insurance_plan = st.selectbox('Insurance Plan',categorical_options['Insurance Plan'])

with row5[0]:
    medical_history = st.selectbox('Medical History',categorical_options['Medical History'])


# Create a dictionary for input values
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Gender': gender,
    'Region': region,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Employment Status': employment_status,
    'Income Level': income_level,
    'Insurance Plan': insurance_plan,
    'Medical History': medical_history
}



if st.button("Preditct"):
    prediction = predict(input_dict)
    st.success(f"Predicted Premium =  {prediction[0]:,.2f}")
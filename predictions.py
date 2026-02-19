import pandas as pd
import joblib


model_young = joblib.load('artifacts/model_young.joblib')
model_rest = joblib.load('artifacts/model_rest.joblib')


def preprocess_input(input_dict):
    expected_columns = ['age', 'gender', 'region', 'marital_status', 'number_of_dependants',
       'bmi_category', 'smoking_status', 'employment_status', 'income_level',
       'income_lakhs', 'insurance_plan', 'genetical_risk', 'risk_score']
    
    df = pd.DataFrame([input_dict])
    df.columns = df.columns.str.replace(' ','_').str.lower()

    risk_scores = {
        'diabetes':6,
        'heart disease':8,
        'high blood pressure':6,
        'thyroid':5,
        'no disease':0,
    }
    
    if df['medical_history'].str.contains('&').iloc[0]:
        df[['disease_1','disease_2']] = df['medical_history'].str.lower().str.split(' & ',expand=True).apply(lambda x:x.str.lower())
        df['disease_1'] = df['disease_1'].map(risk_scores)
        df['disease_2'] = df['disease_2'].map(risk_scores).fillna(0)
        df['risk_score'] = df['disease_1']+df['disease_2']
        df = df.drop(['medical_history','disease_1','disease_2'],axis=1)
    else:
        df['risk_score'] = df['medical_history'].str.lower().map(risk_scores)
        df = df.drop('medical_history',axis=1)

    df['income_level'] = df['income_level'].map({'<10L':1,'10L - 25L':2,'> 40L':3,'25L - 40L':4})

    df['insurance_plan'] = df['insurance_plan'].map({'Bronze':1,'Silver':1,'Gold':3})

    return df


def predict(input_dict):
    input_df = preprocess_input(input_dict)
    if (input_df['age']<=25).iloc[0]:
        prediction = model_young.predict(input_df)
    else:
        prediction = model_rest.predict(input_df)
    return prediction
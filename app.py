import streamlit as st
import pandas as pd
import numpy as np
import joblib


model = joblib.load("C:\\Users\\Megha\\OneDrive\\Desktop\\credit_risk2\\credit_risk_model.pkl")

st.set_page_config(page_title="Credit Risk Prediction", layout="centered")

# App Title
st.title("CREDIT RISK & LOAN DEFAULT PREDICTION")
st.write("Predict the probability of loan default using machine learning")

st.markdown("---")

# ======================
# User Input Section
# ======================
st.header("Applicant Information")

col1, col2 = st.columns(2)

with col1:
    person_age = st.number_input("Age", min_value=18, max_value=100, value=30)
    person_income = st.number_input("Annual Income", min_value=0, value=50000)
    person_emp_length = st.slider("Employment Length (Years)", 0, 40, 5)
    person_home_ownership = st.selectbox(
        "Home Ownership",
        ["RENT", "OWN", "MORTGAGE", "OTHER"]
    )
    cb_person_default_on_file = st.selectbox(
        "Previous Default on File",
        ["Y", "N"]
    )

with col2:
    loan_amnt = st.number_input("Loan Amount", min_value=0, value=10000)
    loan_int_rate = st.slider("Interest Rate (%)", 1.0, 30.0, 10.0)
    loan_intent = st.selectbox(
        "Loan Purpose",
        ["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "HOMEIMPROVEMENT", "DEBTCONSOLIDATION"]
    )
    loan_grade = st.selectbox(
        "Loan Grade",
        ["A", "B", "C", "D", "E", "F", "G"]
    )
    cb_person_cred_hist_length = st.slider(
        "Credit History Length (Years)", 0, 30, 5
    )

# ======================
# Prediction
# ======================
st.markdown("---")

if st.button("Predict Loan Risk"):
    input_data = pd.DataFrame({
        "person_age": [person_age],
        "person_income": [person_income],
        "person_emp_length": [person_emp_length],
        "person_home_ownership": [person_home_ownership],
        "loan_amnt": [loan_amnt],
        "loan_intent": [loan_intent],
        "loan_grade": [loan_grade],
        "loan_int_rate": [loan_int_rate],
        "loan_percent_income": [loan_amnt / person_income if person_income > 0 else 0],
        "cb_person_default_on_file": [cb_person_default_on_file],
        "cb_person_cred_hist_length": [cb_person_cred_hist_length]
    })

    probability = model.predict_proba(input_data)[0][1]
    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error(f"High Risk Applicant\n\n**Default Probability:** {probability:.2%}")
    else:
        st.success(f"Low Risk Applicant\n\n**Default Probability:** {probability:.2%}")

    st.progress(float(probability))

    st.markdown("### Risk Interpretation")
    st.write("""
    - Higher probability indicates higher default risk  
    - Model considers income, interest rate, credit history, and loan intent  
    - Final decision should combine ML output with business rules
    """)

# Footer
st.markdown("---")
st.caption("Built by Megha Shinde | Credit Risk ML Project")

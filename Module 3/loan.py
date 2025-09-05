import streamlit as st

st.title("Loan EMI Estimator")

loan_amount = st.slider("Loan Amount:", min_value=1000, max_value=100000, value=50000)
interest_rate = st.slider("Interest Rate (%):", min_value=1, max_value=20, value=8)
loan_tenure = st.slider("Loan Tenure (years):", min_value=1, max_value=30, value=5)

monthly_interest_rate = interest_rate / (12 * 100)
emi = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate)**(loan_tenure * 12)) / ((1 + monthly_interest_rate)**(loan_tenure * 12) - 1)

st.write("---")
st.write(f"Estimated EMI: ${emi:.2f}")
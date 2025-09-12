import streamlit as st

st.title("💸 Tip Calculator")

# Input fields
bill_amount = st.number_input("Enter Bill Amount (₹)", min_value=0.0, step=50.0)
tip_percent = st.number_input("Enter Tip Percentage (%)", min_value=0.0, max_value=100.0, step=1.0)

# Calculations
tip_amount = (bill_amount * tip_percent) / 100
final_bill = bill_amount + tip_amount

# Results
st.subheader("📊 Bill Summary")
st.metric(label="Tip Amount", value=f"₹{tip_amount:.2f}")
st.metric(label="Final Bill (with Tip)", value=f"₹{final_bill:.2f}")
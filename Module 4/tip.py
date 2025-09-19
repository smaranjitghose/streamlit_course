import streamlit as st

# App Title
st.title("💸 TipMate")

st.write("No more mental math — calculate your tip in seconds!")

# Static bill amount
bill_amount = 1000.0  # fixed bill amount (₹)

# User inputs
name = st.text_input("👤 Enter Your Name")
tip_percent = st.number_input("💯 Enter Tip Percentage (%)", min_value=0.0, max_value=100.0, step=1.0)

# Calculations
tip_amount = (bill_amount * tip_percent) / 100
final_bill = bill_amount + tip_amount

# Results Section
st.subheader("📊 Bill Summary")
st.metric(label="💵 Bill Amount", value=f"₹{bill_amount:.2f}")
st.metric(label="💰 Tip Amount", value=f"₹{tip_amount:.2f}")
st.metric(label="🧾 Final Bill (with Tip)", value=f"₹{final_bill:.2f}")

if name and tip_percent > 0:
    st.write(f"Thanks, {name}! Your tip is ₹{tip_amount:.2f}, making the total ₹{final_bill:.2f}.")
import streamlit as st

st.title("🏢 Employee Portal")
st.write("Welcome! What would you like to do?")

st.page_link("pages/payslips.py", label="💰 View Payslips")
st.page_link("pages/leave.py", label="🌴 Request Leave")
st.page_link("pages/profile.py", label="👤 Edit Profile")

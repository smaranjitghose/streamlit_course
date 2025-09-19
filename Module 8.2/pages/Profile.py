import streamlit as st

st.title("👤 Profile")

name = st.text_input("Name", value="John Smith")
email = st.text_input("Email", value="john@company.com")

if st.button("Update Profile"):
    st.success("Profile updated!")

st.page_link("Employee_Portal.py", label="← Back to Portal")
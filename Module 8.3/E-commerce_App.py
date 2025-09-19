import streamlit as st

st.title("🛒 Shop Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "admin" and password == "password":
        st.success("Login successful! Redirecting...")
        st.switch_page("pages/dashboard.py")
    else:
        st.error("Invalid username or password")

st.write("**Demo credentials:** admin / password")
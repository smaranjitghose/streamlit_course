import streamlit as st

st.title("📊 Dashboard")

# Authentication check
if not st.session_state.get("logged_in", False):
    st.warning("Please log in first!")
    st.switch_page("main.py")

st.success(f"Hello, {st.session_state.username}! Welcome to your dashboard.")

# Navigation
if st.button("Go to Reports"):
    st.switch_page("pages/2_Reports.py")
if st.button("Go to Settings"):
    st.switch_page("pages/3_Settings.py")

# Logout
if st.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.switch_page("main.py")

import streamlit as st

st.title("⚙️ Settings")

# Authentication check
if not st.session_state.get("logged_in", False):
    st.warning("Please log in first!")
    st.switch_page("main.py")

st.write(f"{st.session_state.username}, you can update your settings here.")

# Navigation
if st.button("Go to Dashboard"):
    st.switch_page("pages/1_Dashboard.py")
if st.button("Go to Reports"):
    st.switch_page("pages/2_Reports.py")

# Logout
if st.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.switch_page("main.py")

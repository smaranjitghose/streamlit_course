import streamlit as st
import time

st.title("📂 File Upload Monitor")

uploaded_file = st.file_uploader("Upload a file")

if uploaded_file:
    st.info("Processing your file...")
    progress_bar = st.progress(0)  # start at 0%

    for percent in range(100):
        time.sleep(0.01)  # simulate processing
        progress_bar.progress(percent + 1)  # update bar

    st.success("File processed successfully!")

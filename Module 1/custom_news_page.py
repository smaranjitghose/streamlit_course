import streamlit as st

st.set_page_config(
    page_title="My Awesome News Page",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Welcome to My Awesome News Page!")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top Stories")
    st.write("- Story 1: Streamlit makes Python apps easy!")
    st.write("- Story 2: Data Science trends in 2025")

with col2:
    st.subheader("Weather Update")
    st.write("☀️ Sunny, 32°C")
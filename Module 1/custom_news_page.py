import streamlit as st

st.set_page_config(
    page_title="My Awesome News Page",
    page_icon="📰",
    layout="wide"
)

st.title("📰 Welcome to My Awesome News Page!")

st.subheader("🔥 Top Stories")
st.write("- 🚀 Streamlit makes Python apps easy!")
st.write("- 📊 Data Science trends in 2025")

st.subheader("🌤️ Weather Update")
st.write("☀️ Sunny, 32°C")

st.subheader("💡 Fun Fact of the Day")
st.write("🤔 Did you know? Streamlit was designed to turn data scripts into shareable web apps in minutes!")

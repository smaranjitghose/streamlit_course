import streamlit as st
import random

quotes = [
    "The best way to predict the future is to invent it.",
    "Simplicity is the soul of efficiency.",
    "Do one thing every day that scares you.",
    "Code is like humor. When you have to explain it, it’s bad."
]

st.title("🌟 Daily Quote Board")
st.write("Refresh the page for a new dose of inspiration!")

quote = random.choice(quotes)
st.title(quote)
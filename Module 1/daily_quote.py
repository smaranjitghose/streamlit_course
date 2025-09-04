import streamlit as st
import random

quotes = [
    "The best way to get started is to quit talking and begin doing.",
    "Dream bigger. Do bigger.",
    "Do something today that your future self will thank you for.",
    "Push yourself, because no one else is going to do it for you."
]

st.title("🌟 Daily Quote Board")

if st.button("Get a New Quote ✨"):
    st.write(random.choice(quotes))
else:
    st.write("Click the button to get a motivational quote!")

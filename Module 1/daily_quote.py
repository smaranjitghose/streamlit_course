import streamlit as st
import random

# List of inspiring quotes
quotes = [
    '"🌱 The best way to predict the future is to invent it."',
    '"⚡ Simplicity is the soul of efficiency."', 
    '"🔥 Do one thing every day that scares you."',
    '"💻 Code is like humor. When you have to explain it, it is bad "',
    '"🌟 Great things never come from comfort zones."',
    '"🚀 Stay hungry, stay foolish."'
]

st.title("☕ The Morning Ritual")
st.write("Welcome to FlowState Labs' digital campfire. Let's start our day with some inspiration!")

# Pick a random quote
quote = random.choice(quotes)

# Display the daily quote
st.write("💡 Today's Quote")
st.subheader(quote)

# Fun extra: prompt for team reflection
st.write("💬 What does this quote mean to you? Share your thoughts with the team!")

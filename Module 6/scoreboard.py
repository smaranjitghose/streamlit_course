import streamlit as st 
import time

st.title("Live Scoreboard 🏏") 
# Create a placeholder 
score_placeholder = st.empty()

score = 0  
for i in  range(5):
    score += 4  # Imagine scoring runs 
    score_placeholder.metric("Current Score", f"{score}")
    time.sleep(1)
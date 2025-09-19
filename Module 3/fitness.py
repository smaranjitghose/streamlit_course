import streamlit as st
import random

st.title("🏋️ Fitness Dashboard")

# Generate mock fitness data
steps_today = 10500
steps_change = 800
calories_burned = 2200
calories_change = -150
heart_rate = 82
hr_change = -3

# Display the metrics
st.metric(label="🏃 Steps Today", value=f"{steps_today:,}", delta=steps_change)
st.metric(label="🔥 Calories Burned", value=f"{calories_burned} kcal", delta=f"{calories_change} kcal")
st.metric(label="💓 Average Heart Rate", value=f"{heart_rate} bpm", delta=f"{hr_change} bpm")
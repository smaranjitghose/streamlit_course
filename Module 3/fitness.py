import streamlit as st
import random

# Page setup
st.set_page_config(page_title="🏋️ Fitness Dashboard", layout="centered")

st.title("🏋️ Fitness Dashboard")

st.divider()
# Mock/Simulated data
steps_today = random.randint(8000, 12000)
steps_change = random.randint(-500, 500)

calories_today = random.randint(1800, 2800)
calories_change = random.randint(-200, 200)

heart_rate = random.randint(70, 95)
hr_change = random.randint(-10, 10)

# Display metrics vertically (no columns)
st.metric(label="🏃 Steps Today", value=f"{steps_today:,}", delta=f"{steps_change:+}")

st.metric(label="🔥 Calories Burned", value=f"{calories_today} kcal", delta=f"{calories_change:+} kcal")

st.metric(label="💓 Avg Heart Rate", value=f"{heart_rate} bpm", delta=f"{hr_change:+} bpm")

st.write("✅ Fitness Dashboard ready! Use it to track activity and progress daily.")

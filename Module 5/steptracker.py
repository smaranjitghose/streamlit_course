import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Fitness Dashboard", layout="wide")
st.title("📊 My Fitness Dashboard")

# Fake dataset for 7 days
days = pd.date_range(start="2023-01-01", periods=7)
data = pd.DataFrame({
    "Steps": np.random.randint(3000, 12000, size=7),
    "Calories Burned": np.random.randint(1800, 2800, size=7),
    "Hours Slept": np.random.uniform(5, 9, size=7).round(1)
}, index=days)

# Dashboard sections
st.subheader("👟 Daily Steps")
st.line_chart(data["Steps"])

st.subheader("🔥 Calories Burned")
st.bar_chart(data["Calories Burned"])

st.subheader("💤 Sleep Hours")
st.area_chart(data["Hours Slept"])

# Preview of raw data
st.subheader("📋 Data Table")
st.dataframe(data)

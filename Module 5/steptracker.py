import streamlit as st
import pandas as pd
import numpy as np

st.title("Step Tracker App 👟")

# Generate 7 days of mock step data
days = pd.date_range(start="2023-01-01", periods=7)
steps = np.random.randint(3000, 12000, size=7)

data = pd.DataFrame({"Steps": steps}, index=days)

st.subheader("Daily Step Counts")
st.line_chart(data)

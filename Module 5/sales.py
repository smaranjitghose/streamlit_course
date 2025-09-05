import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Sales Dashboard 📈")

months = pd.date_range("2023-01-01", periods=6, freq="M")
sales = np.random.randint(1000, 5000, size=6)
df = pd.DataFrame({"Month": months, "Sales": sales})

st.subheader("Monthly Sales Overview")

fig = px.bar(df, x="Month", y="Sales", title="Sales Over Time", text="Sales")
fig.update_traces(textposition="outside")

st.plotly_chart(fig, use_container_width=True)

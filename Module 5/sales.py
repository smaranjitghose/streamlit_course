import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📊 Sales Dashboard")

# Fake dataset (12 months for more flexibility)
months = pd.date_range("2023-01-01", periods=12, freq="M")
data = pd.DataFrame({
    "Month": np.tile(months, 3),
    "Region": np.repeat(["North", "South", "West"], 12),
    "Sales": np.random.randint(1000, 5000, size=36),
    "Profit": np.random.randint(200, 1500, size=36)
})

# Sidebar filter
st.sidebar.header("🔎 Filters")
months_to_show = st.sidebar.slider("Select number of recent months:", 3, 12, 6)
region_choice = st.sidebar.selectbox("Select Region for Detailed View:", data["Region"].unique())

# Filter dataset by recent months
latest_months = data["Month"].sort_values().unique()[-months_to_show:]
filtered_data = data[data["Month"].isin(latest_months)]

# Chart 1: Sales overview
st.subheader("📈 Monthly Sales Overview")
fig1 = px.bar(filtered_data, x="Month", y="Sales", color="Region", barmode="group",
              title="Sales by Region")
st.plotly_chart(fig1, use_container_width=True)

# Chart 2: Profit trend
st.subheader("💰 Profit Trend")
fig2 = px.line(filtered_data, x="Month", y="Profit", color="Region", markers=True,
               title="Monthly Profit by Region")
st.plotly_chart(fig2, use_container_width=True)

# Chart 3: Regional focus
st.subheader(f"🎯 Sales Trend in {region_choice}")
region_data = filtered_data[filtered_data["Region"] == region_choice]
fig3 = px.area(region_data, x="Month", y="Sales",
               title=f"Sales Trend in {region_choice}", markers=True)
st.plotly_chart(fig3, use_container_width=True)

# Raw data
st.subheader("📋 Filtered Data Table")
st.dataframe(filtered_data)

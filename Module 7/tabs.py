import streamlit as st
import pandas as pd
import numpy as np

st.title("📈 Investment Portfolio Dashboard")
st.write("Organize your investments into clean sections with tabs")

# Sample dates for charts
dates = pd.date_range("2024-01-01", periods=30, freq="D")

# Tabs for different asset classes
tab1, tab2, tab3= st.tabs(["🇮🇳 Stocks India", "🇺🇸 Stocks US", "₿ Crypto"])

# --- Tab 1: Indian Stocks ---
with tab1:
    st.header("Indian Stock Holdings")
    st.metric("Total Value", "₹2,45,000", "+₹12,500")
    
    data = pd.DataFrame({
        "Date": dates,
        "Value": np.cumsum(np.random.randn(30) * 1000) + 200000
    })
    st.line_chart(data.set_index("Date"))

# --- Tab 2: US Stocks ---
with tab2:
    st.header("US Stock Holdings")
    st.metric("Total Value", "$45,600", "+$2,100")
    
    data = pd.DataFrame({
        "Date": dates,
        "Value": np.cumsum(np.random.randn(30) * 500) + 40000
    })
    st.line_chart(data.set_index("Date"))

# --- Tab 3: Cryptocurrency ---
with tab3:
    st.header("Cryptocurrency Holdings")
    st.metric("Total Value", "$12,400", "-$800")
    
    data = pd.DataFrame({
        "Date": dates,
        "Value": np.cumsum(np.random.randn(30) * 400) + 10000
    })
    st.line_chart(data.set_index("Date"))



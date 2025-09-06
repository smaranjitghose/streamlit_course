import streamlit as st
import time
import random

st.title("📈 Stock Price Fetcher")

@st.cache_data
def get_stock_price(symbol):
    time.sleep(2)  # simulate slow API call
    return round(random.uniform(100, 200), 2)

symbol = st.text_input("Enter stock symbol", "AAPL")
if st.button("Get Price"):
    price = get_stock_price(symbol)
    st.metric(label=f"{symbol} Price", value=f"${price}")

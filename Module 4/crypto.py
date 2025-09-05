import streamlit as st
import random

st.title("Crypto Price Monitor 💰")

# Mock data (instead of API to keep it simple for beginners)
price = random.uniform(25000, 30000)  # Random Bitcoin price
change = random.uniform(-500, 500)    # Random change

st.metric(label="Bitcoin Price (USD)", value=f"${price:,.2f}", delta=f"{change:+.2f}")
import streamlit as st

st.title("Currency Comparison Tool 💱") 
# Create two columns 
col1, col2 = st.columns(2) 
with col1:
    st.subheader("USD")
    st.metric("1 USD", "0.92 EUR") 
with col2:
    st.subheader("EUR")
    st.metric("1 EUR", "1.09 USD")
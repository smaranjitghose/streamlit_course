import streamlit as st
import pandas as pd

st.title("Budget Tracker 💸")

uploaded_file = st.file_uploader("Upload your expense CSV", type="csv")

if uploaded_file is not None:
    # Load CSV into DataFrame
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Preview of Your Expenses")
    st.dataframe(df.head())  # Show first few rows
    
    # Calculate total expenses
    if "Amount" in df.columns:
        total_expenses = df["Amount"].sum()
        st.metric("Total Expenses", f"${total_expenses:,.2f}")
    else:
        st.warning("Your CSV should have a column named 'Amount'.")
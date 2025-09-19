import streamlit as st
import pandas as pd

st.title("Personal Expense Tracker")
st.write("Track and analyze your monthly spending")

# Sample expense data
data = {
    "Date": ["2024-09-01", "2024-09-02", "2024-09-05", "2024-09-08", "2024-09-12"],
    "Category": ["Food", "Transport", "Shopping", "Bills", "Food"],
    "Amount": [450, 120, 999, 2200, 300]
}

df = pd.DataFrame(data)

st.header("Expense Records")
st.dataframe(df)

# Calculate summary statistics
total_expense = df["Amount"].sum()
avg_expense = df["Amount"].mean()
max_expense = df["Amount"].max()

st.divider()

# Create summary table
summary_data = {
    "Metric": ["Total Spent", "Average Transaction", "Highest Expense"],
    "Value": [total_expense, f"{avg_expense:.2f}", max_expense]
}
summary_df = pd.DataFrame(summary_data)

st.subheader("Quick Summary Table")
st.table(summary_df)
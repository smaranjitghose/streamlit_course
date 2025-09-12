import streamlit as st
import pandas as pd

# Page setup
st.title("💰 Personal Expense Tracker")

# Sample expense log
data = {
    "Date": ["2025-09-01", "2025-09-02", "2025-09-05", "2025-09-08", "2025-09-12"],
    "Category": ["Food", "Transport", "Shopping", "Bills", "Food"],
    "Amount (₹)": [450, 120, 999, 2200, 300]
}
df = pd.DataFrame(data)

# Display interactive expense table
st.header("📊 Expense Log")
st.write("Here is the record of all your expenses:")
st.dataframe(df)

# Show summary stats (using write instead of metric)
total_expense = df["Amount (₹)"].sum()
avg_expense = df["Amount (₹)"].mean()
max_expense = df["Amount (₹)"].max()

st.divider()
st.header("📈 Expense Summary")
st.subheader("Key Insights")
st.write(f"✅ **Total Expense**: ₹{total_expense}")
st.write(f"✅ **Average Expense**: ₹{avg_expense:.2f}")
st.write(f"✅ **Highest Expense**: ₹{max_expense}")

st.divider()

# Static snapshot (useful for reports/exports)
st.header("📋 Summary Table")
summary = {
    "Total": [total_expense],
    "Average": [avg_expense],
    "Highest": [max_expense]
}
st.table(pd.DataFrame(summary))
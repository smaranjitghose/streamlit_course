import streamlit as st
import pandas as pd

st.title("💰 CSV Expense Analyzer")

# File upload
uploaded_file = st.file_uploader("Upload your expense CSV file", type="csv")

if uploaded_file is not None:
    # Read and preview the data
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Data Preview")
    st.write("First 10 rows of your expenses:")
    st.dataframe(df.head(10))
    
    # Group by category and calculate totals
    if 'Category' in df.columns and 'Amount' in df.columns:
        st.subheader("Spending by Category")
        category_totals = df.groupby('Category')['Amount'].sum().reset_index()
        st.dataframe(category_totals)
        
        # Download summary
        csv_summary = category_totals.to_csv(index=False)
        st.download_button(
            "Download Summary CSV",
            data=csv_summary,
            file_name="expense_summary.csv",
            mime="text/csv"
        )
    else:
        st.warning("CSV must have 'category' and 'amount' columns")
else:
    st.info("Please upload a CSV file to begin analysis")
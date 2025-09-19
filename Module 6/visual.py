import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("💰 Personal Finance Dashboard")
st.write("Upload your expense tracker CSV to analyze spending patterns.")

# Step 1: Upload CSV
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=['Date'])
    st.write("Expense Data Preview:")
    st.dataframe(df.head(10))
    
    # Step 2: Line Chart for Expenses Over Time
    st.subheader("📈 Daily Spending Over Time")
    daily = df.groupby('Date')['Amount'].sum().reset_index()
    
    # Streamlit built-in line chart
    st.line_chart(daily.set_index('Date'))
    
    # Step 3: Bar Chart for Category Spending
    st.subheader("🏷️ Total Spending by Category")
    category_totals = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
    
    # Matplotlib horizontal bar chart
    fig, ax = plt.subplots()
    ax.barh(category_totals.index, category_totals.values, color='skyblue')
    ax.set_xlabel('Total Spent ($)')
    ax.set_title('Spending by Category')
    st.pyplot(fig)
    
    # Optional: Interactive Plotly version
    fig2 = px.bar(df.groupby('Category')['Amount'].sum().reset_index(),
                  x='Amount', y='Category', orientation='h',
                  color='Category', title="Interactive Category Spending")
    st.plotly_chart(fig2, use_container_width=True)
    
    # Step 4: Key Metrics for Top 3 Spending Categories
    st.subheader("📊 Top Spending Categories")
    top3 = category_totals.head(3)
    for i, (cat, amt) in enumerate(top3.items(), 1):
        st.metric(f"{i}. {cat}", f"${amt:,.2f}")
    
    # Additional Insight: Average Daily Spending
    avg_daily = daily['Amount'].mean()
    st.metric("📈 Average Daily Spending", f"${avg_daily:,.2f}")

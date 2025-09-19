import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

st.title("📈 Sales Analytics Dashboard")
st.write("Interactive business intelligence for small business owners")

# Sample sales data
np.random.seed(42)
dates = pd.date_range('2024-01-01', '2024-06-30', freq='D')
categories = ['Electronics', 'Clothing', 'Home & Garden', 'Books', 'Sports']
regions = ['North', 'South', 'East', 'West']

sample_data = []
for date in dates[:90]:  # 3 months of data
    for _ in range(np.random.randint(3, 8)):  # 3-7 sales per day
        sample_data.append({
            'Date': date,
            'Category': np.random.choice(categories),
            'Region': np.random.choice(regions),
            'Revenue': np.random.uniform(50, 500),
            'Units_Sold': np.random.randint(1, 10)
        })

df = pd.DataFrame(sample_data)
st.write("Sample Sales Data Preview:")
st.dataframe(df.head())

# 1. Interactive Revenue Trend Line Chart
st.subheader("📊 Revenue Trend Over Time")
daily_revenue = df.groupby('Date')['Revenue'].sum().reset_index()
fig1 = px.line(daily_revenue, x='Date', y='Revenue', 
               title='Daily Revenue Trend',
               labels={'Revenue': 'Revenue ($)', 'Date': 'Date'})
fig1.update_traces(line=dict(width=3, color='#1f77b4'))
fig1.update_layout(hovermode='x unified')
st.plotly_chart(fig1, use_container_width=True)

# 2. Category Breakdown Pie Chart
st.subheader("🍰 Sales by Product Category")
category_sales = df.groupby('Category')['Revenue'].sum().reset_index()
fig2 = px.pie(category_sales, values='Revenue', names='Category',
              title='Revenue Distribution by Category',
              color_discrete_sequence=px.colors.qualitative.Set3)
fig2.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig2, use_container_width=True)

# 3. Regional Performance Bar Chart
st.subheader("🗺️ Regional Sales Performance")
region_sales = df.groupby('Region')['Revenue'].sum().reset_index()
fig3 = px.bar(region_sales, x='Region', y='Revenue',
              title='Total Revenue by Region',
              color='Revenue',
              color_continuous_scale='viridis')
fig3.update_traces(texttemplate='$%{y:,.0f}', textposition='outside')
fig3.update_layout(showlegend=False)
st.plotly_chart(fig3, use_container_width=True)

# 4. Bonus: Interactive Category-Region Heatmap
st.subheader("🔥 Category-Region Performance Heatmap")
heatmap_data = df.groupby(['Category', 'Region'])['Revenue'].sum().reset_index()
pivot_data = heatmap_data.pivot(index='Category', columns='Region', values='Revenue')
fig4 = px.imshow(pivot_data, 
                 title='Revenue Heatmap: Category vs Region',
                 aspect='auto',
                 color_continuous_scale='Blues')
st.plotly_chart(fig4, use_container_width=True)
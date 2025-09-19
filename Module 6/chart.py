import streamlit as st
import pandas as pd

st.title("Fitness Progress Dashboard")

# Sample fitness data
fitness_data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', '2024-01-07'],
    'Steps': [8500, 9200, 7800, 10500, 9800, 8900, 11200],
    'Calories': [2200, 2400, 2100, 2600, 2500, 2300, 2700],
    'Workouts': [1, 2, 0, 2, 1, 1, 2],
    'Sleep': [7.5, 8.0, 6.5, 7.8, 8.2, 7.0, 8.5]
}

df = pd.DataFrame(fitness_data)

# Steps trend line chart
st.subheader("Daily Steps Trend")
st.line_chart(df.set_index('Date')['Steps'])

# Calories area chart
st.subheader("Calorie Burn Over Time") 
st.area_chart(df.set_index('Date')['Calories'])

# Workouts bar chart
st.subheader("Weekly Workout Sessions")
st.bar_chart(df.set_index('Date')['Workouts'])

# Sleep vs Calories scatter plot
st.subheader("Sleep vs Calories Relationship")
scatter_data = df[['Sleep', 'Calories']].rename(columns={'Sleep': 'x', 'Calories': 'y'})
st.scatter_chart(scatter_data)

#Summary
st.subheader("Week Summary")

st.metric("Avg Steps", f"{df['Steps'].mean():.0f}")

st.metric("Avg Calories", f"{df['Calories'].mean():.0f}")

st.metric("Total Workouts", df['Workouts'].sum())

st.metric("Avg Sleep", f"{df['Sleep'].mean():.1f}h")
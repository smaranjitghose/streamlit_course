import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Exam Performance Analyzer")
st.write("Upload your grades CSV to analyze student performance patterns")

# Sample data for demonstration
sample_data = {
    'Student': ['Alice', 'Bob', 'Carol', 'David', 'Eve', 'Frank', 'Grace', 'Henry'] * 3,
    'Subject': ['Math', 'Math', 'Math', 'Math', 'Math', 'Math', 'Math', 'Math',
                'Science', 'Science', 'Science', 'Science', 'Science', 'Science', 'Science', 'Science',
                'English', 'English', 'English', 'English', 'English', 'English', 'English', 'English'],
    'Score': [85, 72, 91, 68, 94, 79, 83, 77, 
              88, 75, 89, 71, 92, 81, 86, 74,
              82, 78, 87, 73, 89, 84, 80, 76],
    'Exam_Date': ['2024-01-15'] * 8 + ['2024-02-15'] * 8 + ['2024-03-15'] * 8
}

df = pd.DataFrame(sample_data)
st.write("Sample Data Preview:")
st.dataframe(df.head())

# 1. Grade Distribution Histogram
st.subheader("📈 Overall Grade Distribution")
fig1, ax1 = plt.subplots(figsize=(8, 5))
ax1.hist(df['Score'], bins=10, color='skyblue', alpha=0.7, edgecolor='black')
ax1.set_xlabel('Score')
ax1.set_ylabel('Number of Students')
ax1.set_title('Distribution of Exam Scores')
ax1.grid(True, alpha=0.3)
st.pyplot(fig1)

# 2. Subject-wise Performance Boxplots
st.subheader("📦 Subject-wise Performance Spread")
fig2, ax2 = plt.subplots(figsize=(8, 5))
subjects = df['Subject'].unique()
subject_scores = [df[df['Subject'] == subject]['Score'].values for subject in subjects]
ax2.boxplot(subject_scores, tick_labels=subjects)
ax2.set_ylabel('Score')
ax2.set_title('Score Distribution by Subject')
ax2.grid(True, alpha=0.3)
st.pyplot(fig2)

# 3. Average Scores Over Time
st.subheader("📊 Average Performance Trends")
avg_by_date = df.groupby('Exam_Date')['Score'].mean()
fig3, ax3 = plt.subplots(figsize=(8, 5))
ax3.plot(avg_by_date.index, avg_by_date.values, marker='o', linewidth=2, markersize=8, color='green')
ax3.set_xlabel('Exam Date')
ax3.set_ylabel('Average Score')
ax3.set_title('Class Average Performance Over Time')
ax3.grid(True, alpha=0.3)
plt.xticks(rotation=45)
st.pyplot(fig3)
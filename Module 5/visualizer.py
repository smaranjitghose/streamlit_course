import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Student Marks Visualizer", layout="centered")
st.title("📊 Student Marks Visualizer")

# Generate mock marks for multiple subjects
np.random.seed(42)
subjects = {
    "Math": np.random.normal(75, 12, 100),
    "Science": np.random.normal(70, 15, 100),
    "English": np.random.normal(65, 10, 100),
    "History": np.random.normal(68, 8, 100)
}
df = pd.DataFrame(subjects)

# Sidebar input
st.sidebar.header("⚙️ Settings")
subject_choice = st.sidebar.selectbox("Choose a subject:", df.columns)
bins = st.sidebar.slider("Number of bins:", 5, 20, 10)

# Plot
st.subheader(f"Distribution of Marks in {subject_choice}")
fig, ax = plt.subplots()
sns.histplot(df[subject_choice], bins=bins, kde=True, color="skyblue", ax=ax)
ax.set_xlabel("Marks")
ax.set_ylabel("Number of Students")
ax.set_title(f"{subject_choice} Marks Distribution")

st.pyplot(fig)

# Extra insight
st.subheader("📋 Summary Statistics")
st.write(df[subject_choice].describe().round(2))

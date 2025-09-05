import streamlit as st
import pandas as pd

st.title("Student Gradebook Viewer 📘")

# Mock dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Grade": [85, 92, 78, 88, 95]
}

df = pd.DataFrame(data)

# Display the table
st.subheader("Gradebook")
st.dataframe(df)

# Show average grade
average_grade = df["Grade"].mean()
st.metric("Class Average", f"{average_grade:.2f}")
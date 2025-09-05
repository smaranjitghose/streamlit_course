import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Student Marks Visualizer 📊")

# Generate mock marks
marks = np.random.normal(70, 10, 100)
df = pd.DataFrame({"Marks": marks})

st.subheader("Distribution of Marks")

# Plot histogram with KDE
fig, ax = plt.subplots()
sns.histplot(df["Marks"], bins=10, kde=True, ax=ax)
ax.set_xlabel("Marks")
ax.set_ylabel("Number of Students")
ax.set_title("Student Marks Distribution")

st.pyplot(fig)

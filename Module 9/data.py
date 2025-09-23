import streamlit as st
import pandas as pd
import time

# Cleaning function

def clean_step(data, step, progress, i, total):
    time.sleep(1)
    if step == "Remove duplicates":
        cleaned = data.drop_duplicates()
        status = f"Removed {len(data) - len(cleaned)} duplicates"
    elif step == "Handle missing":
        cleaned = data.fillna("N/A")
        status = "Filled missing values"
    elif step == "Standardize text":
        cleaned = data.copy()
        for col in cleaned.select_dtypes('object'):
            cleaned[col] = cleaned[col].astype(str).str.strip().str.title()
        status = f"Standardized text in {len(cleaned.select_dtypes('object').columns)} columns"
    else:
        cleaned = data
        status = "Step complete"
    progress.progress((i + 1)/total)
    return cleaned, status

# --- Streamlit UI ---
st.title("✨ Quick Data Cleaner")
uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.success(f"Loaded {len(data)} rows, {len(data.columns)} columns")
    st.dataframe(data.head())

    if st.button("Start Cleaning"):
        steps = ["Remove duplicates", "Handle missing", "Standardize text"]
        progress = st.progress(0)
        status_text = st.empty()
        cleaned = data.copy()

        for i, step in enumerate(steps):
            status_text.text(f"Step {i+1}/{len(steps)}: {step}...")
            cleaned, step_status = clean_step(cleaned, step, progress, i, len(steps))
            status_text.text(f"✅ {step_status}")

        st.success("🎉 Cleaning complete!")
        st.subheader("Cleaned Data")
        st.dataframe(cleaned.head())
import streamlit as st
import PyPDF2

st.title("📄 Resume Reviewer")

uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])

if uploaded_file is not None:
    st.write("---")
    st.subheader("First few lines of your resume:")

    if uploaded_file.type == "text/plain":
        # Handle TXT files
        file_contents = uploaded_file.read().decode("utf-8")
        first_few_lines = "\n".join(file_contents.splitlines()[:5])
        st.text(first_few_lines)

    elif uploaded_file.type == "application/pdf":
        # Handle PDF files
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages[:1]:  # Read first page only
            text += page.extract_text() or ""
        first_few_lines = "\n".join(text.splitlines()[:5])
        st.text(first_few_lines)
import streamlit as st
import PyPDF2
import io

st.title("📄 PDF Quick Preview")

# PDF file upload
uploaded_pdf = st.file_uploader("Upload a PDF document", type="pdf")

if uploaded_pdf is not None:
    # Read PDF with PyPDF2
    pdf_reader = PyPDF2.PdfReader(uploaded_pdf)
    num_pages = len(pdf_reader.pages)

    # Show metadata
    st.subheader("Document Information")
    st.write(f"Filename: {uploaded_pdf.name}")
    st.write(f"Number of pages: {num_pages}")

    # Page selection input
    page_number = st.number_input(
        "Enter page number to preview",
        min_value=1,
        max_value=num_pages,
        value=1,
        step=1
    )

    # Extract selected page text
    selected_page = pdf_reader.pages[page_number - 1]
    text_content = selected_page.extract_text() or "⚠️ No text found on this page."

    st.subheader(f"Page {page_number} Preview")
    preview_text = text_content[:500] + "..." if len(text_content) > 500 else text_content
    st.text_area("Text Preview", preview_text, height=200)

    # Option to download just the selected page
    pdf_writer = PyPDF2.PdfWriter()
    pdf_writer.add_page(selected_page)

    pdf_bytes = io.BytesIO()
    pdf_writer.write(pdf_bytes)
    pdf_bytes.seek(0)

    st.download_button(
        f"Download Page {page_number}",
        data=pdf_bytes,
        file_name=f"{uploaded_pdf.name.replace('.pdf','')}_page_{page_number}.pdf",
        mime="application/pdf"
    )

else:
    st.info("Upload a PDF file to preview its content")

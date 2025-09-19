import streamlit as st
from rembg import remove
from PIL import Image
import io

st.title("🖼️ Background Remover")

# Image upload
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Load and display original image
    original_image = Image.open(uploaded_file)
    
    st.subheader("Original Image")
    st.image(original_image, width=300)
    
    # Process image to remove background
    with st.spinner("Removing background..."):
        # Convert to bytes for rembg processing
        img_bytes = uploaded_file.getvalue()
        processed_bytes = remove(img_bytes)
        processed_image = Image.open(io.BytesIO(processed_bytes))
    
    st.subheader("Processed Image")
    st.image(processed_image, width=300)
    
    # Download processed image
    buf = io.BytesIO()
    processed_image.save(buf, format="PNG")
    
    st.download_button(
        "Download Processed Image",
        data=buf.getvalue(),
        file_name="background_removed.png",
        mime="image/png"
    )
else:
    st.info("Upload an image to remove its background")
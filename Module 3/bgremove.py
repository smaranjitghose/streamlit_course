import streamlit as st
from rembg import remove
from PIL import Image
import io

st.title("🖼️ Background Remover App")

st.write("Upload an image and remove its background instantly.")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Open uploaded image
    input_image = Image.open(uploaded_file)

    st.subheader("Original Image")
    st.image(input_image, use_container_width=True)

    # Remove background
    with st.spinner("Removing background..."):
        output_image = remove(input_image)

    st.subheader("Image without Background")
    st.image(output_image, use_container_width=True)

    # Download button
    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="Download Image without Background",
        data=byte_im,
        file_name="no_bg.png",
        mime="image/png"
    )

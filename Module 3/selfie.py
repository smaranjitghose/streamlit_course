import streamlit as st

st.title("📸 Selfie Booth")

st.write("Take a selfie and add a fun caption!")

picture = st.camera_input("Say cheese!") 
if picture:
    st.image(picture, caption="Your Selfie", use_column_width=True)
    
    caption = st.text_input("Add a caption to your selfie:")
    if caption:
        st.success(f"Saved selfie with caption: '{caption}'")
        st.write("Thanks for sharing your selfie!")
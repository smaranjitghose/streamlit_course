import streamlit as st
import io

st.title("🎙️ Voice Memo Player")

# Audio file upload
uploaded_audio = st.file_uploader("Upload your voice memo", type=["wav", "mp3", "m4a"])

if uploaded_audio is not None:
    # Display audio player
    st.subheader("Your Voice Memo")
    st.audio(uploaded_audio)
    
    # Show file details
    st.write(f"File name: {uploaded_audio.name}")
    st.write(f"File size: {len(uploaded_audio.getvalue())} bytes")
    
    
    # Additional processing info
    st.info("Audio uploaded successfully! You can play it using the controls above.")
    
else:
    st.info("Upload an audio file to play your voice memo")
    st.write("Supported formats: WAV, MP3, M4A")
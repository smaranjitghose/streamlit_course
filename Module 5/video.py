import streamlit as st

st.title("🎬 Video Trailer App")

# Video file upload
uploaded_video = st.file_uploader("Upload your video trailer", type=["mp4", "mov", "avi"])

if uploaded_video is not None:
    # Display video player
    st.subheader("Video Player")
    st.video(uploaded_video)
    
    # Show file details
    st.subheader("Video Details")
    st.write(f"File name: {uploaded_video.name}")
    st.write(f"File size: {len(uploaded_video.getvalue())} bytes")
    
    
    st.success("Video uploaded successfully! Use the player controls to watch your trailer.")
    
else:
    st.info("Upload a video file to start watching")
    st.write("Supported formats: MP4, MOV, AVI")
import streamlit as st

st.title("Comment Box")

# Main comment input
comment = st.text_area("Leave a comment:", placeholder="What's on your mind?")

# Popover for additional settings
with st.popover("⚙️ Settings"):
    visibility = st.selectbox("Who can see this?", ["Everyone", "Friends Only", "Private"])
    mood = st.selectbox("Your mood:", ["😊 Happy", "😐 Neutral", "😢 Sad", "😍 Excited", "🤔 Thoughtful"])

# Submit and display
if st.button("Post Comment"):
    if comment:
        st.success("Comment posted!")
        
        # Display the comment with settings
        st.markdown("---")
        st.subheader("Your Comment")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"💬 {comment}")
        with col2:
            st.write(f"Visibility: {visibility}")
            st.write(f"Mood: {mood}")
    else:
        st.error("Please write a comment first!")
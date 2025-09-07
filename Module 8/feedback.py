import streamlit as st

st.set_page_config(page_title="Feedback Collector", page_icon="📝")

st.title("✨ We Value Your Feedback! ✨")
st.write("Help us improve by sharing your thoughts 💡")

with st.form("feedback_form", clear_on_submit=True):
    st.markdown("#### 👤 About You")
    name = st.text_input("Your Name", placeholder="e.g., Alex")

    st.markdown("#### ⭐ Your Experience")
    rating = st.slider("How would you rate your experience?", 1, 5, 3)

    st.markdown("#### 💬 Comments")
    comments = st.text_area("Share your feedback", placeholder="What went well? What can we do better?")

    submitted = st.form_submit_button("🚀 Send Feedback")

if submitted:
    st.success(f"🎉 Thanks **{name or 'Guest'}**")

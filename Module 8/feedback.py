import streamlit as st

st.title("📝 Feedback Collector")

with st.form("feedback_form"):
    name = st.text_input("Your Name")
    rating = st.slider("Rate your experience", 1, 5, 3)
    comments = st.text_area("Additional Comments")
    submitted = st.form_submit_button("Submit")

if submitted:
    st.success(f"Thanks {name}! You rated us {rating}/5.")
    if comments:
        st.write("Your comments:", comments)

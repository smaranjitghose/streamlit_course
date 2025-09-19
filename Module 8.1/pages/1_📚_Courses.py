import streamlit as st

st.title("📚 Our Courses")

st.subheader("Undergraduate Programs")

courses = ["Computer Science", "Software Engineering", "Data Science", "Cybersecurity"]

for course in courses:
    st.write(f"🎯 **{course}** - 4 years, 120 credits")

st.subheader("Graduate Programs")
st.write("🎓 Master of Computer Science - 2 years")
st.write("🎓 PhD in AI - 4 years")

st.info("Need more info? Contact our admissions office!")
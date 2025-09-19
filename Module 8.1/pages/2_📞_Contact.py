import streamlit as st

st.title("📞 Contact Us")

# Contact form
name = st.text_input("Your Name")
email = st.text_input("Email")
message = st.text_area("Message")

if st.button("Send Message"):
    if name and email and message:
        st.success("Message sent! We'll reply within 24 hours.")
    else:
        st.error("Please fill in all fields.")

st.write("---")
st.write("**Campus Address:** 123 University Drive, Tech City")
st.write("**Phone:** (555) 123-TECHU")
st.write("**Email:** info@techu.edu")

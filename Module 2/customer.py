import streamlit as st

# Page config
st.set_page_config(page_title="Customer Support Panel", layout="wide")

st.title("💬 Customer Support Panel")

st.write("Welcome! Submit your issue below and track support status.")

# User issue form
with st.form("support_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Email")
    issue = st.text_area("Describe your issue")
    submitted = st.form_submit_button("Submit Ticket")

if submitted:
    if not name or not email or not issue:
        st.error("⚠️ Please fill out all fields before submitting.")
    else:
        st.success(f"✅ Ticket submitted successfully! A support agent will contact {email}.")
        st.info("📌 Your Ticket ID: #12345")

st.subheader("📂 Support History")
st.chat_message("user").write("I am facing login issues.")
st.chat_message("assistant").write("Thanks for reporting. We are checking it.")
st.chat_message("user").write("Any update?")
st.chat_message("assistant").write("✅ Issue fixed. Please try again.")

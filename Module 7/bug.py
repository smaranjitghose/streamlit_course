import streamlit as st

st.title("My Awesome App")
st.write("Welcome to the app! Click around and explore.")
st.write("If you find any bugs, please report them using the button below.")

# Bug report modal
@st.dialog("Bug Report")
def bug_report_form():
    st.write("Help us improve by reporting any issues you've found:")
    
    # Form fields
    title = st.text_input("Bug Title", placeholder="Brief description of the issue")
    severity = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
    description = st.text_area("Description", placeholder="What happened? What did you expect?")
    email = st.text_input("Your Email (optional)", placeholder="your@email.com")
    
    # Submit button
    if st.button("Submit Report", type="primary"):
        if title and description:
            st.success("Bug report submitted successfully!")
            st.write("**Your Report:**")
            st.write(f"**Title:** {title}")
            st.write(f"**Severity:** {severity}")
            st.write(f"**Description:** {description}")
            st.write(f"**Contact:** {email if email else 'Anonymous'}")
        else:
            st.error("Please fill in title and description")

# Button to open modal
if st.button("🐛 Report a Bug"):
    bug_report_form()
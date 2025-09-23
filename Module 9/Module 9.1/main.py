import streamlit as st

st.title("Login Page")

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# Show login form if not logged in
if not st.session_state.logged_in:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Simple authentication rule
        if username and password == "demo":
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Welcome, {username}!")
            st.switch_page("pages/1_Dashboard.py")
        else:
            st.error("Invalid credentials. Hint: password is 'demo'")

# If already logged in
else:
    st.success(f"Already logged in as: {st.session_state.username}")
    if st.button("Go to Dashboard"):
        st.switch_page("pages/1_Dashboard.py")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

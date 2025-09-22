import streamlit as st

st.title("🌴 Leave Request")

st.write("**Your Balance:** 15 days available")

start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

if st.button("Submit Request"):
    st.success("Request submitted!")

st.page_link("Employee_Portal.py", label="← Back to Portal")
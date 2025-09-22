import streamlit as st

st.title("🛒 Checkout")

st.write("**Order Summary:**")
st.write("• Selected item: Laptop")
st.write("• Price: $999")
st.write("• Tax: $99")
st.write("• **Total: $1,098**")

name = st.text_input("Full Name")
email = st.text_input("Email")

if st.button("Complete Purchase"):
    if name and email:
        st.switch_page("pages/success.py")
    else:
        st.error("Please fill in all fields")
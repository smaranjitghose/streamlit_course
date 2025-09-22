import streamlit as st

st.title("🎉 Order Complete!")

st.success("Thank you for your purchase!")
st.write("Your order has been confirmed and will ship within 2 business days.")
st.write("**Order #12345**")

if st.button("Continue Shopping"):
    st.switch_page("pages/dashboard.py")

if st.button("Logout"):
    st.switch_page("E-commerce_App.py")
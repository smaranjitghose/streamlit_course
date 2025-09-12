import streamlit as st

st.title("Widget Demo: Button")

if st.button("Say Hello"):
    st.write("Hello!")
else:
    st.write("Click the button to greet.")

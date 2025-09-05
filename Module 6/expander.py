import streamlit as st

st.title("FAQ Section ❓") 
with st.expander("What is Streamlit?"):
    st.write("Streamlit is an open-source Python library for building web apps.")

with st.expander("Is Streamlit free?"):
    st.write("Yes, Streamlit is free and open-source.") 
    
with st.expander("How do I install Streamlit?"):
    st.code("pip install streamlit", language="bash")
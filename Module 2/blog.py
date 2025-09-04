import streamlit as st

st.set_page_config(page_title="My Blog Post", layout ='wide')

st.title("Building My First Streamlit Blog Page")
st.markdown("**Author:** John Doe | 📅 August 16, 2025")

st.markdown("---")

st.header("Introduction")
st.markdown("""
Welcome to my first blog post built with **Streamlit**!  
In this post, I’ll walk you through how I created a simple blog page using 
Streamlit’s `st.markdown()` feature.
""")

st.header("Why Streamlit for Blogging?")
st.markdown("""
- 🖥️ Easy to set up, no heavy frameworks  
- 🎨 Supports Markdown for clean formatting  
- 📊 Can embed charts, dataframes, and even interactive apps  
- ☁️ Easy deployment using Streamlit Cloud  
""")

st.header("Code Example")
st.code("""
import streamlit as st

st.title("My Blog Page")
st.markdown("Hello, this is my blog written in **Markdown**")
""", language="python")

st.header("Conclusion")
st.markdown("""
With just a few lines of code, you can turn Streamlit into a **lightweight blogging platform**.  
Next, I’ll explore how to add multiple posts and a navigation sidebar. 🚀
""")

st.markdown("---")
st.info("💡 Tip: You can use `st.image()` and `st.video()` to make posts more engaging.")

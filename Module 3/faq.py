import streamlit as st

st.title("Simple FAQ Bot 💬")

faq = {
    "What is Streamlit?": "Streamlit is an open-source Python library for building web apps.",
    "How do I install Streamlit?": "Run `pip install streamlit` in your terminal.",
    "How do I run a Streamlit app?": "Use `streamlit run your_app.py`.",
    "Who created Streamlit?": "Streamlit was created by Adrien Treuille, Thiago Teixeira, and Amanda Kelly."
}

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm your FAQ bot. Ask me something about Streamlit."}
    ]

for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

user_input = st.chat_input("Ask a question...")

if user_input:
    
    st.session_state.messages.append({"role": "user", "content": user_input})

    
    answer = faq.get(user_input, "Sorry, I don’t know that one yet. Try another question!")
    st.session_state.messages.append({"role": "assistant", "content": answer})

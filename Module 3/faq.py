import streamlit as st

st.title("Simple FAQ Bot 💬")

faq = {
    "what is streamlit": "Streamlit is an open-source Python library for building web apps.",
    "how do i install streamlit": "Run `pip install streamlit` in your terminal.",
    "how do i run a streamlit app": "Use `streamlit run your_app.py`.",
    "who created streamlit": "Streamlit was created by Adrien Treuille, Thiago Teixeira, and Amanda Kelly."
}

# Initial assistant message
st.chat_message("assistant").write("Hi! I'm your FAQ bot. Ask me something about Streamlit.")

# Get user input
user_input = st.chat_input("Ask a question...")

if user_input:
    # Display user message
    st.chat_message("user").write(user_input)

    # Normalize input (lowercase, strip spaces)
    normalized = user_input.lower().strip()

    # Try to find a match (exact or partial)
    answer = None
    for question, response in faq.items():
        if question in normalized:  # partial match
            answer = response
            break

    if not answer:
        answer = "Sorry, I don’t know that one yet. Try another question!"

    # Display assistant answer
    st.chat_message("assistant").write(answer)

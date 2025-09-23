import streamlit as st
import pandas as pd
from difflib import get_close_matches

st.title("Customer Service FAQ Bot")

# Load FAQ data
@st.cache_data
def load_faq():
    return pd.read_csv("faq_data.csv")

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

faq_df = load_faq()

def find_answer(question):
    questions = faq_df['Question'].tolist()
    match = get_close_matches(question.lower(), [q.lower() for q in questions], n=1, cutoff=0.4)
    if match:
        orig_q = questions[[q.lower() for q in questions].index(match[0])]
        return faq_df.loc[faq_df['Question']==orig_q, 'Answer'].iloc[0], orig_q
    return None, None

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
if prompt := st.chat_input("Ask me anything about our services..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    answer, matched_q = find_answer(prompt)
    if answer:
        bot_msg = f"**Answer:** {answer}"
        
    else:
        topics = ["Order Tracking", "Returns", "Shipping", "Payment", "Account"]
        bot_msg = "I don't have a specific answer. Try these topics:\n" + "\n".join(f"• {t}" for t in topics)
    
    st.session_state.messages.append({"role": "assistant", "content": bot_msg})
    with st.chat_message("assistant"):
        st.write(bot_msg)

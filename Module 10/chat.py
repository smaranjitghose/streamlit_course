import streamlit as st
from difflib import get_close_matches

st.title("💬 Customer Service Bot")

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Available commands and their aliases
commands = {
    'cancel': ['cancel', 'stop', 'abort'],
    'postpone': ['postpone', 'delay', 'postpne'],
    'reschedule': ['reschedule', 'change', 'move'],
    'status': ['status', 'check', 'track'],
    'refund': ['refund', 'money', 'return'],
    'help': ['help', 'commands', 'options']
}

def find_command(user_input):
    user_input = user_input.lower().strip()
    
    # Check exact matches first
    for cmd, aliases in commands.items():
        if user_input in aliases:
            return cmd
    
    # Check fuzzy matches
    all_aliases = [alias for aliases in commands.values() for alias in aliases]
    matches = get_close_matches(user_input, all_aliases, n=1, cutoff=0.6)
    
    if matches:
        for cmd, aliases in commands.items():
            if matches[0] in aliases:
                return cmd
    
    return None

def get_bot_response(command):
    responses = {
        'cancel': "I can help you cancel your order. Please provide your order number.",
        'postpone': "I'll help you postpone your delivery. When would you like it delivered?",
        'reschedule': "Let me help you reschedule. What's your preferred new date?",
        'status': "I'll check your order status. Please share your order number.",
        'refund': "I can process your refund request. Please provide your order details.",
        'help': "Available commands: cancel, postpone, reschedule, status, refund, help"
    }
    
    return responses.get(command, "I didn't understand that. Type 'help' for available commands.")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Process command and generate response
    command = find_command(prompt)
    bot_response = get_bot_response(command)
    
    # Add bot response to history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    
    # Display bot response
    with st.chat_message("assistant"):
        st.write(bot_response)
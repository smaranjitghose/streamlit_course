import streamlit as st, re

st.title("💬 Customer Support Chat")

# Initialize session state
st.session_state.setdefault("messages", [])
st.session_state.setdefault("dialog_state", {"waiting_for": None, "intent": None})

def detect_intent(msg):
    msg = msg.lower()
    if any(x in msg for x in ["order", "status", "track"]): return "order_status"
    if any(x in msg for x in ["refund", "return", "money"]): return "refund_policy"
    if any(x in msg for x in ["shipping", "delivery", "time"]): return "shipping_info"
    return "general"

def valid_order_id(order_id): 
    return bool(re.match(r"^[A-Za-z0-9]{6,10}$", order_id))

def bot_reply(user_msg):
    state = st.session_state.dialog_state
    if state["waiting_for"] == "order_id":
        if valid_order_id(user_msg):
            st.session_state.dialog_state = {"waiting_for": None, "intent": None}
            return f"✅ Order {user_msg} found. Status: Shipped - Delivery tomorrow."
        return "❌ Invalid order ID. Please enter 6–10 alphanumeric characters."
    if state["waiting_for"] == "refund_reason":
        st.session_state.dialog_state = {"waiting_for": None, "intent": None}
        return f"Refund noted: {user_msg}. Our team will email you in 24h."

    intent = detect_intent(user_msg)
    if intent == "order_status":
        st.session_state.dialog_state = {"waiting_for": "order_id", "intent": intent}
        return "Please provide your Order ID to check status."
    if intent == "refund_policy":
        st.session_state.dialog_state = {"waiting_for": "refund_reason", "intent": intent}
        return "Why would you like to return your item?"
    if intent == "shipping_info":
        return "🚚 Standard: 3–5 days | Express: 1–2 days"
    return "I can help with order status, refunds, or shipping info. What would you like to know?"

# Display chat history
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.write(m["content"])

# Chat input
if prompt := st.chat_input("Ask me about your order..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.write(prompt)

    reply = bot_reply(prompt)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"): st.write(reply)



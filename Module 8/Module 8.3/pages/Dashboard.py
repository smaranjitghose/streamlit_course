import streamlit as st

st.title("🛒 Shopping Dashboard")
st.write("Welcome! Here are our featured products:")

products = [
    {"name": "Laptop", "price": "$999"},
    {"name": "Headphones", "price": "$199"},
    {"name": "Mouse", "price": "$49"}
]

for product in products:
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.write(f"**{product['name']}**")
    with col2:
        st.write(product['price'])
    with col3:
        if st.button(f"Buy", key=product['name']):
            st.switch_page("pages/checkout.py")
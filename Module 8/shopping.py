import streamlit as st

st.title("🛒 Shopping Cart App")

# Initialize cart in session state
if "cart" not in st.session_state:
    st.session_state.cart = []

# Add items
item = st.text_input("Enter an item to add to cart")
if st.button("Add to Cart"):
    if item:
        st.session_state.cart.append(item)
        st.success(f"{item} added to cart!")

# Show cart
st.subheader("Your Cart")
for i, product in enumerate(st.session_state.cart, start=1):
    st.write(f"{i}. {product}")

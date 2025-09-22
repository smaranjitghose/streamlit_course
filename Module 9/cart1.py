import streamlit as st

st.title("🛍️ Online Store")

# Initialize session state for cart
if 'cart' not in st.session_state:
    st.session_state.cart = []

# Available products
products = {
    "Laptop": 25000,
    "Mouse": 349,
    "Keyboard": 499,
    "Monitor": 7999,
    "Headphones": 799
}

# Product selection form
with st.form("add_product_form"):
    st.subheader("Add Product to Cart")
    selected_product = st.selectbox("Choose a product:", list(products.keys()))
    quantity = st.number_input("Quantity:", min_value=1, max_value=10, value=1)
    
    if st.form_submit_button("Add to Cart"):
        item = {
            "name": selected_product,
            "price": products[selected_product],
            "quantity": quantity,
            "total": products[selected_product] * quantity
        }
        st.session_state.cart.append(item)
        st.success(f"Added {quantity}x {selected_product} to cart!")

# Display cart
st.subheader("Shopping Cart")
if st.session_state.cart:
    for i, item in enumerate(st.session_state.cart):
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
        with col1:
            st.write(f"{item['name']}")
        with col2:
            st.write(f"₹{item['price']}")
        with col3:
            st.write(f"Qty: {item['quantity']}")
        with col4:
            if st.button("Remove", key=f"remove_{i}"):
                st.session_state.cart.pop(i)
                st.rerun()
    
    # Cart total
    total_cost = sum(item['total'] for item in st.session_state.cart)
    st.subheader(f"Total: ₹{total_cost}")
    
    # Clear cart button
    if st.button("Clear Cart"):
        st.session_state.cart = []
        st.rerun()
else:
    st.write("Your cart is empty")
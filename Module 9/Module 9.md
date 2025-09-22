# Module 9: Managing State & Performance

### Topic 9.1: Session State (single page)

<br>

#### **Introduction**

Imagine filling out a long form online, getting halfway through, and then accidentally hitting a button that makes everything disappear—you'd have to start over from scratch. This frustrating experience happens in basic Streamlit apps because, by default, the entire script reruns with every user interaction, resetting all variables to their initial values. While this stateless behavior keeps apps simple and predictable, real-world applications often need to remember information across interactions—like maintaining user preferences, tracking accumulated calculations, or preserving data between different interface actions.
Streamlit's `st.session_state` solves this memory problem by providing persistent storage that survives script reruns, enabling stateful applications that can accumulate and maintain data over multiple user interactions. Session state works as a dictionary-like object where you can store any Python data type and access them throughout your application, creating sophisticated user experiences that handle complex workflows while maintaining consistency across interactions.

#### **Mini Project**

Jake is shopping online for his home office setup, carefully selecting a desk, chair, and accessories across multiple product pages, but every time he navigates back to browse more items, his cart empties and he has to start over. He's frustrated by losing his selections and having to remember what he already picked, especially when he wants to compare different combinations of items or remove something he's changed his mind about.
An online store with persistent cart functionality would let Jake build up his order gradually, make changes as he shops, and maintain his selections throughout his entire browsing session without losing progress.

##### **Project Setup**

Create a new file `app.py`:

```python
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

```

**Run your app with:**

```
streamlit run app.py

```

##### **Output**

<img src="">

<img src="">

---

#### **Step-by-Step Walkthrough**


-   **`st.session_state`:**
    
    -   A special Streamlit dictionary that **persists values across app reruns**.
        
    -   Normally, Streamlit reruns the entire script on any user interaction, which would reset normal variables.
        
    -   Using `st.session_state`, data like the shopping cart can **persist across interactions**.
        
    -   In this project, `st.session_state.cart` stores all cart items to prevent them from being lost when the app reruns.
        
-   **Initialize session state for cart:**
    
    -   Checks if `'cart'` exists in `st.session_state`.
        
    -   If not, creates an empty list: `st.session_state.cart = []`.
        
    -   Ensures the cart is ready for storing items on first load.
        
-   **App title and product list:**
    
    -   `st.title("🛍️ Online Store")` displays the title.
        
    -   Defines a dictionary `products` with available products and their prices.
        
-   **Product selection form (`st.form`):**
    
    -   Groups the product dropdown (`st.selectbox`) and quantity input (`st.number_input`).
        
    -   Prevents the app from rerunning until the user clicks **"Add to Cart"**.
        
    -   Provides smoother UX by allowing users to adjust inputs without triggering premature updates.
        
-   **Adding items to the cart:**
    
    -   When the form is submitted:
        
        -   Creates a dictionary with `name`, `price`, `quantity`, and `total`.
            
        -   Appends the dictionary to `st.session_state.cart`.
            
        -   Displays a `st.success()` message confirming the addition.
            
    -   This allows multiple items to accumulate in the cart while maintaining their details.
        
-   **Displaying the cart:**
    
    -   Iterates through `st.session_state.cart`.
        
    -   Uses `st.columns` to neatly display: product name, price, quantity, and a remove button.
        
    -   Each remove button has a unique `key` to prevent interface conflicts.
        
-   **Removing items from the cart:**
    
    -   Clicking a remove button pops the corresponding item from the cart.
        
    -   Calls `st.rerun()` to immediately refresh the display and reflect the removal.
        
-   **Calculating and displaying total cost:**
    
    -   Sums the `total` value of all items in the cart.
        
    -   Displays the result using `st.subheader()`.
        
-   **Clearing the entire cart:**
    
    -   Clicking **"Clear Cart"** empties `st.session_state.cart`.
        
    -   `st.rerun()` ensures the UI updates immediately to show an empty cart.
        
-   **Handling an empty cart:**
    
    -   If `st.session_state.cart` is empty, displays `"Your cart is empty"`.
        
    -   Keeps the interface informative when no items have been added yet.

#### **Conclusion**

State management patterns transform stateless web frameworks into platforms capable of building persistent applications that maintain user context across interactions. These techniques enable developers to create seamless user experiences for complex workflows, from multi-step processes to interactive data pipelines that accumulate information over time. Mastering state persistence opens the door to creating applications that remember user preferences, track progress, and provide continuity across sessions—essential capabilities for any serious web application.


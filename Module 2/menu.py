import streamlit as st  

# Page setup
st.set_page_config(page_title="🍽️ Bistro Café Menu", layout="centered")  

# Title
st.title("🍴 Welcome to Bistro Café")  
st.markdown("### 🌟 **Today’s Special Menu**")  
st.write("---")  

# Starters
st.header("🥗 Starters")  
st.markdown("""  
- **Bruschetta** 🥖  
  _Toasted bread topped with fresh tomatoes, garlic & basil_ — ₹180  

- **Caesar Salad** 🥬  
  _Crisp romaine lettuce, parmesan, and croutons_ — ₹220  
""")  

st.divider()  

# Main Course
st.header("🍝 Main Course")  
st.markdown("""  
- **Pasta Alfredo** 🍝  
  _Creamy white sauce with mushrooms & herbs_ — ₹350  

- **Grilled Chicken** 🍗  
  _Served with mashed potatoes and sautéed veggies_ — ₹420  
""")  

st.divider()  

# Desserts
st.header("🍰 Desserts")  
st.markdown("""  
- **Chocolate Lava Cake** 🍫  
  _Warm chocolate cake with gooey center_ — ₹180  

- **Cheesecake** 🍮  
  _Classic New York style, rich & smooth_ — ₹200  
""")  

st.divider()  

# Beverages
st.header("🥂 Beverages")  
st.markdown("""  
- **Cold Coffee** ☕ — ₹120  
- **Fresh Lime Soda** 🥤 — ₹100  
- **Iced Tea** 🍹 — ₹130  
""")  
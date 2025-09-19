import streamlit as st

# Project title
st.title("🍩 Sip & Smile: Craft Your Drink")

# Coffee selection widgets
coffee_type = st.radio(
    "Choose your coffee type:",
    ["Espresso", "Latte", "Cappuccino"]
)

coffee_size = st.selectbox(
    "Select coffee size:",
    ["Small", "Medium", "Large"]
)

sugar = st.slider(
    "Sugar level (teaspoons):",
    min_value=0, max_value=5, step=1
)

whipped_cream = st.checkbox("Add whipped cream topping")

# Display order summary
st.subheader("📝 Your Coffee Order:")
order_summary = f"- {coffee_size} {coffee_type}\n- Sugar: {sugar} tsp"

# Add whipped cream only if selected
if whipped_cream:
    order_summary += "\n- With whipped cream 🍦"

st.write(order_summary)

import streamlit as st
st.title("☕ Coffee Order App")

# Coffee type selection
coffee_type = st.radio(
    "Choose your coffee type:",
    ["Espresso", "Latte", "Cappuccino"]
)

# Coffee size selection
coffee_size = st.selectbox(
    "Select coffee size:",
    ["Small", "Medium", "Large"]
)

# Sugar level
sugar = st.slider(
    "Select sugar level (teaspoons):",
    min_value=0, max_value=5, step=1
)

# Extra topping
whipped_cream = st.checkbox("Add whipped cream topping")

# order summary
st.subheader("📝 Your Coffee Order Summary:")
order_summary = f"- {coffee_size} {coffee_type}\n- Sugar: {sugar} tsp"
if whipped_cream:
    order_summary += "\n- With whipped cream 🍦"
else:
    order_summary += "\n- No whipped cream"

st.write(order_summary)
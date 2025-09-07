import streamlit as st

st.title("🍽️ Indian Dishes Recipes")

# Two Indian dishes with images and steps
recipes = {
    "Butter Chicken": {
        "steps": [
            "Marinate chicken in yogurt and spices",
            "Cook chicken in a pan until browned",
            "Prepare tomato and butter gravy",
            "Add chicken to gravy and simmer",
            "Serve hot with naan or rice"
        ]
    },
    "Paneer Tikka": {
        "steps": [
            "Cube paneer and marinate with yogurt and spices",
            "Skewer paneer with veggies",
            "Grill or bake until slightly charred",
            "Serve with mint chutney"
        ]
    }
}

# Dropdown to select dish
choice = st.selectbox("Select a dish:", list(recipes.keys()))

# Display selected dish
dish = recipes[choice]
st.header(choice)
st.subheader("Recipe Steps:")
for step in dish["steps"]:
    st.write(f"- {step}")

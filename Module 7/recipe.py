import streamlit as st

# Session state to remember which recipe is active
if "page" not in st.session_state:
    st.session_state.page = 0

recipes = [
    {"title": "🍝 Spaghetti Carbonara", "steps": ["Boil pasta", "Fry pancetta", "Mix with eggs & cheese"]},
    {"title": "🥗 Greek Salad", "steps": ["Chop veggies", "Add feta cheese", "Drizzle olive oil"]},
    {"title": "🍪 Chocolate Chip Cookies", "steps": ["Mix dough", "Add chocolate chips", "Bake until golden"]}
]

# Display current recipe
recipe = recipes[st.session_state.page]
st.title(recipe["title"])
for step in recipe["steps"]:
    st.write(f"- {step}")

# Navigation buttons
col1, col2 = st.columns(2)
if col1.button("Previous") and st.session_state.page > 0:
    st.session_state.page -= 1
if col2.button("Next") and st.session_state.page < len(recipes) - 1:
    st.session_state.page += 1
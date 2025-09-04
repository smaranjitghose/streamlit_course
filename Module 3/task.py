import streamlit as st

st.set_page_config(page_title="Basic Task App")

st.title("Basic Task Toggle App")

# Input for new task
tasks =  ["Learn Streamlit", "Build an app", "Deploy to Cloud"] 
completed = []

new_task = st.text_input("Enter a new task")
if st.button("Add Task ➕"):
    tasks.append(new_task)

st.markdown("------")

# Show tasks
st.subheader("Your Tasks 📝")
for t in tasks:
    if st.checkbox(t, key=t):
        completed.append(t)

st.markdown("------")

st.subheader("Completed Tasks 📌")
for c in completed:
    st.write(f"✅ {c}")

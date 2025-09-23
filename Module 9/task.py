import streamlit as st

# Initialize session state for tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = []
if 'task_input' not in st.session_state:
    st.session_state.task_input = ""

# Task functions 
def add_task():
    if st.session_state.task_input.strip():
        st.session_state.tasks.append({
            'text': st.session_state.task_input,
            'done': False
        })
        st.session_state.task_input = ""

def toggle_task(index):
    st.session_state.tasks[index]['done'] = not st.session_state.tasks[index]['done']

def delete_task(index):
    st.session_state.tasks.pop(index)

# --- Page Title ---
st.title("⚡ QuickTasks ⚡")

# Add New Task Section 
st.subheader("➕ Add a New Task")
st.text_input("Enter your task here:", key="task_input", on_change=add_task)

# Task List Section
st.subheader("📋 Your Tasks")
if not st.session_state.tasks:
    st.info("No tasks yet. Add one above! ✨")

for i, task in enumerate(st.session_state.tasks):
    col1, col2, col3 = st.columns([3, 1, 1])
    
    with col1:
        style = "text-decoration: line-through; color: gray;" if task['done'] else ""
        st.markdown(f"<span style='{style}'>{task['text']}</span>", unsafe_allow_html=True)
    
    with col2:
        status = "✅ Done" if task['done'] else "✔️ Mark Done"
        st.button(status, key=f"toggle_{i}", on_click=toggle_task, args=(i,))
    
    with col3:
        st.button("🗑️ Delete", key=f"delete_{i}", on_click=delete_task, args=(i,))

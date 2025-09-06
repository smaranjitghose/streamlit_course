import streamlit as st

st.title("🔢 Counter Button App")
st.markdown('---')

if "count" not in st.session_state:
    st.session_state.count = 0

def increment():
    st.session_state.count += 1


st.button("Increase", on_click=increment)

st.markdown(f"<h1 style='text-align: center; font-size: 72px;'>{st.session_state.count}</h1>", unsafe_allow_html=True)


import streamlit as st 
import utils

utils.init_score()

st.title("📊 Quiz Results")
st.write(f"Your final score: {st.session_state.score}")
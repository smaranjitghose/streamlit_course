import streamlit as st 
import utils

utils.init_score()

st.title("Question 1")
answer = st.radio("What is 2 + 2?", [3, 4, 5]) 
if st.button("Submit"): 
    if answer == 4:
        utils.update_score(1)
        st.success("Correct!") 
    else:
        st.error("Oops, try again.")
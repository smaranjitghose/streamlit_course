import streamlit as st 
import utils

utils.init_score()

st.title("Question 2")
answer = st.radio("What is the capital of France?", ["Berlin", "Paris", "Rome"]) 
if st.button("Submit"): 
    if answer == "Paris":
        utils.update_score(1)
        st.success("Correct!") 
    else:
        st.error("Oops, try again.")
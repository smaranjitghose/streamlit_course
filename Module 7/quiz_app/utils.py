import streamlit as st 
def  init_score(): 
    if  "score"  not  in st.session_state:
        st.session_state.score = 0  
def  update_score(points):
    st.session_state.score += points
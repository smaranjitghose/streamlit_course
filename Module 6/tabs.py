import streamlit as st

st.title("Sports Stats Dashboard 🏅")

tab1, tab2, tab3 = st.tabs(["Football", "Basketball", "Cricket"]) 
with tab1:
    st.subheader("Football Stats")
    st.write("Top Scorer: Messi - 30 goals") 
with tab2:
    st.subheader("Basketball Stats")
    st.write("Top Scorer: LeBron James - 25 PPG") 
with tab3:
    st.subheader("Cricket Stats")
    st.write("Top Scorer: Virat Kohli - 1200 runs")
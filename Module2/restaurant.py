import streamlit as st

st.title("Welcome to Our Restaurant!")

col1,col2=st.columns(2)

with col1:
    st.header("Starters")
    st.write("Cheese Burger")
    st.write("Cheese Sandwich")
    st.write("Hot Dog")
    st.write("Chicken Sandwich")

    st.header("Main Course")
    st.write("Steak ")
    st.write("Pasta Carbonara")

    st.subheader("Desserts")
    st.write("Chocolate Cake")
    st.write("Ice Cream ")

with col2:
    st.header("")
    st.write("$34")
    st.write("$21")    
    st.write("$30")
    st.write("$34")

    st.header("")
    st.write("$40")
    st.write("$54")

    st.subheader("")
    st.write("$25")
    st.write("$20")
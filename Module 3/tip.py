import streamlit as st;

st.set_page_config(page_title='Tip Calculator App')

st.title('Tip Calculator')

bill_amount = st.number_input("Enter bill amount:", min_value=0.0)
tip_percentage = st.number_input("Enter tip percentage:", min_value=0, max_value=100, value=15)

tip_amount = bill_amount * (tip_percentage / 100)
total_amount = bill_amount + tip_amount

st.write("---")
st.write(f"Tip amount: ${tip_amount:.2f}")
st.write(f"Total amount: ${total_amount:.2f}")

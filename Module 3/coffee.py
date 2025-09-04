import streamlit as st;

st.set_page_config(page_title='Coffee Order App')

st.title('Coffee Order App ☕')

coffee_type = st.radio('Choose your favourite Coffee',('Latte', 'Cappuccino', 'Espresso'))

coffee_size = st.radio('Select Size',('Small', 'Medium', 'Large'))

prices=['$10','$15', '$20']
if st.button("Order Coffee"):
    if coffee_size=='Small':
        coffee_price='$10'
    elif coffee_size=='Medium':
        coffee_price='$15'
    else:
        coffee_price='$20'

    st.write("------")
    st.write(f'You ordered {coffee_type} in size {coffee_size.lower()}')
    st.info(f'Your bill is {coffee_price}')
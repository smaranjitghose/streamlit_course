import streamlit as st
import datetime

st.set_page_config(page_title='Birthday Countdown')

st.title('Birthday Countdown 🎊')

birth_date=st.date_input("Select your Birthday", value=datetime.date(2002,5,2), min_value=datetime.date(1990,1,1), max_value=datetime.date.today())

today = datetime.date.today() 

next_birthday = birth_date.replace(year=today.year)

if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

days_left=(next_birthday - today).days

st.write('-----')
st.write(f'🎂Days left until your birthday {days_left} days ')
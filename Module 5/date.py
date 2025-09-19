import streamlit as st
from datetime import date, datetime

st.title("🎂 Birthday Countdown")

# Date selection for birthday
birth_date = st.date_input("When is your birthday?")

# Calculate days until next birthday
today = date.today()
this_year_birthday = birth_date.replace(year=today.year)

# If birthday already passed this year, calculate for next year
if this_year_birthday < today:
    next_birthday = birth_date.replace(year=today.year + 1)
else:
    next_birthday = this_year_birthday

days_until = (next_birthday - today).days

# Display countdown
if days_until > 0:
    st.metric("Days Until Birthday", days_until)
    st.success(f"🎉 Only {days_until} days until your birthday!")
elif days_until == 0:
    st.balloons()
    st.success("🎊 Happy Birthday! Today is your special day!")
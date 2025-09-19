import streamlit as st

# App title
st.title("🌀 MoodSwitch")

st.write("Flip the vibe instantly — will it be balloons or snow?")

# Party Mode button
if st.button("🎈 Party Mode"):
    st.balloons()
    st.write("The mood is set: 🎉 It's party time with balloons!")

# Snow Mode button
if st.button("❄️ Snow Mode"):
    st.snow()
    st.write("The mood is set: ❄️ A magical winter wonderland begins!")

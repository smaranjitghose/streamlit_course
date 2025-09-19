import streamlit as st

st.title("🎨 Brand Palette Creator")

# Color selection
color1 = st.color_picker("Primary Color", "#FF6B6B")
color2 = st.color_picker("Secondary Color", "#4ECDC4") 
color3 = st.color_picker("Accent Color", "#45B7D1")

# Display color codes
st.subheader("Your Brand Colors")
st.write(f"Primary: {color1}")
st.write(f"Secondary: {color2}")
st.write(f"Accent: {color3}")
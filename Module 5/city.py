import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="Tourist Spot Explorer", layout="centered")
st.title("🕌 Explore Indian Tourist Spots")

# Dataset with 2 places
data = pd.DataFrame({
    "spot": ["Taj Mahal", "Golden Temple"],
    "city": ["Agra", "Amritsar"],
    "description": [
        "One of the Seven Wonders of the World, a symbol of love in Agra.",
        "The holiest gurdwara and a central religious place for Sikhs, in Amritsar."
    ],
    "lat": [27.1751, 31.6200],
    "lon": [78.0421, 74.8765],
    "image": [
        "https://upload.wikimedia.org/wikipedia/commons/d/da/Taj-Mahal.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/3/34/Golden_Temple_in_Amritsar_India.jpg"
    ]
})

# Dropdown to choose tourist spot
choice = st.selectbox("Select a tourist spot:", data["spot"])

# Filter data
selected = data[data["spot"] == choice].iloc[0]

# Show details
st.header(f"{selected['spot']} ({selected['city']})")
st.write(selected["description"])
st.image(selected["image"], use_container_width=True)

# Show map for selected place
st.subheader("📍 Location on Map")
layer = pdk.Layer(
    "ScatterplotLayer",
    pd.DataFrame([selected]),
    get_position=["lon", "lat"],
    get_color=[200, 30, 0, 160],
    get_radius=40000,
    pickable=True
)

view_state = pdk.ViewState(latitude=selected["lat"], longitude=selected["lon"], zoom=10)

st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"text": "{spot}, {city}"}
))

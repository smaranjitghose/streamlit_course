import streamlit as st
import pandas as pd
import pydeck as pdk

st.title("City Explorer 🗺️")

data = pd.DataFrame({
    "city": ["Paris", "New York", "Tokyo", "Sydney"],
    "lat": [48.8566, 40.7128, 35.6895, -33.8688],
    "lon": [2.3522, -74.0060, 139.6917, 151.2093]
})

st.subheader("Tourist Spots Map")

layer = pdk.Layer(
    "ScatterplotLayer",
    data,
    get_position=["lon", "lat"],
    get_color=[200, 30, 0, 160],
    get_radius=50000,
)

view_state = pdk.ViewState(latitude=20, longitude=0, zoom=1)

st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

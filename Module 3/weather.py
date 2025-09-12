import streamlit as st 

# Sample weather JSON-like data (in real apps, this comes from API responses)
weather_data = {
    "location": {"name": "Hyderabad", "region": "Telangana", "country": "India"},
    "current": {
        "temperature_c": 27,
        "humidity": 81,
        "condition": {"text": "Cloudy", "icon": "overcast"},
        "wind_kph": 8,
        "uv_index": 1,
    },
    "forecast": [
        {"date": "2025-09-12", "text": "Cloudy, a little rain", "max_temp_c": 30, "min_temp_c": 24},
        {"date": "2025-09-13", "text": "Cloudy, rain", "max_temp_c": 29, "min_temp_c": 23},
        {"date": "2025-09-14", "text": "Humid with a little rain", "max_temp_c": 31, "min_temp_c": 25},
    ],
}

st.title("🌤️ Weather Data Explorer")

# Location section
st.header("📍 Location")
loc = weather_data["location"]
st.write(f"{loc['name']}, {loc['region']}, {loc['country']}")

# Current conditions
st.header("🌡️ Current Conditions")
current = weather_data["current"]
st.metric("Temperature (°C)", current["temperature_c"])
st.metric("Humidity (%)", current["humidity"])
st.metric("UV Index", current["uv_index"])
st.write(f"Condition: {current['condition']['text']}")
st.write(f"Wind Speed: {current['wind_kph']} kph")

# Forecast
st.header("📅 Forecast")
for day in weather_data["forecast"]:
    st.write(f"**{day['date']}**: {day['text']} (Max: {day['max_temp_c']}°C, Min: {day['min_temp_c']}°C)")

st.divider()

# Raw JSON data
st.header("🗂️ Raw JSON Data")
st.json(weather_data)
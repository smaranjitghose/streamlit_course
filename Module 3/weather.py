import streamlit as st

# Sample weather data (simulates API response)
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
        {"date": "2025-09-12", "text": "Cloudy with light rain", "max_temp_c": 30, "min_temp_c": 24},
        {"date": "2025-09-13", "text": "Rainy", "max_temp_c": 29, "min_temp_c": 23},
    ],
}

st.title("🌤️ Weather Data Explorer")

# Display parsed summary
st.header("Current Weather")
current = weather_data["current"]
st.metric("Temperature", f"{current['temperature_c']}°C")
st.metric("Humidity", f"{current['humidity']}%")
st.write(f"Condition: {current['condition']['text']}")

# Display raw JSON
st.header("Raw API Data")
st.json(weather_data)
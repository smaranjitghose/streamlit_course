import streamlit as st
import requests

@st.cache_data
def fetch_universities(country):
    """Fetch universities from API and cache results"""
    url = f"http://universities.hipolabs.com/search?country={country}"
    response = requests.get(url)
    return response.json()

@st.cache_resource
def get_api_base_url():
    """Cache the API base configuration"""
    return "http://universities.hipolabs.com/search"

st.title("University Finder")
st.write("Search for universities by country (results are cached for faster loading)")

# Country selection
country = st.selectbox(
    "Select a country:",
    ["Canada", "United Kingdom", "Australia", "Germany"]
)

if country:
    # Show loading message
    with st.spinner(f"Searching universities in {country}..."):
        universities = fetch_universities(country)
    
    st.subheader(f"Universities in {country}")
    st.write(f"Found {len(universities)} universities")
    
    # Display first 10 universities
    for uni in universities[:10]:
        with st.expander(uni['name']):
            st.write(f"**Website:** {uni.get('web_pages', ['N/A'])[0]}")
            st.write(f"**Domain:** {uni.get('domains', ['N/A'])[0]}")
            
    # Show caching info
    st.info("💡 Try selecting the same country again - it loads instantly from cache!")
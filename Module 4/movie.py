import streamlit as st

st.title("🎥 Movie Night Planner")

# Select movie genres
genres = st.multiselect(
    "Select your favorite movie genres:",
    ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance"]
)

# Select streaming service
service = st.radio(
    "Choose your preferred streaming service:",
    ["Netflix", "Hulu", "Disney+", "Amazon Prime"]
)

# Simple movie recommendation mapping
recommendations = {
    "Action": "Extraction",
    "Comedy": "The Mask",
    "Drama": "The Godfather",
    "Horror": "A Quiet Place",
    "Sci-Fi": "Interstellar",
    "Romance": "La La Land"
}

# Recommend a movie based on first selected genre 
if genres:
    recommended_movie = recommendations.get(genres[0], "Movie Not Found")
    st.subheader(f"🎬 Recommended Movie: {recommended_movie} on {service}")
else:
    st.write("Select at least one genre to get a recommendation.")

# Feedback
st.subheader("⭐ Rate this recommendation")
feedback = st.radio("Your feedback:", ["Loved it ❤️", "It’s okay 🙂", "Not interested 😢"])
st.write(f"You selected: {feedback}")
import streamlit as st

st.title("🎥 Movie Night Planner")

# Select multiple movie genres
genres = st.multiselect(
    "Select your favorite movie genres:",
    ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance"]
)

# Select streaming service using pills
service = st.pills(
    "Choose your preferred streaming service:",
    ["Netflix", "Hulu", "Disney+", "Amazon Prime"]
)

# Movie recommendations based on genre
recommendations = {
    "Action": "Extraction",
    "Comedy": "The Mask", 
    "Drama": "The Godfather",
    "Horror": "A Quiet Place",
    "Sci-Fi": "Interstellar",
    "Romance": "La La Land"
}

# Show recommendation if genres selected
if genres and service:
    recommended_movie = recommendations.get(genres[0], "Movie Not Found")
    st.subheader(f"🎬 Recommended: {recommended_movie}")
    st.write(f"Available on {service}")
    
    # Collect feedback using st.feedback
    st.write("Rate this recommendation:")
    feedback = st.feedback("stars")
    
    if feedback is not None:
        rating_text = ["Poor", "Fair", "Good", "Very Good", "Excellent"]
        st.write(f"Thanks for rating: {rating_text[feedback]} ({feedback + 1} stars)")
else:
    if not genres:
        st.write("Select at least one genre to get started.")
    if not service:
        st.write("Choose a streaming service to see recommendations.")
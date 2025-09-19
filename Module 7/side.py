import streamlit as st

# Sample movie data
movies = [
    {"title": "The Matrix", "genre": "Sci-Fi", "rating": 8.7, "year": 1999},
    {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8, "year": 2010},
    {"title": "The Godfather", "genre": "Drama", "rating": 9.2, "year": 1972},
    {"title": "Pulp Fiction", "genre": "Drama", "rating": 8.9, "year": 1994},
    {"title": "Toy Story", "genre": "Animation", "rating": 8.3, "year": 1995},
    {"title": "Finding Nemo", "genre": "Animation", "rating": 8.2, "year": 2003}
]

st.title("Movie Recommendations")

# Sidebar filters
genre = st.sidebar.selectbox("Choose Genre", ["All", "Sci-Fi", "Drama", "Animation"])
min_rating = st.sidebar.slider("Minimum Rating", 0.0, 10.0, 7.0)
min_year = st.sidebar.number_input("From Year", min_value=1900, max_value=2024, value=1990)

# Filter movies
filtered_movies = []
for movie in movies:
    if (genre == "All" or movie["genre"] == genre) and \
       movie["rating"] >= min_rating and \
       movie["year"] >= min_year:
        filtered_movies.append(movie)

# Display results
st.write(f"Found {len(filtered_movies)} movies:")
for movie in filtered_movies:
    st.write(f"**{movie['title']}** ({movie['year']}) - {movie['genre']} - Rating: {movie['rating']}")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("🍴 Restaurant Review Dashboard")
st.write("Upload your restaurant review CSV to visualize ratings and review trends.")

# Step 1: Upload CSV
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=['ReviewDate'])
    st.write("Review Data Preview:")
    st.dataframe(df.head(10))
    
    # Step 2: Line Chart for Average Ratings Over Time
    st.subheader("📈 Average Ratings Over Time")
    daily_avg = df.groupby('ReviewDate')['Rating'].mean().reset_index()
    st.line_chart(daily_avg.set_index('ReviewDate'))
    
    # Step 3: Bar Chart for Total Reviews by Cuisine
    st.subheader("🏷️ Total Reviews by Cuisine")
    cuisine_reviews = df.groupby('Cuisine')['Rating'].count().sort_values(ascending=False)
    
    # Matplotlib horizontal bar chart
    fig, ax = plt.subplots()
    ax.barh(cuisine_reviews.index, cuisine_reviews.values, color='salmon')
    ax.set_xlabel('Number of Reviews')
    ax.set_title('Reviews by Cuisine')
    st.pyplot(fig)
    
    # Interactive Plotly version
    fig2 = px.bar(df.groupby('Cuisine')['Rating'].count().reset_index(),
                  x='Rating', y='Cuisine', orientation='h',
                  color='Cuisine', title="Interactive Reviews by Cuisine")
    st.plotly_chart(fig2, use_container_width=True)
    
    # Step 4: Key Metrics for Top 3 Cuisines
    st.subheader("🏅 Top 3 Most Reviewed Cuisines")
    top3 = cuisine_reviews.head(3)
    for i, (cuisine, count) in enumerate(top3.items(), 1):
        st.metric(f"{i}. {cuisine}", f"{count} reviews")
    
    # Average Rating Across All Restaurants
    avg_rating = df['Rating'].mean()
    st.metric("⭐ Average Rating", f"{avg_rating:.2f}")

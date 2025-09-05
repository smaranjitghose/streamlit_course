import streamlit as st

st.title("Travel Planner ✈️") # Sidebar inputs 
st.sidebar.header("Plan Your Trip")
destination = st.sidebar.text_input("Destination", "Paris")
start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")
budget = st.sidebar.number_input("Budget ($)", min_value=100, step=50)

# Main content 
st.subheader("Your Trip Summary")
st.write(f"Destination: {destination}")
st.write(f"Dates: {start_date} to {end_date}")
st.write(f"Budget: ${budget}")
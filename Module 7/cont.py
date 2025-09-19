import streamlit as st
import time

st.title("Live Sports Scoreboard")

# Create placeholder for score (will replace content)
score_placeholder = st.empty()

# Create container for commentary (will append content)
with st.container():
    st.subheader("Live Commentary")
    commentary_area = st.container()

# Simulate live updates
if st.button("Start Game Simulation"):
    # Game data
    home_team = "Lakers"
    away_team = "Warriors"
    
    # Simulate score updates
    for quarter in range(1, 5):
        home_score = quarter * 25 + (quarter * 3)
        away_score = quarter * 23 + (quarter * 2)
        
        # Update score (replaces previous score)
        score_placeholder.metric(
            label=f"Quarter {quarter}",
            value=f"{home_team} {home_score} - {away_score} {away_team}"
        )
        
        # Add commentary (appends to container)
        with commentary_area:
            st.write(f"⏰ End of Quarter {quarter}: Great plays from both teams!")
            if quarter == 2:
                st.write("🏀 Halftime: Players heading to locker rooms")
            elif quarter == 4:
                st.write("🎉 Game Over! What an exciting finish!")
        
        time.sleep(2)  # Simulate real-time delay
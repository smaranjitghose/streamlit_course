
# Module 6: Organizing Layouts in Streamlit

When building an app,  **how information is arranged literally shapes the user experience**. Imagine walking into a room—would you prefer furniture scattered randomly, or carefully placed so the space feels open and inviting? The same goes for your app’s layout.

Streamlit offers a rich toolkit for  **designing clean, intuitive interfaces**  that guide users effortlessly:

-   **Sidebar:**  Have you seen a control panel on the side of your favorite apps? That’s what the sidebar is—a place for filters, settings, or navigation that doesn’t crowd the main screen.
    
-   **Columns:**  Want to compare two things side-by-side? Columns are like using split screens or placing two pictures next to each other for easy comparison.
    
-   **Tabs:**  Ever used browser tabs? They let you switch between topics without losing context. Streamlit tabs do the same—organize related content in neat, clickable sections.
    
-   **Expanders:**  Think FAQ sections that hide answers until you ask for them—expanding on demand to keep things tidy.
    
-   **Containers & Placeholders:**  Imagine reserved seats or empty frames where content can appear or change without reshuffling your entire app. These keep your layout flexible and dynamic.
    

Instead of presenting these tools as abstract features,  **let’s explore how each feels and works**  by building projects you can touch and modify. 

*Layouts aren't just technical—they are the blueprint that shapes how your users  **discover, interact, and enjoy**  what your app offers.*

---------
### Topic 6.1: Sidebar

**Introduction**

Before we jump into building, let's understand the sidebar. The sidebar is your app's  **control panel**—like the dashboard in your car or the cockpit controls in an airplane. It’s a dedicated vertical space on the left where users can change settings, apply filters, or navigate between views without cluttering the main screen. This keeps your app clean, focused, and user-friendly.

### Mini Project: Travel Planner App

Now,  let’s see how to create a useful **Travel Planner app** where the sidebar collects user inputs for destination and dates, while the main screen summarizes the trip.

**Code**

```
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
```

**Expected Output**

-   Sidebar with input fields for destination, dates, and budget.
    
-   Main area displays a trip summary based on inputs.  
    (Screenshot placeholder: sidebar with fields + main summary text.)

**Key Takeaways**

-   Sidebar keeps inputs **organized and separate** from results.
    
-   Perfect for **filters, settings, or navigation menus**.

---
### Topic 6.2: Columns

**Introduction**

Think about comparing two things side by side—like opening two pages of a book or placing two photos next to each other. 
Columns let you split your screen horizontally, making comparisons easier and quicker.

Next, we’ll build a **Currency Comparison** tool that uses columns to show exchange rates side by side, so the viewer can instantly see both USD→EUR and EUR→USD rates clearly.

### Mini Project: Currency Comparison Tool

```
import streamlit as st

st.title("Currency Comparison Tool 💱") 
# Create two columns 
col1, col2 = st.columns(2) 
with col1:
    st.subheader("USD")
    st.metric("1 USD", "0.92 EUR") 
with col2:
    st.subheader("EUR")
    st.metric("1 EUR", "1.09 USD")
```

**Expected Output**

-   Two columns side by side.
    
-   Left shows USD to EUR rate.
    
-   Right shows EUR to USD rate.  
    (Screenshot placeholder: two-column layout with metrics.)
    
    
**Key Takeaways**

-   Use `st.columns()` to create **side-by-side comparisons**.
    
-   Great for dashboards, metrics, and before/after results.

---
### Topic 6.3: Tabs

Tabs work just like browser tabs or file folders inside your app, helping you organize content into neat sections. Instead of showing everything at once, tabs let users switch views easily—focus on one category at a time without distraction.

Let’s build a **Sports Stats Dashboard** with three tabs—Football, Basketball, and Cricket—where each tab shows the top scorer stats for that sport.

### Mini Project: Sports Stats Tabs

```
import streamlit as st

st.title("Sports Stats Dashboard 🏅")

tab1, tab2, tab3 = st.tabs(["Football", "Basketball", "Cricket"]) 
with tab1:
    st.subheader("Football Stats")
    st.write("Top Scorer: Messi - 30 goals") 
with tab2:
    st.subheader("Basketball Stats")
    st.write("Top Scorer: LeBron James - 25 PPG") 
with tab3:
    st.subheader("Cricket Stats")
    st.write("Top Scorer: Virat Kohli - 1200 runs")
```

**Expected Output**

-   Tabs labeled “Football”, “Basketball”, “Cricket”.
    
-   Clicking each tab shows the respective stats.  
    (Screenshot placeholder: three tabs with content switching.)


**Key Takeaways**

-   Tabs organize content without clutter.
    
-   Great for **dashboards with multiple categories**.

---

### Topic 6.4: Expanders 

Expanders are like secret compartments in your app that open up only when the user wants to see more. They are perfect for FAQs, explanations, or optional details, keeping your interface tidy while still letting curious users explore.

We’ll create an **FAQ Section** with common questions hidden inside expanders—clicking a question reveals its answer without overwhelming the page.

### Mini Project: FAQ Section

```
import streamlit as st

st.title("FAQ Section ❓") 
with st.expander("What is Streamlit?"):
    st.write("Streamlit is an open-source Python library for building web apps.") 
with st.expander("Is Streamlit free?"):
    st.write("Yes, Streamlit is free and open-source.") 
with st.expander("How do I install Streamlit?"):
    st.code("pip install streamlit", language="bash")
``` 

**Expected Output**

-   Three FAQ questions with expanders.
    
-   Clicking one reveals the answer.  
    (Screenshot placeholder: collapsible sections opening on click.)

**Key Takeaways**

-   Expanders keep apps **tidy and uncluttered**.
    
-   Perfect for FAQs, help text, or advanced settings.
------
### Topic 6.5: Containers & Placeholders 

Imagine a reserved seat in a theater—it stays empty until the show starts, then someone sits down. Containers and placeholders in Streamlit reserve space where content can dynamically update without messing up the rest of your layout.

To demonstrate, we’ll create a **Live Scoreboard** that updates its value every second, showing the current score using a placeholder that refreshes in place.

### Mini Project: Live Scoreboard

```
import streamlit as st 
import time

st.title("Live Scoreboard 🏏") 
# Create a placeholder 
score_placeholder = st.empty()

score = 0  
for i in  range(5):
    score += 4  # Imagine scoring runs 
    score_placeholder.metric("Current Score", f"{score}")
    time.sleep(1)
```

**Expected Output**

-   A metric card labeled “Current Score”.
    
-   Updates every second as the loop runs.  
    (Screenshot placeholder: live-updating score counter.)
    
**Key Takeaways**

-   `st.empty()` creates placeholders for dynamic updates.
    
-   Useful for **live dashboards, progress, or streaming data**.
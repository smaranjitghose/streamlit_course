
# Module 5: Data Visualization in Streamlit

Numbers in tables can feel overwhelming and cold—rows and columns of figures often fail to tell the full story.  **Visualization is the art of transforming raw numbers into compelling stories**  that highlight trends, show comparisons, reveal patterns, and bring data to life at a glance.

Streamlit makes this process  **seamless and accessible**  by combining a rich set of built-in plotting tools with powerful, industry-standard libraries like Matplotlib, Seaborn, Plotly, and Altair. It even supports interactive maps for geospatial insights. Whether you need a quick chart or a highly customizable, interactive dashboard, Streamlit has you covered.

----------

### Topic 5.1: Built-in Charts 

**Introduction**

Streamlit’s built-in charts such as  `st.line_chart()`,  `st.bar_chart()`, and  `st.area_chart()`  are like the  **instant noodles of data visualization**—fast, easy, and deliciously satisfying for many common use cases.

These functions enable you to visualize data directly from simple pandas DataFrames without fiddling with detailed chart configurations. They are perfect for quickly spotting  **daily trends, comparing quantities, or showing cumulative totals**  in a clean and responsive way.

Think of them as your fast food option for visualization—ready in seconds, good-looking, and almost always the right tool when you want to see  _what’s happening_  right away.

### Mini Project:  Step Tracker App

**Introduction**

Now let’s build a simple fitness dashboard using Streamlit’s built-in charts to track steps, calories burned, and sleep patterns.

**Code**

```python

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Fitness Dashboard", layout="wide")
st.title("📊 My Fitness Dashboard")

# Fake dataset for 7 days
days = pd.date_range(start="2023-01-01", periods=7)
data = pd.DataFrame({
    "Steps": np.random.randint(3000, 12000, size=7),
    "Calories Burned": np.random.randint(1800, 2800, size=7),
    "Hours Slept": np.random.uniform(5, 9, size=7).round(1)
}, index=days)

# Dashboard sections
st.subheader("👟 Daily Steps")
st.line_chart(data["Steps"])

st.subheader("🔥 Calories Burned")
st.bar_chart(data["Calories Burned"])

st.subheader("💤 Sleep Hours")
st.area_chart(data["Hours Slept"])

# Preview of raw data
st.subheader("📋 Data Table")
st.dataframe(data)


```

**Expected Output**

- 📈 A line chart showing dates on the x-axis and steps on the y-axis (daily step count).

<img src ="https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%205/step1.png">

- 📊 A bar chart showing dates vs. calories burned each day.

<img src ="https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%205/step2.png">


- 🌙 An area chart showing dates vs. hours slept per night.

<img src ="https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%205/step3.png">


- 📋 A data table displaying all the metrics (Steps, Calories Burned, Sleep Hours).
    

**Key Takeaways**

-   Built-in charts like  `st.line_chart()`  are super quick to implement.
    
-   They work directly with Pandas DataFrames.
    
-   Perfect for fast data exploration or embedding simple dashboards.
----------

### Topic 5.2: Matplotlib & Seaborn 

**Introduction**

Matplotlib and Seaborn are your  **artist-grade paintbrushes**  for data visualization in Python. They provide  **fine control over every aspect of your plot**, from colors and shapes to advanced statistical overlays.

Matplotlib lays the foundation with raw power and customization, while Seaborn builds on it with beautiful default styles and easier syntax for complex statistical charts.

Use these when you want to  **explore data deeply**, reveal distributions, plot relationships, or craft polished figures for reports and publications. Streamlit’s  `st.pyplot()`  integrates these seamlessly, letting you combine artistic flexibility with easy app deployment.

### Mini Project: Student Marks Visualizer

**Introduction**

Let’s use Matplotlib and Seaborn to create a more customized and polished chart. We’ll visualize a distribution of student marks using a histogram and smooth KDE curve.

**Code**

```python

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Student Marks Visualizer", layout="centered")
st.title("📊 Student Marks Visualizer")

# Generate mock marks for multiple subjects
np.random.seed(42)
subjects = {
    "Math": np.random.normal(75, 12, 100),
    "Science": np.random.normal(70, 15, 100),
    "English": np.random.normal(65, 10, 100),
    "History": np.random.normal(68, 8, 100)
}
df = pd.DataFrame(subjects)

# Sidebar input
st.sidebar.header("⚙️ Settings")
subject_choice = st.sidebar.selectbox("Choose a subject:", df.columns)
bins = st.sidebar.slider("Number of bins:", 5, 20, 10)

# Plot
st.subheader(f"Distribution of Marks in {subject_choice}")
fig, ax = plt.subplots()
sns.histplot(df[subject_choice], bins=bins, kde=True, color="skyblue", ax=ax)
ax.set_xlabel("Marks")
ax.set_ylabel("Number of Students")
ax.set_title(f"{subject_choice} Marks Distribution")

st.pyplot(fig)

# Extra insight
st.subheader("📋 Summary Statistics")
st.write(df[subject_choice].describe().round(2))


```

**Expected Output**

-   A histogram showing frequency distribution of marks by subject.
    
-   A smooth KDE curve overlay indicating the general shape.
    
<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%205/marks1.png">

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%205/marks2.png">


**Key Takeaways**

-   Matplotlib + Seaborn offer granular control and aesthetics.
    
-   Use  `st.pyplot(fig)`  to embed these plots in Streamlit.
    
-   Excellent for statistical analysis and refined data storytelling.
----------

### Topic 5.3: Plotly & Altair 

**Introduction**

Plotly and Altair bring your data to life with  **interactive, dashboard-ready visuals**. Unlike static charts, these allow your users to  **hover for details, zoom into areas of interest, and filter or select data subsets**, unlocking richer insights.

They’re like fully equipped interactive exhibits in a museum—allowing visitors to touch, explore, and discover patterns on their own.

Streamlit’s native support means you can embed and control these powerful tools with just a few lines of code. Use them to build  **professional dashboards where exploration and user engagement are key**.

### Mini Project: Sales Dashboard

**Introduction**

Next, we’ll explore interactive plotting with Plotly. Build a sales dashboard with an interactive bar chart that lets users hover, zoom, and explore monthly sales data by region.

**Code**

```python

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📊 Sales Dashboard")

# Fake dataset (12 months for more flexibility)
months = pd.date_range("2023-01-01", periods=12, freq="M")
data = pd.DataFrame({
    "Month": np.tile(months, 3),
    "Region": np.repeat(["North", "South", "West"], 12),
    "Sales": np.random.randint(1000, 5000, size=36),
    "Profit": np.random.randint(200, 1500, size=36)
})

# Sidebar filter
st.sidebar.header("🔎 Filters")
months_to_show = st.sidebar.slider("Select number of recent months:", 3, 12, 6)
region_choice = st.sidebar.selectbox("Select Region for Detailed View:", data["Region"].unique())

# Filter dataset by recent months
latest_months = data["Month"].sort_values().unique()[-months_to_show:]
filtered_data = data[data["Month"].isin(latest_months)]

# Chart 1: Sales overview
st.subheader("📈 Monthly Sales Overview")
fig1 = px.bar(filtered_data, x="Month", y="Sales", color="Region", barmode="group",
              title="Sales by Region")
st.plotly_chart(fig1, use_container_width=True)

# Chart 2: Profit trend
st.subheader("💰 Profit Trend")
fig2 = px.line(filtered_data, x="Month", y="Profit", color="Region", markers=True,
               title="Monthly Profit by Region")
st.plotly_chart(fig2, use_container_width=True)

# Chart 3: Regional focus
st.subheader(f"🎯 Sales Trend in {region_choice}")
region_data = filtered_data[filtered_data["Region"] == region_choice]
fig3 = px.area(region_data, x="Month", y="Sales",
               title=f"Sales Trend in {region_choice}", markers=True)
st.plotly_chart(fig3, use_container_width=True)

# Raw data
st.subheader("📋 Filtered Data Table")
st.dataframe(filtered_data)


```
**Expected**

- 📊 An interactive bar chart showing monthly sales by region (with zoom, pan, and hover tooltips).

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%205/sales1.png">

- 📈 An interactive line chart showing profit trends across regions over time.

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%205/sales2.png">

- 🌍 An interactive area chart that updates dynamically based on the selected region in the sidebar.

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%205/sales3.png">

- 📋 A data table displaying only the filtered months and region, matching the charts.
    
<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%205/sales4.png">

    

**Key Takeaways**

-   Plotly adds rich interactivity for deeper user exploration.
    
-   Use  `st.plotly_chart(fig)`  to embed Plotly visuals easily.
    
-   Ideal for professional, polished dashboards.

----------

### Topic 5.4: Maps (Pydeck/Folium) 

**Introduction**

Maps uniquely blend  **data with geography**, giving meaning to location-based information. They’re essential for everything from visualizing customer distribution, tracking delivery routes, to highlighting tourist hotspots.

Streamlit supports Pydeck (for built-in, high-performance 3D geospatial visualizations) and Folium (for rich, customizable maps) so you can  **pin ideas on a globe**  and interact intuitively.

Mapping your data adds a spatial dimension that can make patterns visible only when seen in context—turning raw coordinates into meaningful stories.

### Mini Project: City Explorer

## Introduction

Finally, we’ll visualize geospatial data by mapping tourist spots with Pydeck, Streamlit’s built-in map visualization tool.

## Code

```python

import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="Tourist Spot Explorer", layout="centered")
st.title("🕌 Explore Indian Tourist Spots")

# Dataset with 2 places
data = pd.DataFrame({
    "spot": ["Taj Mahal", "Golden Temple"],
    "city": ["Agra", "Amritsar"],
    "description": [
        "One of the Seven Wonders of the World, a symbol of love in Agra.",
        "The holiest gurdwara and a central religious place for Sikhs, in Amritsar."
    ],
    "lat": [27.1751, 31.6200],
    "lon": [78.0421, 74.8765],
    "image": [
        "https://upload.wikimedia.org/wikipedia/commons/d/da/Taj-Mahal.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/3/34/Golden_Temple_in_Amritsar_India.jpg"
    ]
})

# Dropdown to choose tourist spot
choice = st.selectbox("Select a tourist spot:", data["spot"])

# Filter data
selected = data[data["spot"] == choice].iloc[0]

# Show details
st.header(f"{selected['spot']} ({selected['city']})")
st.write(selected["description"])
st.image(selected["image"], use_container_width=True)

# Show map for selected place
st.subheader("📍 Location on Map")
layer = pdk.Layer(
    "ScatterplotLayer",
    pd.DataFrame([selected]),
    get_position=["lon", "lat"],
    get_color=[200, 30, 0, 160],
    get_radius=40000,
    pickable=True
)

view_state = pdk.ViewState(latitude=selected["lat"], longitude=selected["lon"], zoom=10)

st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"text": "{spot}, {city}"}
))


```

**Expected Output**

- When a user selects Taj Mahal or Golden Temple from the dropdown, the app first displays the spot’s name and city.

- Below that, the app shows a short description of the tourist spot.

- Next, an image of the selected location is displayed.

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%205/city1.png">

- Finally, an interactive zoomable map appears, centered on the chosen spot, with a red marker highlighting its location.

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%205/city2.png">

    

**Key Takeaways**

-   Maps connect your data to real-world geography.
    
-   Pydeck is bundled and efficient for location-based visualizations.
    
-   Folium can be added externally for more complex mapping needs.
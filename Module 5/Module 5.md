
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

Now let’s see how easy it is to create a simple visualization with Streamlit’s built-in charts. We’ll build a step tracker that displays your daily steps as a clear line chart.

**Code**

```python

import streamlit as st
import pandas as pd
import numpy as np

st.title("Step Tracker App 👟")

# Generate 7 days of mock step data
days = pd.date_range(start="2023-01-01", periods=7)
steps = np.random.randint(3000, 12000, size=7)

data = pd.DataFrame({"Steps": steps}, index=days)

st.subheader("Daily Step Counts")
st.line_chart(data)

```

**Expected Output**

-   A line chart showing dates on the x-axis and steps on the y-axis.
    
-   Each point represents the steps walked on that day.
    
<img src ="https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%205/steptracker.png">
    

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

st.title("Student Marks Visualizer 📊")

# Generate mock marks
marks = np.random.normal(70, 10, 100)
df = pd.DataFrame({"Marks": marks})

st.subheader("Distribution of Marks")

# Plot histogram with KDE
fig, ax = plt.subplots()
sns.histplot(df["Marks"], bins=10, kde=True, ax=ax)
ax.set_xlabel("Marks")
ax.set_ylabel("Number of Students")
ax.set_title("Student Marks Distribution")

st.pyplot(fig)

```

**Expected Output**

-   A histogram showing frequency distribution of marks.
    
-   A smooth KDE curve overlay indicating the general shape.
    
<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%205/marksvisualizer.png">
    

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

Next, we’ll explore interactive plotting with Plotly. Build a sales dashboard with an interactive bar chart that lets users hover, zoom, and explore monthly sales data.

**Code**

```python

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Sales Dashboard 📈")

months = pd.date_range("2023-01-01", periods=6, freq="M")
sales = np.random.randint(1000, 5000, size=6)
df = pd.DataFrame({"Month": months, "Sales": sales})

st.subheader("Monthly Sales Overview")

fig = px.bar(df, x="Month", y="Sales", title="Sales Over Time", text="Sales")
fig.update_traces(textposition="outside")

st.plotly_chart(fig, use_container_width=True)

```

**Expected Output**

-   An interactive bar chart showing sales per month.
    
-   Hover over bars for detailed values; zoom and pan on chart.
    
<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%205/sales_dashboard.png">
    

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

st.title("City Explorer 🗺️")

data = pd.DataFrame({
    "city": ["Paris", "New York", "Tokyo", "Sydney"],
    "lat": [48.8566, 40.7128, 35.6895, -33.8688],
    "lon": [2.3522, -74.0060, 139.6917, 151.2093]
})

st.subheader("Tourist Spots Map")

layer = pdk.Layer(
    "ScatterplotLayer",
    data,
    get_position=["lon", "lat"],
    get_color=[200, 30, 0, 160],
    get_radius=50000,
)

view_state = pdk.ViewState(latitude=20, longitude=0, zoom=1)

st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

```

**Expected Output**

-   A zoomable, pannable world map centered broadly on the globe.
    
-   Red dots marking Paris, New York, Tokyo, and Sydney locations.
    
<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%205/cityexplorer.png">

**Key Takeaways**

-   Maps connect your data to real-world geography.
    
-   Pydeck is bundled and efficient for location-based visualizations.
    
-   Folium can be added externally for more complex mapping needs.
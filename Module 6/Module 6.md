# Module 6: Data Visualization

### Topic 6.1: Built-in Charts

<br>

#### **Introduction**

Numbers on a spreadsheet can feel overwhelming—but the moment you turn them into a chart, the story hidden inside becomes clear. Streamlit makes this process effortless with built-in chart functions like `st.line_chart()`, `st.area_chart()`, `st.bar_chart()`, and `st.scatter_chart()`. With just a few lines of code, your data transforms into interactive visuals that highlight trends, comparisons, and relationships.

Each chart type has its own personality: line charts trace change over time, area charts show growth piling up, bar charts stack categories side by side, and scatter plots reveal hidden connections. Choosing the right one doesn’t just make your app look good—it makes your insights easier to understand and more impactful.

#### **Mini Project**

Jake has been tracking his steps, workouts, calories, and sleep for months but feels like he's making no progress. His fitness app shows basic daily numbers, but he can't see if his efforts are actually working or how his different health metrics connect to each other. Without clear insights into patterns and trends, Jake feels discouraged and unsure if his routine is effective.
A comprehensive fitness dashboard would reveal the hidden progress in Jake's data and show him which habits have the biggest impact on his overall wellness.

##### **Project Setup**

Create a new file `app.py`:

```python
import streamlit as st
import pandas as pd

st.title("Fitness Progress Dashboard")

# Sample fitness data
fitness_data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', '2024-01-07'],
    'Steps': [8500, 9200, 7800, 10500, 9800, 8900, 11200],
    'Calories': [2200, 2400, 2100, 2600, 2500, 2300, 2700],
    'Workouts': [1, 2, 0, 2, 1, 1, 2],
    'Sleep': [7.5, 8.0, 6.5, 7.8, 8.2, 7.0, 8.5]
}

df = pd.DataFrame(fitness_data)

# Steps trend line chart
st.subheader("Daily Steps Trend")
st.line_chart(df.set_index('Date')['Steps'])

# Calories area chart
st.subheader("Calorie Burn Over Time") 
st.area_chart(df.set_index('Date')['Calories'])

# Workouts bar chart
st.subheader("Weekly Workout Sessions")
st.bar_chart(df.set_index('Date')['Workouts'])

# Sleep vs Calories scatter plot
st.subheader("Sleep vs Calories Relationship")
scatter_data = df[['Sleep', 'Calories']].rename(columns={'Sleep': 'x', 'Calories': 'y'})
st.scatter_chart(scatter_data)

# Data summary
st.subheader("Week Summary")

st.metric("Avg Steps", f"{df['Steps'].mean():.0f}")

st.metric("Avg Calories", f"{df['Calories'].mean():.0f}")

st.metric("Total Workouts", df['Workouts'].sum())

st.metric("Avg Sleep", f"{df['Sleep'].mean():.1f}h")
```

**Run your app with:**

```bash
streamlit run app.py
```
----

#### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%206/mod6chart1.png">



<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%206/mod6chart2.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%206/mod6chart3.png">




<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%206/mod6chart4.png">



---

#### **Step-by-Step Walkthrough**

The sample data represents a week of fitness tracking with realistic values that demonstrate healthy activity levels and balanced metrics across different aspects of fitness monitoring.

-   The `st.line_chart()` displays daily steps as a connected line, making it easy to spot trends and patterns in activity levels throughout the week. The line format clearly shows increases and decreases over time. **Parameters include:**
    
    -   `data`: The dataset to be plotted (e.g., a pandas DataFrame or Series).
        
    -   `width`: Optional, the width of the chart in pixels.
        
    -   `height`: Optional, the height of the chart in pixels.
        
    -   `use_container_width`: Optional, whether to make the chart use the full width of the container (default is True).
        
-   The `st.area_chart()` shows calorie burn with filled areas that emphasize the magnitude of daily energy expenditure. The filled area makes it easy to compare relative daily totals at a glance. **Parameters include:**
    
    -   `data`: The dataset to be plotted (pandas DataFrame or Series).
        
    -   `width`: Optional chart width in pixels.
        
    -   `height`: Optional chart height in pixels.
        
    -   `use_container_width`: Optional, whether the chart should expand to container width.
        
-   The `st.bar_chart()` displays workout sessions as discrete bars, perfect for comparing specific daily activity counts. Bar charts work well for categorical data like workout frequency. **Parameters include:**
    
    -   `data`: The dataset to plot as bars.
        
    -   `width`: Optional chart width in pixels.
        
    -   `height`: Optional chart height in pixels.
        
    -   `use_container_width`: Optional, whether the chart should expand to container width.
        
-   The `st.scatter_chart()` explores the relationship between sleep hours and calorie burn by plotting each day as a point. This helps identify whether better sleep correlates with higher activity levels. **Parameters include:**
    
    -   `data`: The dataset to be plotted (pandas DataFrame).
        
    -   `width`: Optional chart width in pixels.
        
    -   `height`: Optional chart height in pixels.
        
    -   `use_container_width`: Optional, whether the chart should expand to container width.
        
-   The summary metrics provide key statistics that complement the visual analysis, giving users both graphical trends and numerical benchmarks for their fitness progress.

---

#### **Key Learning Points**

-   **Chart choice matters:** Selecting the right chart type depends on whether the goal is to show trends, compare categories, highlight magnitude, or explore relationships.
    
-   **Visual balance:** Mixing multiple chart types helps avoid bias — no single visualization tells the full story.
    
-   **Complementary metrics:** Pairing charts with summary statistics strengthens interpretation and adds context.
    
-   **Clarity over complexity:** Simple, well-labeled charts are more effective than cramming too much into a single visualization.
    
-   **User perspective:** Always design visualizations around the questions users are likely to ask of the data.

#### **Conclusion**

Built-in Streamlit charts democratize professional data visualization by making sophisticated analytical displays achievable with minimal code complexity. Whether tracking fitness metrics, monitoring business KPIs, or analyzing research data, these visualization tools empower users to transform numbers into actionable insights through clean, interactive displays that communicate effectively without requiring design expertise.

----

### Topic 6.2: Matplotlib Integration

<br>

#### **Introduction**

Think about the last time you needed a specific type of chart - maybe a violin plot for statistical analysis, or a subplot with multiple visualizations. While Streamlit provides excellent built-in charting functions like `st.line_chart()` and `st.bar_chart()`, you quickly hit their limits when you need something more specialized. What if you could access Python's most powerful visualization library directly in your Streamlit apps?

The `st.pyplot()` function bridges this gap, allowing you to display any Matplotlib figure directly in your Streamlit interface. This integration opens up advanced visualization possibilities - from statistical plots and subplots to highly customized charts that match your exact specifications. Whether you're creating scientific visualizations, detailed analytical dashboards, or simply need plotting features beyond Streamlit's native options, `st.pyplot()` gives you access to the entire Matplotlib ecosystem without leaving the simplicity of Streamlit.

#### **Mini Project**

Ms. Rodriguez teaches multiple subjects at Roosevelt High School and notices her students seem to be struggling more than usual this semester, but she can't pinpoint exactly where the problems lie. She has spreadsheets full of test scores and grades, but staring at rows and columns of numbers doesn't reveal the patterns she needs to see. Are students consistently weak in certain subjects? Is performance getting worse over time? Without clear visual insights, she can't identify which students need extra help or adjust her teaching strategies effectively.
A grade analysis app would transform her confusing spreadsheet data into clear visual patterns, helping Ms. Rodriguez understand her students' performance trends and make informed decisions about where to focus her teaching efforts.

##### **Project Setup**

Create a new file `app.py`:

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Exam Performance Analyzer")
st.write("Upload your grades CSV to analyze student performance patterns")

# Sample data for demonstration
sample_data = {
    'Student': ['Alice', 'Bob', 'Carol', 'David', 'Eve', 'Frank', 'Grace', 'Henry'] * 3,
    'Subject': ['Math', 'Math', 'Math', 'Math', 'Math', 'Math', 'Math', 'Math',
                'Science', 'Science', 'Science', 'Science', 'Science', 'Science', 'Science', 'Science',
                'English', 'English', 'English', 'English', 'English', 'English', 'English', 'English'],
    'Score': [85, 72, 91, 68, 94, 79, 83, 77, 
              88, 75, 89, 71, 92, 81, 86, 74,
              82, 78, 87, 73, 89, 84, 80, 76],
    'Exam_Date': ['2024-01-15'] * 8 + ['2024-02-15'] * 8 + ['2024-03-15'] * 8
}

df = pd.DataFrame(sample_data)
st.write("Sample Data Preview:")
st.dataframe(df.head())

# 1. Grade Distribution Histogram
st.subheader("📈 Overall Grade Distribution")
fig1, ax1 = plt.subplots(figsize=(8, 5))
ax1.hist(df['Score'], bins=10, color='skyblue', alpha=0.7, edgecolor='black')
ax1.set_xlabel('Score')
ax1.set_ylabel('Number of Students')
ax1.set_title('Distribution of Exam Scores')
ax1.grid(True, alpha=0.3)
st.pyplot(fig1)

# 2. Subject-wise Performance Boxplots
st.subheader("📦 Subject-wise Performance Spread")
fig2, ax2 = plt.subplots(figsize=(8, 5))
subjects = df['Subject'].unique()
subject_scores = [df[df['Subject'] == subject]['Score'].values for subject in subjects]
ax2.boxplot(subject_scores, tick_labels=subjects)
ax2.set_ylabel('Score')
ax2.set_title('Score Distribution by Subject')
ax2.grid(True, alpha=0.3)
st.pyplot(fig2)

# 3. Average Scores Over Time
st.subheader("📊 Average Performance Trends")
avg_by_date = df.groupby('Exam_Date')['Score'].mean()
fig3, ax3 = plt.subplots(figsize=(8, 5))
ax3.plot(avg_by_date.index, avg_by_date.values, marker='o', linewidth=2, markersize=8, color='green')
ax3.set_xlabel('Exam Date')
ax3.set_ylabel('Average Score')
ax3.set_title('Class Average Performance Over Time')
ax3.grid(True, alpha=0.3)
plt.xticks(rotation=45)
st.pyplot(fig3)
```

**Run your app with:**

```bash
streamlit run app.py
```
---
##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%206/mod6matplot1.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%206/mod6matplot2.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%206/mod6matplot3.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%206/mod6matplot4.png">

---

#### **Step-by-Step Walkthrough**

-   **Matplotlib (`matplotlib.pyplot`)**: A plotting library for the Python programming language. Used for creating custom plots (histograms, boxplots, line plots) with full control over styling and layout.
    
-   **`plt.subplots()`**: Creates a Figure (`fig`) and Axes (`ax`) where charts are drawn.
    
-   **`ax.hist()`**: Plots a histogram to show how many students fall within each score range.
    
-   **`ax.boxplot()`**: Creates boxplots to display score distribution by subject (median, quartiles, outliers).
    
-   **`ax.plot()`**: Draws a line plot of average scores over exam dates to reveal performance trends.
    
-   **`plt.xticks(rotation=45)`**: Rotates date labels for readability on the x-axis.
    
-   **`ax.set_xlabel()`, `ax.set_ylabel()`, `ax.set_title()`**: Add chart labels and titles.
    
-   **`ax.grid()`**: Adds a light grid to make charts easier to read.
    
-   **`st.pyplot(fig)`**: Displays the Matplotlib figure directly in the Streamlit app.
---

#### **Conclusion**

By bridging Streamlit's simplicity with Matplotlib's comprehensive visualization ecosystem, st.pyplot() provides an elegant upgrade path from basic charts to professional-grade analytics. This capability transforms Streamlit applications from simple dashboards into sophisticated analytical platforms capable of handling complex statistical visualizations, custom branding requirements, and specialized plotting needs that rival dedicated visualization software.


---

### Topic 6.3: Plotly Integration

<br>

#### **Introduction**

Have you ever wished your Streamlit charts could zoom, pan, and respond to user interaction? While static charts tell a story, interactive visualizations let your users explore the data themselves. Imagine being able to hover over data points for detailed information, zoom into specific time periods, or click on legend items to filter the view - all without writing complex JavaScript.  

The `st.plotly_chart()` function brings Plotly's powerful interactive visualization capabilities directly into your Streamlit apps. Unlike static matplotlib figures, Plotly charts are naturally interactive, responsive, and web-ready. This integration transforms your dashboards from simple displays into engaging analytical tools where users can dive deep into the data with intuitive gestures like hovering, clicking, and zooming.  

#### **Mini Project**
You're helping a small business owner analyze their sales performance across different regions and product categories. They need an interactive dashboard where they can explore revenue trends over time, see the breakdown of sales by category, and compare performance across regions.  

The interactivity is crucial - they want to zoom into specific months, hover for exact values, and click to focus on particular categories. Static charts won't give them the exploratory power they need.  

##### **Project Setup**

Create a new file **`app.py`**:

```python
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

st.title("📈 Sales Analytics Dashboard")
st.write("Interactive business intelligence for small business owners")

# Sample sales data
np.random.seed(42)
dates = pd.date_range('2024-01-01', '2024-06-30', freq='D')
categories = ['Electronics', 'Clothing', 'Home & Garden', 'Books', 'Sports']
regions = ['North', 'South', 'East', 'West']

sample_data = []
for date in dates[:90]:  # 3 months of data
    for _ in range(np.random.randint(3, 8)):  # 3-7 sales per day
        sample_data.append({
            'Date': date,
            'Category': np.random.choice(categories),
            'Region': np.random.choice(regions),
            'Revenue': np.random.uniform(50, 500),
            'Units_Sold': np.random.randint(1, 10)
        })

df = pd.DataFrame(sample_data)
st.write("Sample Sales Data Preview:")
st.dataframe(df.head())

# 1. Interactive Revenue Trend Line Chart
st.subheader("📊 Revenue Trend Over Time")
daily_revenue = df.groupby('Date')['Revenue'].sum().reset_index()
fig1 = px.line(daily_revenue, x='Date', y='Revenue', 
               title='Daily Revenue Trend',
               labels={'Revenue': 'Revenue ($)', 'Date': 'Date'})
fig1.update_traces(line=dict(width=3, color='#1f77b4'))
fig1.update_layout(hovermode='x unified')
st.plotly_chart(fig1, use_container_width=True)

# 2. Category Breakdown Pie Chart
st.subheader("🍰 Sales by Product Category")
category_sales = df.groupby('Category')['Revenue'].sum().reset_index()
fig2 = px.pie(category_sales, values='Revenue', names='Category',
              title='Revenue Distribution by Category',
              color_discrete_sequence=px.colors.qualitative.Set3)
fig2.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig2, use_container_width=True)

# 3. Regional Performance Bar Chart
st.subheader("🗺️ Regional Sales Performance")
region_sales = df.groupby('Region')['Revenue'].sum().reset_index()
fig3 = px.bar(region_sales, x='Region', y='Revenue',
              title='Total Revenue by Region',
              color='Revenue',
              color_continuous_scale='viridis')
fig3.update_traces(texttemplate='$%{y:,.0f}', textposition='outside')
fig3.update_layout(showlegend=False)
st.plotly_chart(fig3, use_container_width=True)

# 4. Bonus: Interactive Category-Region Heatmap
st.subheader("🔥 Category-Region Performance Heatmap")
heatmap_data = df.groupby(['Category', 'Region'])['Revenue'].sum().reset_index()
pivot_data = heatmap_data.pivot(index='Category', columns='Region', values='Revenue')
fig4 = px.imshow(pivot_data, 
                 title='Revenue Heatmap: Category vs Region',
                 aspect='auto',
                 color_continuous_scale='Blues')
st.plotly_chart(fig4, use_container_width=True)

```

**Run your app with:**

```bash
streamlit run app.py
```

##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%206/mod6plotly1.png">

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%206/mod6plotly2.png">



<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%206/mod6plotly3.png">



<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%206/mod6plotly4.png">



<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%206/mod6plotly5.png">


---

#### **Step-by-Step Walkthrough**

-   **Plotly (`plotly.express` / `plotly.graph_objects`)**: An interactive visualization library for Python that creates web-ready, browser-based charts with built-in interactivity (zoom, hover, click).
    
-   **px.line()**: Creates an interactive line chart for time-series data, showing trends and allowing hover for exact values.
    
-   **px.pie()**: Generates an interactive pie chart with automatic color schemes; users can click legend items to show/hide categories.
    
-   **px.bar()**: Creates a bar chart with color mapping and text annotations; hover shows precise values.
    
-   **px.imshow()**: Generates a heatmap or correlation-style visualization with color-coded intensity.
    
-   **update_traces() / update_layout()**: Customize chart appearance, marker style, hover behavior, and label positions.
    
-   **st.plotly_chart(fig, use_container_width=True)**: Displays the Plotly figure in Streamlit while preserving interactivity and making it responsive.
   
---

#### **Conclusion**

By combining Streamlit's deployment simplicity with Plotly's interactive sophistication, `st.plotly_chart()` creates intelligent visualizations that adapt to user behavior and exploration patterns. This powerful pairing ensures your applications can handle everything from executive dashboards requiring drill-down capabilities to scientific tools needing detailed data examination, making complex datasets accessible through intuitive, responsive interfaces.


----

### Topic 6.4: Comparative Visualization

<br>

#### **Introduction**

Have you ever looked at a chart and wondered, “What does this really tell me?” A single visualization only shows part of the story. Comparative visualization combines multiple charts and key metrics to create a fuller, more meaningful picture.

By placing different visual elements side by side—like trends, category comparisons, and performance indicators—you can see patterns, relationships, and insights that would be hard to notice in isolation.

Streamlit makes it easy to mix line charts, bar charts, and metrics in a single dashboard, allowing each element to complement the others. This approach transforms scattered data points into clear, actionable insights, helping you make smarter, data-driven decisions.

#### **Mini Project**

Maya is a food blogger who collects restaurant reviews from various sources but struggles to make sense of the overwhelming data scattered across spreadsheets. She has hundreds of reviews with ratings, cuisines, and dates, but can't easily identify which types of restaurants are trending, whether certain cuisines consistently perform better, or which establishments deserve her next feature article. Manually sorting through rows of data to find meaningful patterns takes hours and often leads to missed opportunities.
A restaurant review analyzer would transform Maya's messy data into clear visual insights, helping her quickly spot dining trends and identify the standout restaurants worth writing about. 

##### **Project Setup**

Create a new file `app.py`:

```python
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

```

**Run your app with:**

```bash
streamlit run app.py
```

##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%206/visual1mod6.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%206/visual2mod6.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%206/visual3mod6.png">

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%206/visual4mod6.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%206/visual5mod6.png">

---

#### **Step-by-Step Walkthrough**

-   **Dashboard Overview:** Combines multiple chart types and metrics to tell a financial story.
    
-   **Line Chart:** Shows trends over time; helps identify when spending events occur.
    
-   **Bar Chart:** Compares spending across categories; shows what drives overall expenses.

-   **Metrics Row:** Displays key performance indicators to highlight the most important insights upfront.
    
-   **Additional Insights:** Highlights extremes, averages, and monthly changes to provide context.
    
-   **Integrated Storytelling:** Metrics, trend charts, and category charts work together to reveal patterns and support decision-making.

---

#### **Conclusion**

The power of mixed visualization approaches lies in their ability to present data at multiple analytical levels simultaneously, enabling users to make informed decisions quickly while retaining access to supporting details. This comprehensive view—combining at-a-glance metrics with exploratory charts—transforms Streamlit applications into decision-support systems that accommodate different user needs, from executives requiring summary insights to analysts needing detailed investigation capabilities.
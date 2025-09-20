# Module 3: Displaying & Exploring Data

### Topic 3.1: DataFrames & Tables 

<br>

#### **Introduction**

In today's data-driven world, numbers aren't just statistics—they're the foundation of decisions, insights, and meaningful stories. From tracking monthly expenses to analyzing business performance, effective data presentation transforms raw information into actionable knowledge that people can understand and act upon.

Streamlit makes this transformation seamless with functions designed specifically for displaying structured data. Instead of wrestling with complex frontend code or trying to format tables manually, you can present data professionally with just a few simple commands.

Think of a DataFrame as a digital spreadsheet that lives inside your app. It organizes information into neat rows and columns, just like Excel or Google Sheets, but with the power to be interactive and dynamic. Understanding how to display this data effectively is essential for any data-focused application.

#### **Core Concepts**

Streamlit provides two complementary approaches for displaying tabular data, each serving different user interaction needs:

- **Interactive vs. Static presentation**: `st.dataframe()` creates interactive tables where users can scroll, sort, and explore large datasets dynamically. `st.table()` creates static snapshots that present fixed information cleanly without user interaction. The choice depends on whether you want users to explore data or simply view specific information.

- **Data exploration vs. information delivery**: Interactive tables work best when users need to discover patterns or find specific records in large datasets. Static tables excel when presenting summarized results, reports, or key metrics that don't require manipulation.

#### **Mini Project**

You want to build a personal finance tool to track where your money goes each month. Instead of manually calculating totals in a notebook or using complex spreadsheet formulas, you need a simple app that shows your expense records clearly and automatically calculates key insights like total spending and average costs. This would help you understand your spending patterns at a glance.

##### **Project Setup**

Create a new file called `app.py`:

```python
import streamlit as st
import pandas as pd

st.title("Personal Expense Tracker")
st.write("Track and analyze your monthly spending")

# Sample expense data
data = {
    "Date": ["2024-09-01", "2024-09-02", "2024-09-05", "2024-09-08", "2024-09-12"],
    "Category": ["Food", "Transport", "Shopping", "Bills", "Food"],
    "Amount": [450, 120, 999, 2200, 300]
}

df = pd.DataFrame(data)

st.header("Expense Records")
st.dataframe(df)

# Calculate summary statistics
total_expense = df["Amount"].sum()
avg_expense = df["Amount"].mean()
max_expense = df["Amount"].max()

st.divider()

# Create summary table
summary_data = {
    "Metric": ["Total Spent", "Average Transaction", "Highest Expense"],
    "Value": [total_expense, f"{avg_expense:.2f}", max_expense]
}
summary_df = pd.DataFrame(summary_data)

st.subheader("Quick Reference Table")
st.table(summary_df)

```

**Run your app with:**

```bash
streamlit run app.py

```
##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%203/expense1mod3.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%203/expense2mod3.png">


----

#### **Step-by-Step Walkthrough**

Let's examine how each function contributes to effective data presentation:

- **pandas (pd)** is an open-source Python library widely used for data manipulation and analysis.

- **`pd.DataFrame(data)`**: Creates a structured data table from your dictionary. The keys become column headers, and the values become rows. 

- **`st.dataframe(df)`**: Displays the expense records in an interactive table where users can scroll horizontally/vertically, sort data by clicking column headers, and explore large datasets. Perfect for raw data exploration.

- **DataFrame calculations**: Methods like `df["Amount"].sum()`, `df["Amount"].mean()`, and `df["Amount"].max()` These are built-in pandas functions for performing common aggregations on data.

- **`st.table(pd.DataFrame(summary))`**: Creates a static table presenting summary statistics in fixed format. Unlike interactive dataframes, this provides quick reference without user interaction.


----

#### **Conclusion**

The combination of `st.dataframe()` and `st.table()` transforms raw data into accessible, professional displays that users can immediately understand and interact with. These fundamental display functions form the foundation of effective data communication in Streamlit applications, enabling you to present information clearly whether building analytical dashboards or simple data exploration tools.

----

### Topic 3.2: Metrics 

<br>

#### **Introduction**

When exploring data, sometimes raw tables or charts aren't enough—you need fast, digestible insights. That's where **metrics** come in. Streamlit's `st.metric()` is designed to highlight key performance indicators (KPIs) that answer users' first question: _"So, how am I doing right now?"_

A metric card is simple but powerful: it shows a label, a value, and a delta (the change compared to a previous value). `st.metric()` makes trends obvious at a glance by using green/red arrows to indicate positive or negative changes.

In data-driven apps, metrics provide immediate context and help users understand their progress without having to dig through complex visualizations or raw numbers.

#### **Mini Project**

You're building a personal fitness dashboard similar to what you'd see on a smartwatch or fitness app. The dashboard needs to display daily health metrics like steps, calories burned, and heart rate with clear indicators of whether you're improving or declining compared to yesterday.

##### **Project Setup**

Create a new file `app.py`:

```python
import streamlit as st
import random

st.title("🏋️ Fitness Dashboard")

# Generate mock fitness data
steps_today = 10500
steps_change = 800
calories_burned = 2200
calories_change = -150
heart_rate = 82
hr_change = -3

# Display the metrics
st.metric(label="🏃 Steps Today", value=f"{steps_today:,}", delta=steps_change)
st.metric(label="🔥 Calories Burned", value=f"{calories_burned} kcal", delta=f"{calories_change} kcal")
st.metric(label="💓 Average Heart Rate", value=f"{heart_rate} bpm", delta=f"{hr_change} bpm")
```

**Run your app with:**

```
streamlit run app.py
```

##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%203/metricmod3.png">


----

#### **Step-by-Step Walkthrough**

The `st.metric()` function takes three main parameters that create professional-looking KPI cards:

-   **`label`**: The title that describes what you're measuring. Use clear, concise descriptions with emojis to make them visually appealing.
    
-   **`value`**: The current measurement. You can format this as a string to include units (like "kcal" or "bpm") or use number formatting (like `:,` for comma separators in large numbers).
    
-   **`delta`**: The change from the previous period. Streamlit automatically colors this green for positive values and red for negative values, with arrows indicating the direction of change.
    

When you run this code, each `st.metric()` creates a card that displays the label at the top, the main value prominently in the center, and the delta change at the bottom with appropriate color coding. The delta parameter accepts both numbers and formatted strings, giving you flexibility in how you present the change information.

---


#### **Conclusion**

This function is the cornerstone of your Streamlit app, turning raw data into an impactful and easy-to-understand narrative. By providing context to your numbers, `st.metric()` helps your users immediately grasp the meaning behind their data and make informed decisions, all within a single, clean interface.

---

### Topic 3.1: JSON Viewer


<br>

#### **Introduction**

In data-driven applications, a lot of information arrives as raw **JSON (JavaScript Object Notation)**—a format that's efficient for machines but often a jumbled mess for humans to read. Whether you're fetching real-time data from an API or just working with structured files, understanding this raw data can be a challenge. 

Streamlit's `st.json()` function solves this problem by transforming unformatted JSON strings into a clean, interactive, and beautiful display. It automatically formats and color-codes your data, allowing users to expand and collapse nested objects to explore complex payloads with ease. This powerful tool is not only great for developers who need to debug API responses in real time, but also for building transparency with users by showing them the exact data your app is working with. 
`st.json()` turns a technical mess into a clear, explorable view, making your application more trustworthy and user-friendly.

#### **Mini Project**

A weekend hiker checking weather forecasts sees "partly cloudy, 22°C" but needs humidity details for gear decisions, while a meteorologist noticing unusual temperature readings requires access to raw API data to investigate sensor anomalies. You're building a weather data explorer that serves both users simultaneously—providing clean, actionable summaries for everyday decisions alongside complete JSON responses for technical analysis, demonstrating how the same dataset can be presented in multiple formats to meet different professional and personal needs.

##### **Project Setup**

Create a new file `app.py`:

```python
import streamlit as st

# Sample weather data (simulates API response)
weather_data = {
    "location": {"name": "Hyderabad", "region": "Telangana", "country": "India"},
    "current": {
        "temperature_c": 27,
        "humidity": 81,
        "condition": {"text": "Cloudy", "icon": "overcast"},
        "wind_kph": 8,
        "uv_index": 1,
    },
    "forecast": [
        {"date": "2025-09-12", "text": "Cloudy with light rain", "max_temp_c": 30, "min_temp_c": 24},
        {"date": "2025-09-13", "text": "Rainy", "max_temp_c": 29, "min_temp_c": 23},
    ],
}

st.title("🌤️ Weather Data Explorer")

# Display parsed summary
st.header("Current Weather")
current = weather_data["current"]
st.metric("Temperature", f"{current['temperature_c']}°C")
st.metric("Humidity", f"{current['humidity']}%")
st.write(f"Condition: {current['condition']['text']}")

# Display raw JSON
st.header("Raw API Data")
st.json(weather_data)

```

**Run your app with:**

```bash
streamlit run app.py

```

----

##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%203/weathermod3.png">

-----

#### **Step-by-Step Walkthrough**

- The `st.json()` function takes a single parameter—either a Python dictionary, list, or JSON string—and renders it in an interactive, formatted display.

- When you pass a Python dictionary (like our `weather_data`) to `st.json()`, Streamlit automatically converts it into a beautifully formatted JSON view. The rendered JSON includes syntax highlighting with different colors for keys, values, and data types, making it easy to read and understand the structure.

- The interactive nature of `st.json()` allows users to click on nested objects to expand or collapse them. For example, users can click on the "current" object to see all the weather details, or expand the "forecast" array to examine each day's data individually.

This function is particularly powerful when working with API responses because it preserves the exact structure and data types of the original JSON, letting users see boolean values, numbers, strings, and null values exactly as they appear in the API response.

---
#### **Key Learning Points**

- **Great for debugging:** `st.json()` is a quick way to inspect raw responses during development before transforming the data.

- **Lightweight alternative:** It avoids the overhead of creating tables or charts when the goal is simply to check structure.

- **Best for nested data:** Unlike `st.dataframe()`, it naturally handles deeply nested objects without flattening.

- **Not for presentation:** Ideal for debugging or inspection, but less suited for polished dashboards where summaries or charts may be more effective.

#### **Conclusion**

The `st.json()` function bridges the gap between raw data and a user-friendly display. While processed summaries help users quickly understand information, showing the raw JSON alongside them adds transparency. Users can see exactly what data your app received and how it’s being interpreted, making your application more credible while giving developers a powerful tool for debugging and verification.
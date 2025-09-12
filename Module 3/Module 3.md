# Module 3: Displaying & Exploring Data

## Topic 3.1: DataFrames & Tables 

----------

### **Introduction**

In today’s world, data isn’t just numbers—it’s the  **core of decisions, insights, and stories**. From tracking your monthly expenses to analyzing stock prices, good presentation can turn raw data into actionable knowledge.

Streamlit makes this process seamless: with just a few commands, you can  **display, sort, and analyze structured data**—without writing complex front-end code.

Think of a  **DataFrame**  as a  **digital spreadsheet inside your app**. It organizes data neatly into rows and columns, just like Excel or Google Sheets. Streamlit gives you two versatile tools here:

-   **`st.dataframe()`**  
    An  _interactive_  table where users can scroll horizontally/vertically, sort data, and explore large tables. It’s perfect for dynamic dashboards.
    
-   **`st.table()`**  
    A  _static_  snapshot of tabular data you want to show cleanly, without user interactivity—like fixed reports or summaries.
    

**Example Scenarios:**

-   A  **teacher**  showing student grades in a class spreadsheet.
    
-   A  **finance tracker**  showing income vs. expenses.
    
-   A  **sports app**  showing player stats with season averages.
    

**Pro Tip**: Always support large data with  `st.dataframe()`  so users can explore details, but highlight important numbers above or below with  `st.metric()`  to avoid mental math.

----------


### Mini Project: Personal Expense Tracker

Tracking expenses is a key step toward better money management. With Streamlit, we can quickly build a simple app that records expenses, shows insights, and summarizes spending patterns.

- Create a file `app.py`

```python
import streamlit as st
import pandas as pd

st.title("💰 Personal Expense Tracker")

data = {
    "Date": ["2025-09-01", "2025-09-02", "2025-09-05", "2025-09-08", "2025-09-12"],
    "Category": ["Food", "Transport", "Shopping", "Bills", "Food"],
    "Amount (₹)": [450, 120, 999, 2200, 300]
}
df = pd.DataFrame(data)


st.header("📊 Expense Log")
st.write("Here is the record of all your expenses:")
st.dataframe(df)

total_expense = df["Amount (₹)"].sum()
avg_expense = df["Amount (₹)"].mean()
max_expense = df["Amount (₹)"].max()

st.divider()
st.header("📈 Expense Summary")
st.subheader("Key Insights")
st.write(f"✅ **Total Expense**: ₹{total_expense}")
st.write(f"✅ **Average Expense**: ₹{avg_expense:.2f}")
st.write(f"✅ **Highest Expense**: ₹{max_expense}")

st.divider()

st.header("📋 Summary Table")
summary = {
    "Total": [total_expense],
    "Average": [avg_expense],
    "Highest": [max_expense]
}
st.table(pd.DataFrame(summary))

```

----
**Run the app**
- `streamlit run app.py`

----------

### Expected Output

When you run the app (`streamlit run app.py`), you’ll see:

-   A **title bar**: “💰 Personal Expense Tracker”.
    
-   An **Expense Log table** with all transactions listed (Date, Category, Amount).
    
-   A **summary section** showing:
    
    -   Total Expense → ₹4069
        
    -   Average Expense → ₹813.80
        
    -   Highest Expense → ₹2200
        
-   A **static summary table** displaying the same stats in tabular format (good for reports/exports).
    

----------

### Explanation

-   **`st.dataframe(df)`** → Displays the expense records in an interactive table.
    
-   **`df.sum()`, `df.mean()`, `df.max()`** → Used to calculate key statistics.
    
-   **`st.write()`** → Shows total, average, and highest expenses in a readable format.
    
-   **`st.table()`** → Presents a static version of the summary, useful for snapshots.
    
-   **`st.divider()`** → Adds clean horizontal breaks for better sectioning.
    

This app acts as a **basic personal finance dashboard**, helping users monitor spending patterns with just a few lines of Python.

---

## Topic 3.2: Metrics


### **Introduction**

When exploring data, sometimes  **raw tables or charts aren’t enough**—you need  _fast, digestible insights_. That’s where  **metrics**  come in.

Streamlit’s  `st.metric()`  is designed to highlight  _key performance indicators (KPIs)_, such as:

-   A runner’s  **daily steps count**
    
-   Your  **heart rate**  during a workout
    
-   The  **calories burned today vs yesterday**
    

A metric card is  **simple but powerful**: it shows a  _label_, a  _value_, and a  _delta_  (the change compared to a previous value).

For example:

-   **Steps (Today: 10,000, Delta: +800)**  → shows progress.
    
-   **Heart Rate (85 bpm, Delta: -5)**  → shows improvement in condition.
    

Just like a  **fitness tracker watch**  or a  **stock ticker**,  `st.metric()`  makes trends obvious at a glance by using green/red arrows.

In data-driven apps, metrics answer users’ first question:  _“So, how am I doing right now?”_

**Tip:**  Use metrics to spotlight the  _most important indicators_. Keep them concise, use meaningful labels, and always show trends (positive or negative changes) to give context.

----------
### **Mini Project: Fitness Dashboard**

Fitness apps and smartwatches often display **daily health metrics** like steps, calories, and heart rate in a simple dashboard. With Streamlit, we can simulate such a dashboard to keep track of personal health progress.

- Create a file `app.py`

```python
import streamlit as st
import random

# Page setup
st.set_page_config(page_title="🏋️ Fitness Dashboard", layout="centered")

st.title("🏋️ Fitness Dashboard")

st.divider()
# Mock/Simulated data
steps_today = random.randint(8000, 12000)
steps_change = random.randint(-500, 500)

calories_today = random.randint(1800, 2800)
calories_change = random.randint(-200, 200)

heart_rate = random.randint(70, 95)
hr_change = random.randint(-10, 10)

# Display metrics 
st.metric(label="🏃 Steps Today", value=f"{steps_today:,}", delta=f"{steps_change:+}")

st.metric(label="🔥 Calories Burned", value=f"{calories_today} kcal", delta=f"{calories_change:+} kcal")

st.metric(label="💓 Avg Heart Rate", value=f"{heart_rate} bpm", delta=f"{hr_change:+} bpm")

st.write("✅ Fitness Dashboard ready! Use it to track activity and progress daily.")

```

----------

### **Expected Output**

-   A **Steps metric card** with today’s count and delta (arrow showing + or -).
    
-   A **Calories metric card** showing calories burned and change from yesterday.
    
-   A **Heart rate metric card** showing average heart rate and variation.
    
-   All metrics are shown **stacked vertically** for a clean, scrollable layout.
    
----------

### **Explanation**

-   **`random.randint()`** → generates mock fitness data to simulate a tracker.
    
-   **`st.metric()`** → displays KPI-style cards with:
    
    -   `label` → what the metric is (Steps, Calories, Heart Rate).
        
    -   `value` → today’s reading.
        
    -   `delta` → change compared to the last reading (green for +, red for -).
        

---


## Topic 3.3: JSON Viewer

----------

### **Introduction**

In many data-driven applications, raw data often comes in the form of  **JSON (JavaScript Object Notation)**—a format that efficiently organizes data into nested objects and arrays. APIs, especially those fetching real-time information like weather, stock prices, or sensor data, usually return responses as JSON.

Streamlit’s  `st.json()`  function makes it easy to  **display JSON data in a readable, interactive format**  directly in your app. It formats and pretty-prints JSON content with indentation and syntax highlighting, so users can explore complex nested data effortlessly.

Key benefits of using  `st.json()`:

-   Converts raw JSON strings or Python dictionaries/lists to a structured, collapsible view.
    
-   Enables users to expand or collapse nested objects for better clarity.
    
-   No extra frontend code or libraries needed to display complex JSON.
    

This is especially useful for developers, data analysts, or users debugging/understanding API responses in real time.

**Pro Tip:**  Use  `st.json()`  to display full API payloads or response samples alongside your parsed or processed data. It builds transparency and trust by letting users see the exact raw data the app is working with.

----------


### **Mini Project: Weather Data Explorer**

Weather apps usually show users a **clean summary** of conditions but also rely on raw JSON data fetched from APIs in the background. In this mini project, we’ll create a **Weather Data Explorer** that displays both the **human-readable summary** (location, temperature, humidity, forecast) and the **raw JSON data** for developers.

- Create a file `app.py`

```python
import streamlit as st 

# Sample weather JSON-like data (in real apps, this comes from API responses)
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
        {"date": "2025-09-12", "text": "Cloudy, a little rain", "max_temp_c": 30, "min_temp_c": 24},
        {"date": "2025-09-13", "text": "Cloudy, rain", "max_temp_c": 29, "min_temp_c": 23},
        {"date": "2025-09-14", "text": "Humid with a little rain", "max_temp_c": 31, "min_temp_c": 25},
    ],
}

st.title("🌤️ Weather Data Explorer")

# Location section
st.header("📍 Location")
loc = weather_data["location"]
st.write(f"{loc['name']}, {loc['region']}, {loc['country']}")

# Current conditions
st.header("🌡️ Current Conditions")
current = weather_data["current"]
st.metric("Temperature (°C)", current["temperature_c"])
st.metric("Humidity (%)", current["humidity"])
st.metric("UV Index", current["uv_index"])
st.write(f"Condition: {current['condition']['text']}")
st.write(f"Wind Speed: {current['wind_kph']} kph")

# Forecast
st.header("📅 Forecast")
for day in weather_data["forecast"]:
    st.write(f"**{day['date']}**: {day['text']} (Max: {day['max_temp_c']}°C, Min: {day['min_temp_c']}°C)")

st.divider()

# Raw JSON data
st.header("🗂️ Raw JSON Data")
st.json(weather_data)

```
----

**Run the app**
- `streamlit run app.py`
----------

### **Expected Output**


    

----------

### **Explanation**

-   **`st.metric()`** → Shows key KPIs like temperature, humidity, UV index.
    
-   **`st.write()`** → Displays descriptive text (condition, wind speed, forecast).
    
-   **`for` loop** → Iterates through forecast list and prints daily summaries.
    
-   **`st.json()`** → Renders the full raw data in a structured, interactive format.
    

This setup is useful because it **balances end-user readability** (summary cards, plain text) with **developer transparency** (raw JSON view).
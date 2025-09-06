
# Module 4: Displaying & Exploring Data in Streamlit

**Introduction**  
Data powers decisions, insights, and stories in every modern application. Streamlit makes it effortless to  **show, analyze, and summarize**  data so that users can interact—no advanced front-end coding required. Whether you’re dealing with student grades, crypto prices, or budget sheets, Streamlit helps you turn raw data into useful information and clear visuals.

----------

### Topic 4.1: DataFrames & Tables 

**Introduction**  
Think of a  **DataFrame**  as a digital spreadsheet—like having Excel right inside your Python app. It lets you organize data in rows and columns for everything from grades to sales to survey responses. In Streamlit,

-   `st.dataframe()`  displays data interactively: users can scroll, sort, and even search in the table, turning raw figures into understandable patterns.
    
-   `st.table()`  shows a static, nicely formatted version for simpler needs.
    
This approach brings clarity: instead of scanning plain lists, users see well-structured tables that reveal trends and individual details at a glance.

**Tip:** 
Add summary boxes (using  `st.metric()`) to highlight important figures, such as averages or totals, so users don’t have to calculate them manually. This makes dashboards both detailed and user-friendly.

### Mini Project: Student Grad Book Viewer

Let's build digital gradebook that shows student grades in a neatly formatted table, plus an average grade summary—just like a classroom spreadsheet.

**Code**
```
import streamlit as st
import pandas as pd

st.title("Student Gradebook Viewer 📘")

# Mock dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Grade": [85, 92, 78, 88, 95]
}

df = pd.DataFrame(data)

# Display the table
st.subheader("Gradebook")
st.dataframe(df)

# Show average grade
average_grade = df["Grade"].mean()
st.metric("Class Average", f"{average_grade:.2f}")
```

**Expected Output**

- A neat, interactive table showing student names and grades.

- A metric card displaying the class average.

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%204/studentgradbook.png">

**Key Takeaways**

- Use st.dataframe() for interactive tables.

- Use st.metric() to highlight key numbers (like averages).

- Perfect for dashboards where users want both detail and summary.
----------

### Topic 4.2: JSON & Metrics 

**Introduction**  
APIs are the bridges between your app and the outside world, and  **JSON**  is the language they speak—like electronic “menus” where you order information and receive just what you need.

-   Streamlit can display  **live metrics**  (e.g., prices, scores, key performance indicators) in eye-catching labels using  `st.metric()`.
    
-   When data updates, you get instant visual feedback (red/green delta arrows)—just like watching stock tickers or scoreboards.
    

By bringing JSON and metric visualization together, Streamlit makes real-time dashboards easy for beginners, and powerful for advanced users. You can even practice with mocked data before integrating real APIs, lowering the barrier to entry for learning.

**Tip:**  
Use metrics to highlight what matters most, and always clarify trends (is it up or down?), so users interpret numbers with confidence.

### Mini Project: Crypto Price Monitor

Let`s build a simple crypto dashboard that fetches (or simulates) live Bitcoin prices and displays them with up/down changes in a KPI card—think stock ticker, but for cryptocurrency.

**Code**

```python
import streamlit as st
import random

st.title("Crypto Price Monitor 💰")

# Mock data (instead of API to keep it simple for beginners)
price = random.uniform(25000, 30000)  # Random Bitcoin price
change = random.uniform(-500, 500)    # Random change

st.metric(label="Bitcoin Price (USD)", value=f"${price:,.2f}", delta=f"{change:+.2f}")
```

**Expected Output**

- A metric card showing Bitcoin’s price in USD.

- A delta arrow showing if the price went up or down.

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%204/crypto_price.png">

**Key Takeaways**

- JSON is a common format for API data.

- st.metric() is ideal for showing prices, KPIs, and changes.

- You can mock data for practice before connecting real APIs.

----------

### Topic 4.3: File Upload & Preview 

**Introduction**  
Letting users upload their own data transforms your app into a  **personal workspace**—like importing an expense sheet to analyze spending or loading a dataset for research.

-   Streamlit’s  `st.file_uploader()`  enables drag-and-drop or selection of files (CSV, Excel, etc.) for instant, secure upload.
    
-   With Pandas, you can preview results (using  `df.head()`), summarize key metrics, and provide feedback—all on the fly.
    

This functionality empowers users: instead of just viewing generic samples, they can see insights tailored to their own unique data. Adding metrics (like total expenses or savings) makes numbers actionable, helping users draw conclusions and plan next steps.

**Tip:**  
Clearly specify expected file formats and column names so users aren’t confused. Use friendly warnings or guidance if data is missing or not quite right—building confidence and reducing friction.

### Mini Project: Budget Tracker

Let's build an expense tracker that lets users upload a CSV file of their monthly budget, previews the data, and summarizes total spending—just like a personal finance dashboard.

**Code**

```python
import streamlit as st
import pandas as pd

st.title("Budget Tracker 💸")

uploaded_file = st.file_uploader("Upload your expense CSV", type="csv")

if uploaded_file is not None:
    # Load CSV into DataFrame
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Preview of Your Expenses")
    st.dataframe(df.head())  # Show first few rows
    
    # Calculate total expenses
    if "Amount" in df.columns:
        total_expenses = df["Amount"].sum()
        st.metric("Total Expenses", f"${total_expenses:,.2f}")
    else:
        st.warning("Your CSV should have a column named 'Amount'.")
```

**Expected Output**

- File uploader where user selects a CSV file.

- Preview table of the first few rows.

- A total expenses metric displayed if the file has an Amount column.

<img src ="https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%204/budget_tracker.png">

**Key Takeaways**

- st.file_uploader() makes your app dynamic — users bring their own data.

- Use Pandas to preview and summarize uploaded data.

- Adding simple metrics (like totals) turns raw data into useful insights.
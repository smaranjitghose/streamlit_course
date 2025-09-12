# Module 1: Getting Started with Streamlit

### Topic 1.1: Introduction 

#### **What is Streamlit ?**

Imagine you want to share a cool data analysis you did in Python with your colleagues, but they don't know how to run Python code. Streamlit is the answer! It's a Python library that lets you turn your Python scripts into interactive web applications with just a few lines of code. Think of it as a bridge between your Python code and a user-friendly web interface.

#### **Why Use Streamlit?**

-   **Simplicity:** Streamlit is incredibly easy to learn and use, even if you have limited web development experience.
    
-   **Rapid Prototyping:** Build and iterate on your web apps quickly. Streamlit's hot-reloading feature automatically updates your app whenever you save your code.
    
-   **Python-Centric:** Write your entire application in Python. No need to learn HTML, CSS, or JavaScript.
    
-   **Interactive:** Easily add interactive widgets like sliders, buttons, and text inputs to your apps.
    
-   **Data Visualization:** Streamlit integrates seamlessly with popular data visualization libraries like Matplotlib, Seaborn, and Plotly.
    
<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/module1.png" alt="Features of Streamlit" style="width: 500px; height: auto;" />


#### **Traditional Approach vs. Streamlit:**

| Feature               | Traditional Web Dev (Flask/Django + Frontend) | Streamlit                         |
| --------------------- | --------------------------------------------- | --------------------------------- |
| **Learning Curve**    | Requires HTML, CSS, JS, plus backend skills   | Pure Python                       |
| **Development Speed** | Slow, more boilerplate                        | Very fast, minimal code           |
| **Prototyping**       | Takes days/weeks                              | Minutes                           |
| **Focus**             | Split between frontend + backend + deployment | Purely on Python and logic        |
| **Use Case**          | Full production apps                          | Data apps, dashboards, prototypes |


If your goal is data exploration, dashboards, reporting, or ML model demos, Streamlit is much faster and simpler than the traditional stack.

---
### Topic 1.2: Setup

#### **Setting Up Your First Streamlit Project**

When starting any new Python project, it’s best practice to keep dependencies isolated.
With uv (a fast and reliable Python package/dependency manager), you can quickly set up a clean environment and start building.

---

##### **Step 1: Create a new directory**

```
mkdir streamlit-app
cd streamlit-app
```
----

##### **Step 2: Initialize uv in your project**

```
uv init

```

<img src ="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/43tfadctp/content/43waq8uyt/uvinit.png" width=400>

---

- It does not automatically create a `.venv/` folder until you add your first dependency (uv add streamlit)
---

##### **Step 2: Install Streamlit**

```
uv add streamlit
```


<img src ="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/43tfadctp/content/43waq8uyt/installstreamlit.png" width=700>

---

<img src= "https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/43tfadctp/content/43waq8uyt/foldervenv.png" width =400 height=200 >

---

- This will create a `.venv/` folder

----
##### **Step 4: Activate the Virtual environment**

```
.venv\Scripts\Activate.ps1

```
---

##### **Step 5: Start your App**


```
streamlit hello
```

This launches Streamlit’s built-in demo app in your browser. 🎉


##### **Expected Output**


![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/43tfadctp/content/43waq8uyt/defaultstreamlit.png)


 
---
### Topic 1.3: Build your First Project


#### **Building a Random Quote App:**

Let's create a more interesting app that displays a random quote each time the page is refreshed. First, we need a list of quotes.
- Create a file `app.py`

```python
import streamlit as st
import random

quotes = [
    "The best way to predict the future is to invent it.",
    "Simplicity is the soul of efficiency.",
    "Do one thing every day that scares you.",
    "Code is like humor. When you have to explain it, it’s bad."
]

st.title("Daily Quote Board")
st.write("Refresh the page for a new dose of inspiration!")

quote = random.choice(quotes)
st.write(quote)

```
---

**Running the App**

- Save as `app.py`

- Run with:
  ```
  streamlit run app.py
  ```

---

**Browser opens showing:**

Title “Daily Quote Board”

Message about refreshing

A randomly chosen quote displayed in a highlighted box.

---

**Expected Output:**

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/dailyquote.png">
    

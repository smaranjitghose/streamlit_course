# Module 1: Getting Started with Streamlit

### Topic 1.1: Introduction 


#### **What is Streamlit?**

You’re a data scientist who’s just finished analyzing sales trends for the year. The insights are crucial—knowing which regions performed best, which months saw spikes, and where opportunities lie for the next quarter. But how do you make this information truly accessible?
Instead of emailing yet another static report, you fire up Streamlit. With just Python, you build a web application.
That’s what Streamlit is: an open-source Python library for building interactive web application, dashboards, and reporting tools in pure Python. It lets technical teams—and anyone with Python know-how to bring their data, models, and analysis to life for everyone.

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%201/whatissysdes1.png">



#### **Why Streamlit is Perfect for Data Professionals**

Streamlit was built for data scientists, analysts, and researchers who want to share their work without becoming web developers:

**Pure Python Simplicity**: Write everything in Python. No HTML, CSS, or JavaScript required.

**Lightning-Fast Development**: Build interactive dashboards in minutes. Streamlit updates your app instantly when you save your file.

**Data-First Design**: Works seamlessly with Pandas, Matplotlib, Plotly, and Scikit-learn.

**Interactive by Default**: Built-in widgets like sliders and dropdowns make your data interactive without complex coding.

----

#### **The Streamlit Advantage**

While building a web application can take weeks with traditional methods, Streamlit allows you to create one in a matter of minutes.

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%201/tradvsstreamlit1.png">


#### **How Streamlit Works**

Streamlit follows a simple philosophy: your app is just a Python script that runs from top to bottom. When users interact with your app, Streamlit reruns your script with the new values.

**Basic flow:**

1. A Python script is created using Streamlit functions.

2. The script is executed, which launches the Streamlit application.

3. The application opens in a web browser.

4. Users interact with the app through the web interface.

5. Each interaction automatically updates the display to reflect changes.


#### **When to Choose Streamlit**

**Perfect for**:

-   Data exploration and visualization apps
-   Machine learning model demos
-   Interactive dashboards and reports
-   Proof-of-concept applications

**Not ideal for**:

-   Complex multi-user applications
-   Apps requiring extensive custom styling
-   High-performance application

#### **What's Next?**

In the following chapters, you'll build increasingly sophisticated applications through hands-on projects. We'll start with basic text and formatting, then progress to data visualization, user inputs, and interactive dashboards.





### Topic 1.2: Setup 


<br>

##### **Prerequisites**

- Ensure the latest version of [**Python**](https://www.python.org/downloads/) is installed.

- Ensure [UV](https://docs.astral.sh/uv/getting-started/installation/) is installed.


##### **Setting Up Your First Streamlit Project**

---

**1. Create a new directory**

`mkdir streamlit-app`

---

**2. Change to the working Directory**

`cd streamlit-app`

----

**3. Initialize uv in your project**

`uv init`


<img src ="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%201/uvinit.png" width=400>

---

- It does not automatically create a `.venv/` folder until you add your first dependency
---

**4. Install Streamlit**

`uv add streamlit`


<img src ="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%201/installstreamlit.png" width=700>

---

- This will create a `.venv/` folder


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%201/foldervenv1.png">


----

**5. Activate the Virtual environment**

----

- **On Linux/Mac:**

  `source .venv/bin/activate`


- **On Windows (PowerShell):**

  `.venv\Scripts\Activate.ps1`

---

**6. Start your App**

`streamlit hello`

This launches Streamlit’s built-in demo app in your browser. 🎉


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%201/defaultstreamlit.png">

---
 Congratulations🎉! You have successfully run your first Streamlit project.



 
### Topic 1.3: First Streamlit Project 


<br>

#### **Introduction**

The best way to learn Streamlit is by building simple, hands-on projects. Small projects allow you to see immediate results and understand how different functions work together, giving you confidence to tackle bigger challenges. In this chapter, we'll create your very first Streamlit project from scratch. The goal isn't complexity—it's understanding the fundamental workflow: writing Python code, running it with Streamlit, and watching it come alive in your browser.

---

#### **Mini Project**

Your remote tech team, "FlowState Labs", is starting its daily 9 AM standup feeling groggy and uninspired. Everyone is logging in, but the energy is low, and you need a way to get the team mentally aligned and motivated before diving into the day's tasks.
Your team lead proposes a solution "The Morning Ritual," a custom web app that acts as your team's digital campfire. Each day, the app presents a new, inspiring quote, sparking a brief, engaging conversation that energizes the team and sets a positive tone for the day.

##### **Project Setup**

Create a new file `app.py`:

```python
import streamlit as st
import random

# List of inspiring quotes
quotes = [
    '"🌱 The best way to predict the future is to invent it."',
    '"⚡ Simplicity is the soul of efficiency."', 
    '"🔥 Do one thing every day that scares you."',
    '"💻 Code is like humor. When you have to explain it, it is bad "',
    '"🌟 Great things never come from comfort zones."',
    '"🚀 Stay hungry, stay foolish."'
]

st.title("☕ The Morning Ritual")
st.write("Welcome to FlowState Labs' digital campfire. Let's start our day with some inspiration!")

# Pick a random quote
quote = random.choice(quotes)

# Display the daily quote
st.write("💡 Today's Quote")
st.subheader(quote)

# Fun extra: prompt for team reflection
st.write("💬 What does this quote mean to you? Share your thoughts with the team!")

```

**Now run your app:**

```bash
streamlit run app.py

```
----

##### **Output**

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%201/quotemod1tldraw.png">


----

#### **Step-by-Step Walkthrough**

Let's break down what each part of your code accomplishes:

- **`import streamlit as st`**: It is the standard way to import the Streamlit library, allowing you to use its functions by typing `st.` followed by the function name.

- **`import random`**: We're using Python's built-in module, here it is used to randomly select a quote from the list. This shows how Streamlit easily integrates with any Python library.

- **`quotes = [...]`**: This is just regular Python—a list containing our motivational quotes. Nothing Streamlit-specific here, which demonstrates how your existing Python knowledge transfers directly.

- **`st.title("☕ The Morning Ritual")`**: Your first Streamlit function! This creates a large, prominent heading at the top of your app. The emoji adds visual appeal without any complex styling.

- **`st.write("Welcome to FlowState ...")`**: This displays regular text below your title. `st.write()` is incredibly versatile—it can display text, dataframes, charts, and more.

- **`quote = random.choice(quotes)`**: Pure Python logic that picks a random quote from your list. This happens every time someone loads or refreshes your app.

- **`st.subheader(quote)`**: This displays your random quote as a medium-sized heading, making it stand out as the main content of your page.

---

##### **What happens when you run `streamlit run app.py`**

-   To start a Streamlit project, run the command:
    
    `streamlit run app.py` 
    
    _(Here, `app.py` is your project file.)_
    
-   Once executed, Streamlit automatically starts a **local server** on your computer.
    
-   By default, this server runs at the address:
    
    `http://localhost:8501` 
    
-   You can open this URL in your web browser to view and interact with your app.
    
-   Other devices on the same Wi-Fi network can access your app using the **Network URL** (e.g., `http://192.168.1.70:8501`).
    
-   When you deploy, the `localhost` is replaced with a **public URL** (e.g., Streamlit Cloud).


---

#### **Key Learning Points**

-   **Python-first development**: Your Streamlit app is just a Python script that runs from top to bottom. No special web development knowledge required.
   
-   **Automatic reactivity**: Every time someone interacts with your app (like refreshing the page), Streamlit reruns your script and updates the display.

-   **Instant visual feedback**: Functions like `st.title()` and `st.write()` immediately create visual elements in your browser, making development feel magical.


#### **Conclusion**

Congratulations, you've built your first Streamlit app! What you've created is a perfect example of Streamlit's core power: turning simple Python scripts into interactive web application instantly. 
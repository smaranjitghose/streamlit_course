# Module 1: Getting Started with Streamlit

### Topic 1.1: Introduction & Setup

#### **What is Streamlit ?**

Imagine you want to share a cool data analysis you did in Python with your colleagues, but they don't know how to run Python code. Streamlit is the answer! It's a Python library that lets you turn your Python scripts into interactive web applications with just a few lines of code. Think of it as a bridge between your Python code and a user-friendly web interface.

#### **Why Use Streamlit?**

-   **Simplicity:** Streamlit is incredibly easy to learn and use, even if you have limited web development experience.
    
-   **Rapid Prototyping:** Build and iterate on your web apps quickly. Streamlit's hot-reloading feature automatically updates your app whenever you save your code.
    
-   **Python-Centric:** Write your entire application in Python. No need to learn HTML, CSS, or JavaScript.
    
-   **Interactive:** Easily add interactive widgets like sliders, buttons, and text inputs to your apps.
    
-   **Data Visualization:** Streamlit integrates seamlessly with popular data visualization libraries like Matplotlib, Seaborn, and Plotly.
    
<img src=".\image\Module 1\module1.png" alt="Features of Streamlit" style="width: 500px; height: auto;" />

#### **Traditional Approach vs. Streamlit:**

Traditionally, creating web apps required knowledge of front-end technologies (HTML, CSS, JavaScript) and back-end frameworks (Flask, Django). Streamlit simplifies this process by handling the front-end complexity, allowing you to focus on the Python logic.

**Installation:**

Before you start, make sure you have Python installed (version 3.8 or higher is recommended). Open your terminal or command prompt and install Streamlit using pip:

```bash
pip install streamlit

```

**Hello, World! Demo:**

Let's create a simple "Hello, World!" Streamlit app. Create a new Python file named `hello.py` and add the following code:

```python
import streamlit as st

st.title("My First Streamlit App")
st.write("Hello, World!")

```

Save the file. Now, run the app from your terminal:

```bash
streamlit run hello.py

```

This command will launch your app in your default web browser. You should see a page with the title "My First Streamlit App" and the text "Hello, World!".

**Expected Output:**

The browser window will display the following:

-   Title: My First Streamlit App
    
-   Content: Hello, World!
    

(A screenshot of the "Hello, World!" app would appear here)

**Hands-on Exercise:**

1.  Modify the `hello.py` file to display your name instead of "Hello, World!".
    
2.  Add a subtitle to your app using `st.subheader()`.
    

**Key Takeaways:**

-   Streamlit is a Python library for creating interactive web apps.
    
-   It simplifies web development by handling the front-end complexity.
    
-   You can install Streamlit using `pip install streamlit`.
    
-   The `streamlit run` command launches your app in a web browser.

---
### Topic 1.2: Running Streamlit Apps


**The** `streamlit run` **Command:**

As you've seen, the `streamlit run` command is used to launch your Streamlit apps. It takes the path to your Python script as an argument.

```bash
streamlit run your_app.py

```

**Browser Workflow:**

When you run a Streamlit app, Streamlit starts a local web server and opens your app in your default web browser. Any changes you make to your Python code will automatically be reflected in the browser after you save the file. This is called "hot reloading" and it's a huge time-saver.

**Localhost URL:**

Streamlit apps typically run on `localhost` (also known as `127.0.0.1`) on a specific port (usually 8501). You can access your app by navigating to `http://localhost:8501` in your web browser. The terminal output after running `streamlit run` will show the exact URL.
    

**Key Takeaways:**

-   `streamlit run` starts a local web server and opens your app in a browser.
    
-   Streamlit uses hot reloading to automatically update your app when you save changes.
    
-   Apps are typically accessible at `http://localhost:8501`.
    
---
### Topic 1.2: Daily Quote Board

#### **Building a Random Quote App:**

Let's create a more interesting app that displays a random quote each time the page is refreshed. First, we need a list of quotes.

```python
import streamlit as st
import random

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Strive not to be a success, but rather to be of value. - Albert Einstein",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Tell me and I forget. Teach me and I remember. Involve me and I learn. - Benjamin Franklin",
    "Be the change that you wish to see in the world. - Mahatma Gandhi"
]

st.title("Daily Quote")

quote = random.choice(quotes)
st.write(quote)

```

Save this code as `quote_app.py` and run it using `streamlit run quote_app.py`.

**Running the App:**

When you run the app, Streamlit will display a random quote from the list. Refresh the page to see a different quote.

**Expected Output:**

The browser window will display the following:

-   Title: Daily Quote
    
-   Content: A random quote from the list.
    

(A screenshot of the Daily Quote app would appear here)

**Interactivity Basics:**

Let's add a button to generate a new quote. We'll use the `st.button()` function.

```python
import streamlit as st
import random

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Strive not to be a success, but rather to be of value. - Albert Einstein",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart. - Helen Keller",
    "Be the change that you wish to see in the world. - Mahatma Gandhi"
]

st.title("Daily Quote")

if st.button("Get New Quote"):
    quote = random.choice(quotes)
    st.write(quote)
else:
    st.write("Click the button to see a quote!")

```

Now, the app will only display a quote when you click the "Get New Quote" button.

**Expected Output:**

Initially, the browser window will display:

-   Title: Daily Quote
    
-   Content: Click the button to see a quote!
    

After clicking the "Get New Quote" button, a random quote will be displayed.

(A screenshot of the Daily Quote app with the button would appear here)
    

**Key Takeaways:**

-   You can display text and data using `st.write()`.
    
-   `st.button()` creates an interactive button.
    
-   Streamlit apps automatically re-run when the code changes or a widget is interacted with.

---
### Topic 1.4: Custom News Page

**Page Configuration:**

Let's create a custom news page with a title, icon, and layout. We can configure the page using `st.set_page_config()`.

```python
import streamlit as st

st.set_page_config(
    page_title="My Awesome News Page",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Welcome to My Awesome News Page!")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top Stories")
    st.write("- Story 1: Streamlit makes Python apps easy!")
    st.write("- Story 2: Data Science trends in 2025")

with col2:
    st.subheader("Weather Update")
    st.write("☀️ Sunny, 32°C")
```

**Titles and Icons:**

-   `page_title`: Sets the title that appears in the browser tab.
    
-   `page_icon`: Sets the icon that appears in the browser tab. You can use emojis or URLs to image files.
    

**Layouts:**

-   `layout="wide"`: Makes the app full width


(A screenshot of the Custom News Page app with the button would appear here)

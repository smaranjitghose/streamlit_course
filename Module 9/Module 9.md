# Module 9: Managing State & Performance

### Topic 9.1: Session State (single page)

<br>

#### **Introduction**

Imagine filling out a long form online, getting halfway through, and then accidentally hitting a button that makes everything disappear—you'd have to start over from scratch. This frustrating experience happens in basic Streamlit apps because, by default, the entire script reruns with every user interaction, resetting all variables to their initial values. While this stateless behavior keeps apps simple and predictable, real-world applications often need to remember information across interactions—like maintaining user preferences, tracking accumulated calculations, or preserving data between different interface actions.
Streamlit's `st.session_state` solves this memory problem by providing persistent storage that survives script reruns, enabling stateful applications that can accumulate and maintain data over multiple user interactions. Session state works as a dictionary-like object where you can store any Python data type and access them throughout your application, creating sophisticated user experiences that handle complex workflows while maintaining consistency across interactions.

#### **Mini Project**

Jake is shopping online for his home office setup, carefully selecting a desk, chair, and accessories across multiple product pages, but every time he navigates back to browse more items, his cart empties and he has to start over. He's frustrated by losing his selections and having to remember what he already picked, especially when he wants to compare different combinations of items or remove something he's changed his mind about.
An online store with persistent cart functionality would let Jake build up his order gradually, make changes as he shops, and maintain his selections throughout his entire browsing session without losing progress.

##### **Project Setup**

Create a new file `app.py`:

```python
import streamlit as st

st.title("🛍️ Online Store")

# Initialize session state for cart
if 'cart' not in st.session_state:
    st.session_state.cart = []

# Available products
products = {
    "Laptop": 25000,
    "Mouse": 349,
    "Keyboard": 499,
    "Monitor": 7999,
    "Headphones": 799
}

# Product selection form
with st.form("add_product_form"):
    st.subheader("Add Product to Cart")
    selected_product = st.selectbox("Choose a product:", list(products.keys()))
    quantity = st.number_input("Quantity:", min_value=1, max_value=10, value=1)
    
    if st.form_submit_button("Add to Cart"):
        item = {
            "name": selected_product,
            "price": products[selected_product],
            "quantity": quantity,
            "total": products[selected_product] * quantity
        }
        st.session_state.cart.append(item)
        st.success(f"Added {quantity}x {selected_product} to cart!")

# Display cart
st.subheader("Shopping Cart")
if st.session_state.cart:
    for i, item in enumerate(st.session_state.cart):
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
        with col1:
            st.write(f"{item['name']}")
        with col2:
            st.write(f"₹{item['price']}")
        with col3:
            st.write(f"Qty: {item['quantity']}")
        with col4:
            if st.button("Remove", key=f"remove_{i}"):
                st.session_state.cart.pop(i)
                st.rerun()
    
    # Cart total
    total_cost = sum(item['total'] for item in st.session_state.cart)
    st.subheader(f"Total: ₹{total_cost}")
    
    # Clear cart button
    if st.button("Clear Cart"):
        st.session_state.cart = []
        st.rerun()
else:
    st.write("Your cart is empty")

```

**Run your app with:**

```
streamlit run app.py

```

##### **Output**

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%209/mod9cart1.png">

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%209/mod9cart2.png">

---

#### **Step-by-Step Walkthrough**


-   **`st.session_state`:**
    
    -   A special Streamlit dictionary that **persists values across app reruns**.
        
    -   Normally, Streamlit reruns the entire script on any user interaction, which would reset normal variables.
        
    -   Using `st.session_state`, data like the shopping cart can **persist across interactions**.
        
    -   In this project, `st.session_state.cart` stores all cart items to prevent them from being lost when the app reruns.
        
-   **Initialize session state for cart:**
    
    -   Checks if `'cart'` exists in `st.session_state`.
        
    -   If not, creates an empty list: `st.session_state.cart = []`.
        
    -   Ensures the cart is ready for storing items on first load.
        
-   **App title and product list:**
    
    -   `st.title("🛍️ Online Store")` displays the title.
        
    -   Defines a dictionary `products` with available products and their prices.
        
-   **Product selection form (`st.form`):**
    
    -   Groups the product dropdown (`st.selectbox`) and quantity input (`st.number_input`).
        
    -   Prevents the app from rerunning until the user clicks **"Add to Cart"**.
        
    -   Provides smoother UX by allowing users to adjust inputs without triggering premature updates.
        
-   **Adding items to the cart:**
    
    -   When the form is submitted:
        
        -   Creates a dictionary with `name`, `price`, `quantity`, and `total`.
            
        -   Appends the dictionary to `st.session_state.cart`.
            
        -   Displays a `st.success()` message confirming the addition.
            
    -   This allows multiple items to accumulate in the cart while maintaining their details.
        
-   **Displaying the cart:**
    
    -   Iterates through `st.session_state.cart`.
        
    -   Uses `st.columns` to neatly display: product name, price, quantity, and a remove button.
        
    -   Each remove button has a unique `key` to prevent interface conflicts.
        
-   **Removing items from the cart:**
    
    -   Clicking a remove button pops the corresponding item from the cart.
        
    -   Calls `st.rerun()` to immediately refresh the display and reflect the removal.
        
-   **Calculating and displaying total cost:**
    
    -   Sums the `total` value of all items in the cart.
        
    -   Displays the result using `st.subheader()`.
        
-   **Clearing the entire cart:**
    
    -   Clicking **"Clear Cart"** empties `st.session_state.cart`.
        
    -   `st.rerun()` ensures the UI updates immediately to show an empty cart.
        
-   **Handling an empty cart:**
    
    -   If `st.session_state.cart` is empty, displays `"Your cart is empty"`.
        
    -   Keeps the interface informative when no items have been added yet.

#### **Conclusion**

State management patterns transform stateless web frameworks into platforms capable of building persistent applications that maintain user context across interactions. These techniques enable developers to create seamless user experiences for complex workflows, from multi-step processes to interactive data pipelines that accumulate information over time. Mastering state persistence opens the door to creating applications that remember user preferences, track progress, and provide continuity across sessions—essential capabilities for any serious web application.

-------

### Topic 9.2: Multi-page Session State Management

----

#### **Introduction**

Consider an e-commerce application where users browse products on one page, add items to their cart on another, and proceed to checkout on a third page. Without proper state management, users would lose their cart contents every time they navigate between pages, forcing them to repeatedly add the same items or abandon their purchase entirely. This fragmented experience breaks user expectations and creates significant barriers to completing multi-step processes. Streamlit's session state solves this cross-page persistence challenge by automatically maintaining user context across all pages in your application.
Session state in Streamlit works seamlessly across page navigation, enabling sophisticated application flows like user authentication systems, multi-step wizards, or personalized experiences where each page can access and modify shared data. This capability allows developers to build cohesive applications that feel integrated and stateful rather than disconnected collections of individual tools, creating smooth user experiences that maintain context throughout the entire application journey.

#### **Mini Project**

Maria is using her company's project management app, but every time she clicks between the dashboard, reports, and settings pages, she gets kicked back to the login screen and has to enter her credentials again. This constant re-authentication interrupts her workflow and wastes time, especially during busy days when she needs to quickly jump between different sections to update projects and check team progress.
A multi-page application with persistent authentication would let Maria log in once and seamlessly navigate between all sections without losing her session, keeping her workflow smooth and uninterrupted.

##### **Project Setup**

Create the following file structure:
```
app/
├── main.py
├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_Reports.py
│   └── 3_Settings.py

```

**main.py** (Login page):
```python
import streamlit as st

st.title("Login Page")

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# Show login form if not logged in
if not st.session_state.logged_in:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Simple authentication rule
        if username and password == "demo":
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Welcome, {username}!")
            st.switch_page("pages/1_Dashboard.py")
        else:
            st.error("Invalid credentials. Hint: password is 'demo'")

# If already logged in
else:
    st.success(f"Already logged in as: {st.session_state.username}")
    if st.button("Go to Dashboard"):
        st.switch_page("pages/1_Dashboard.py")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

```

**pages/1_Dashboard.py**:

```python
import streamlit as st

st.title("📊 Dashboard")

# Authentication check
if not st.session_state.get("logged_in", False):
    st.warning("Please log in first!")
    st.switch_page("main.py")

st.success(f"Hello, {st.session_state.username}! Welcome to your dashboard.")

# Navigation
if st.button("Go to Reports"):
    st.switch_page("pages/2_Reports.py")
if st.button("Go to Settings"):
    st.switch_page("pages/3_Settings.py")

# Logout
if st.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.switch_page("main.py")

```

**pages/2_Reports.py**

```python

import streamlit as st

st.title("📑 Reports")

# Authentication check
if not st.session_state.get("logged_in", False):
    st.warning("Please log in first!")
    st.switch_page("main.py")

st.write(f"{st.session_state.username}, here are your project reports.")

# Navigation
if st.button("Go to Dashboard"):
    st.switch_page("pages/1_Dashboard.py")
if st.button("Go to Settings"):
    st.switch_page("pages/3_Settings.py")

# Logout
if st.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.switch_page("main.py")

```
**pages/3_Settings.py**

```python

import streamlit as st

st.title("⚙️ Settings")

# Authentication check
if not st.session_state.get("logged_in", False):
    st.warning("Please log in first!")
    st.switch_page("main.py")

st.write(f"{st.session_state.username}, you can update your settings here.")

# Navigation
if st.button("Go to Dashboard"):
    st.switch_page("pages/1_Dashboard.py")
if st.button("Go to Reports"):
    st.switch_page("pages/2_Reports.py")

# Logout
if st.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.switch_page("main.py")

```

**Run your app with:**

```bash
streamlit run main.py
```

##### **Output**

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%209/mod9-top2.1.png">

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%209/mod9-top2.2.png">

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%209/mod9-top2.3.png">

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%209/mod9-top2.4.png">

----

#### **Step-by-Step Walkthrough**

-   **Initialize session state variables**
    
    -   At the start of `main.py`, we check if keys exist in `st.session_state`.
        
    -   If not, we create them:
        
        -   `st.session_state.logged_in = False` → tracks whether the user is logged in.
            
        -   `st.session_state.username = ""` → stores the current username.
            
-   **During login**
    
    -   When the user submits the login form, if the password is `"demo"`, then:
        
        -   `st.session_state.logged_in` is set to `True`.
            
        -   `st.session_state.username` is set to the entered username.
            
    -   These values persist across pages.
        
-   **Access control on each page**
    
    -   Every page (Dashboard, Reports, Settings) checks `st.session_state.get("logged_in", False)`.
        
    -   If `False`, the page warns the user and redirects back to `main.py`.
        
    -   If `True`, the page displays personalized content using `st.session_state.username`.
        
-   **Navigation between pages**
    
    -   Since `st.session_state` retains values across page loads, the user doesn’t need to log in again.
        
    -   `st.switch_page("...")` just changes the view, while the login state remains intact.
        
-   **Logout**
    
    -   On pressing `Logout`, we reset:
        
        -   `st.session_state.logged_in = False`
            
        -   `st.session_state.username = ""`
            
    -   This clears the session so the user is forced to log in again.

#### **Key Learning Points**

- Session state persists automatically across all pages in multi-page Streamlit applications

- Authentication patterns use session state to maintain login status across page navigation

- `st.stop()` prevents unauthorized access to protected pages

- Different pages can access and modify the same session state variables

- Cross-page data sharing enables integrated application experiences

#### **Conclusion**

Multi-page session state management unlocks the ability to build comprehensive applications like e-commerce platforms, learning management systems, and enterprise dashboards that maintain user context across sections. This persistent state capability enables developers to create applications where user progress, preferences, and data flow seamlessly between different functional areas. Mastering cross-page state management is essential for building web applications that compete with traditional desktop software in terms of user experience and functionality.


----

### Topic 9.3: Widget Callbacks

---

#### **Introduction**

Imagine building a data dashboard where users need to filter datasets, update charts, and modify parameters—but every single interaction forces them to wait while the entire application reloads from scratch. This sluggish experience plagues traditional web applications, where clicking a button to add an item to a list, submitting a form, or adjusting a slider triggers a complete page refresh. Users become frustrated with the delays, especially when performing multiple related actions that should flow seamlessly together. The problem intensifies in complex data applications where immediate feedback is crucial for maintaining user engagement and workflow momentum.

Streamlit's widget callback system eliminates these delays by allowing specific functions to execute instantly when users interact with widgets, rather than forcing the entire app to rerun. This creates responsive, desktop-application-like experiences where button clicks, input changes, and widget interactions trigger immediate responses. Widget callbacks are particularly powerful for managing complex state changes, processing form data dynamically, and coordinating multiple widgets to work together seamlessly—transforming sluggish web apps into fluid, interactive experiences that respond in real-time to user actions.

#### **Mini Project**

David is a project manager who currently tracks his tasks across sticky notes, email drafts, and a basic notepad app. Throughout his busy days, he constantly loses track of what he's already completed, forgets to add new urgent tasks that come up during meetings, and wastes time manually crossing out or erasing outdated items when priorities change.
A dedicated task tracker would give David one central place to instantly add new tasks, check off completed work for immediate visual clarity, and remove irrelevant items with a simple delete action, transforming his chaotic task management into a streamlined daily workflow.

##### **Project Setup**

Create a new file `app.py`:

```python

import streamlit as st

# Initialize session state for tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = []
if 'task_input' not in st.session_state:
    st.session_state.task_input = ""

# Task functions 
def add_task():
    if st.session_state.task_input.strip():
        st.session_state.tasks.append({
            'text': st.session_state.task_input,
            'done': False
        })
        st.session_state.task_input = ""

def toggle_task(index):
    st.session_state.tasks[index]['done'] = not st.session_state.tasks[index]['done']

def delete_task(index):
    st.session_state.tasks.pop(index)

st.title("⚡ QuickTasks ⚡")

# Add New Task Section 
st.subheader("➕ Add a New Task")
st.text_input("Enter your task here:", key="task_input", on_change=add_task)

# Task List Section
st.subheader("📋 Your Tasks")
if not st.session_state.tasks:
    st.info("No tasks yet. Add one above! ✨")

for i, task in enumerate(st.session_state.tasks):
    col1, col2, col3 = st.columns([3, 1, 1])
    
    with col1:
        style = "text-decoration: line-through; color: gray;" if task['done'] else ""
        st.markdown(f"<span style='{style}'>{task['text']}</span>", unsafe_allow_html=True)
    
    with col2:
        status = "✅ Done" if task['done'] else "✔️ Mark Done"
        st.button(status, key=f"toggle_{i}", on_click=toggle_task, args=(i,))
    
    with col3:
        st.button("🗑️ Delete", key=f"delete_{i}", on_click=delete_task, args=(i,))

```
**Run your app with:**

```bash
streamlit run main.py
```
---

##### **Output**

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%209/mod9-task1.png">

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%209/mod9-task2.png">

----

#### **Step-by-Step Walkthrough**

-   **Initialize session state**
    
    -   `st.session_state.tasks` → stores the list of tasks (each as a dictionary with `'text'` and `'done'`).
        
    -   `st.session_state.task_input` → stores the current input value for the new task.
        
-   **Define task functions**
    
    -   `add_task()` → adds a new task to `tasks` if the input is not empty and clears `task_input`.
        
    -   `toggle_task(index)` → flips the `'done'` status of the task at the given index.
        
    -   `delete_task(index)` → removes the task at the given index.
        
            
-   **Display tasks dynamically**
    
    -   Loop over `st.session_state.tasks` using `enumerate()` to get `i` (index) and `task`.
        
    -   Use `st.columns([3,1,1])` to layout each task row:
        
        -   **Column 1:** Show task text with strikethrough if done (`task['done']`).
            
        -   **Column 2:** Button to toggle done status:
            
            -   `st.button(status, key=f"toggle_{i}", on_click=toggle_task, args=(i,))`
                
            -   `on_click` calls `toggle_task` with the task index.
                
        -   **Column 3:** Button to delete the task:
            
            -   `st.button("🗑️ Delete", key=f"delete_{i}", on_click=delete_task, args=(i,))`
                
            -   `on_click` calls `delete_task` with the task index.
                
-   **Reactive updates**
    
    -   Any modification to `st.session_state.tasks` triggers a **Streamlit rerun**, instantly updating the UI.
        
    -   The `key` parameter ensures each input and button is **uniquely tracked** across reruns.
        
-   **Empty task handling**
    
    -   If `st.session_state.tasks` is empty, `st.info("No tasks yet. Add one above! ✨")` shows a friendly message.

#### **Conclusion**

This callback pattern establishes a foundation for building responsive user interfaces that can be applied across web applications, dashboards, and interactive tools. The ability to connect user actions directly to functions while maintaining clean state management becomes essential when scaling applications or integrating real-time features. Mastering this approach to event-driven programming significantly improves development efficiency and creates more intuitive user experiences in any interactive project.


----

### Topic 9.4: Caching

---

#### **Introduction**

Picture a data analysis app that fetches information from an API, loads a large CSV file, and trains a machine learning model every single time a user adjusts a filter or clicks a button. Each interaction forces users to wait through the same expensive operations repeatedly—the API call takes 3 seconds, the file load takes 2 seconds, and model training takes 10 seconds—even when the underlying data hasn't changed. This creates a painfully slow user experience where simple interactions result in 15+ second delays, making the app practically unusable for real-world scenarios where users need to explore data interactively.

Streamlit's caching system eliminates this performance bottleneck by intelligently storing the results of expensive operations and reusing them when inputs remain unchanged. Through two main caching decorators—`st.cache_data` for data operations like API calls and calculations, and `st.cache_resource` for global resources like database connections or ML models—Streamlit transforms sluggish apps into snappy, responsive tools. When users interact with a cached app, operations that previously took seconds now execute instantly, creating fluid experiences where data exploration feels seamless and immediate rather than frustratingly slow.

#### **Mini Project**

Emma is researching universities abroad and constantly switches between searching for schools in different countries. Each time she revisits a country she's already explored, she has to wait for the same slow loading times as the system fetches identical university data from scratch, making her research process frustratingly repetitive.

A smart university finder would cache her previous searches, instantly showing universities from countries she's already explored while fetching fresh data for new searches, eliminating unnecessary wait times during her university research.

##### **Project Setup**

Create a new file `app.py`:

```python

import streamlit as st
import requests

@st.cache_data
def fetch_universities(country):
    """Fetch universities from API and cache results"""
    url = f"http://universities.hipolabs.com/search?country={country}"
    response = requests.get(url)
    return response.json()

@st.cache_resource
def get_api_base_url():
    """Cache the API base configuration"""
    return "http://universities.hipolabs.com/search"

st.title("University Finder")
st.write("Search for universities by country (results are cached for faster loading)")

# Country selection
country = st.selectbox(
    "Select a country:",
    ["United States", "Canada", "United Kingdom", "Australia", "Germany"]
)

if country:
    # Show loading message
    with st.spinner(f"Searching universities in {country}..."):
        universities = fetch_universities(country)
    
    st.subheader(f"Universities in {country}")
    st.write(f"Found {len(universities)} universities")
    
    # Display first 10 universities
    for uni in universities[:10]:
        with st.expander(uni['name']):
            st.write(f"**Website:** {uni.get('web_pages', ['N/A'])[0]}")
            st.write(f"**Domain:** {uni.get('domains', ['N/A'])[0]}")
            
    # Show caching info
    st.info("💡 Try selecting the same country again - it loads instantly from cache!")

```

**Run your app with:**

```bash
streamlit run app.py
```

##### **Output**

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%209/mod9-cache1.png">

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%209/mod9-cache2.png">

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%209/mod9-cache3.png">

----

#### **Step-by-Step Walkthrough**

-   **`import requests`** → allows the app to make HTTP requests to external APIs (here, to fetch university data).
        
-   **Fetch universities with caching**
    
    -   `@st.cache_data` wraps `fetch_universities(country)` → caches results based on the country parameter.
        
    -   First search triggers an API call; subsequent searches for the same country return cached data instantly.
        
-   **Global resource caching**
    
    -   `@st.cache_resource` wraps `get_api_base_url()` → stores global configuration that doesn’t depend on parameters.
        
-   **Loading feedback**
    
    -   `st.spinner()` shows a loading message while the API request is in progress.
        
        
-   **Cache behavior explanation**
    
    -   Streamlit automatically invalidates cache if the input parameter (`country`) changes.
        
    -   The same function code works without modification; Streamlit handles caching transparently.
        
    -   `st.info()` reminds users that selecting the same country again loads results instantly from cache.

#### **Conclusion**

Strategic caching implementation dramatically improves application performance across web development, data processing, and API-driven projects by eliminating redundant computations. This optimization technique becomes crucial when building scalable applications that handle external data sources, large datasets, or resource-intensive operations. Mastering efficient caching strategies reduces server load, minimizes user wait times, and enables developers to create professional-grade applications that maintain responsiveness under heavy usage.

----

### Topic 9.5: Progress & Status

#### **Introduction**

Imagine uploading a large dataset to your Streamlit app for processing—clicking the "Analyze" button only to be met with a completely static screen for several minutes. Users have no idea if the app is working, frozen, or broken, leading many to refresh the page or abandon the process entirely. This scenario repeats across data applications whenever users trigger long-running operations like file processing, API calls, or complex calculations. Without visual feedback, even a 30-second operation feels endless, creating anxiety and uncertainty that drives users away from otherwise functional applications.

Streamlit's progress indicators and status messaging tools solve this communication gap by keeping users informed and engaged during lengthy operations. Through `st.progress()` for visual progress bars showing completion percentages, `st.spinner()` for animated loading indicators with custom messages, and status containers for multi-step process updates, Streamlit transforms potentially frustrating wait times into reassuring progress updates. These feedback mechanisms turn user anxiety into confidence, ensuring that long-running processes feel manageable and professional rather than broken or unresponsive.

#### **Mini Project**
Marcus is a market research analyst who dreads Monday mornings when his inbox fills with chaotic CSV files—customer surveys with typos, sales reports missing crucial columns, and product data riddled with duplicates from different regional offices. He currently spends his entire morning playing detective with spreadsheets, manually hunting down errors and inconsistencies, never knowing if he's missed something critical or how to explain his cleaning process to his skeptical boss.
A transparent data cleaning pipeline would let Marcus drag and drop his messy files and watch as the system methodically identifies and fixes each issue, providing a clear log of what was cleaned and timing estimates, transforming his Monday morning nightmare into a confident, trackable process.

##### **Project Setup**

Create a new file `app.py`:

```python
import streamlit as st
import pandas as pd
import time

# Cleaning function

def clean_step(data, step, progress, i, total):
    time.sleep(1)
    if step == "Remove duplicates":
        cleaned = data.drop_duplicates()
        status = f"Removed {len(data) - len(cleaned)} duplicates"
    elif step == "Handle missing":
        cleaned = data.fillna("N/A")
        status = "Filled missing values"
    elif step == "Standardize text":
        cleaned = data.copy()
        for col in cleaned.select_dtypes('object'):
            cleaned[col] = cleaned[col].astype(str).str.strip().str.title()
        status = f"Standardized text in {len(cleaned.select_dtypes('object').columns)} columns"
    else:
        cleaned = data
        status = "Step complete"
    progress.progress((i + 1)/total)
    return cleaned, status

# --- Streamlit UI ---
st.title("✨ Quick Data Cleaner")
uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.success(f"Loaded {len(data)} rows, {len(data.columns)} columns")
    st.dataframe(data.head())

    if st.button("Start Cleaning"):
        steps = ["Remove duplicates", "Handle missing", "Standardize text"]
        progress = st.progress(0)
        status_text = st.empty()
        cleaned = data.copy()

        for i, step in enumerate(steps):
            status_text.text(f"Step {i+1}/{len(steps)}: {step}...")
            cleaned, step_status = clean_step(cleaned, step, progress, i, len(steps))
            status_text.text(f"✅ {step_status}")

        st.success("🎉 Cleaning complete!")
        st.subheader("Cleaned Data")
        st.dataframe(cleaned.head())

```
**Run your app with:**

```bash
streamlit run app.py
```

##### **Output**

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%209/mod9-data1.png">

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%209/mod9-data2.png">

---

#### **Step-by-Step Walkthrough**


-   `st.button("Start Cleaning")` triggers the cleaning pipeline when clicked, starting the sequential data cleaning steps.
    
-   `clean_step(data, step, progress, i, total)` performs individual cleaning operations (remove duplicates, fill missing values, standardize text) and updates the progress bar and status message for each step.
    
-   `st.progress(0)` creates a progress bar that updates after each cleaning step to show progress visually.
    
-   `st.empty()` provides a placeholder for dynamic status messages during the cleaning process.
    
-   `st.success("🎉 Cleaning complete!")` signals completion, giving users visual feedback that all steps have finished.
    
-   `st.dataframe(cleaned.head())` displays the first 5 rows of the cleaned data so users can immediately see the effect of the cleaning steps.


#### **Conclusion**

Progress indicators and status messaging are essential UX patterns that prevent user abandonment and build trust across any application involving time-intensive operations. Implementing appropriate feedback mechanisms—whether spinners, progress bars, or status updates—becomes critical for maintaining user engagement in data processing tools, file uploads, API integrations, and batch operations. These user experience principles directly impact application adoption and user satisfaction, making them fundamental skills for developing professional software that handles complex or lengthy tasks.


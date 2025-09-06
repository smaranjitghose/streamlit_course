
# Module 7: Building Multi-Page Applications in Streamlit

### Introduction
So far, every app you’ve built has been a single, scrolling page. But imagine your app growing—wouldn’t it be easier to organize content into distinct sections, just like chapters in a book or tabs on a website?

**Multi-page apps transform your Streamlit project from a simple poster into an interactive storybook or professional website:**

-   Each "chapter" (page) covers its own topic.
    
-   Users flip between chapters at will.
    
-   You can share elements (like instructions or scores) across different sections.
    

Streamlit makes this effortless. With tools like the  `pages/`  folder for automatic navigation, session state for memory, and reusable utility files, building polished multi-page apps is something anyone can do.


### Why Go Multi-Page?

Imagine browsing an online store, a recipe book, or a quiz—would you want  _everything_  crammed on one page, or split into Home, Products, Cart, and more?  **Multi-page design keeps content organized, interactive, and easy to explore.**


### How Does Streamlit Help?

-   The  **pages/ folder**  acts like a bookshelf; each Python file inside becomes one page, complete with automatic sidebar navigation.
    
-   Use  **buttons and session state**  for custom navigation flows, like flipping through recipes or tutorials.
    
-   Build shared code files (like utilities) so logic, data, and scores work seamlessly across pages—no messy repetition.

---
### Topic 7.1: Pages Folder 

**Introduction**  
Ever wish your app felt more like a real website, with different sections for different purposes—Home, About, Contact, and more? Streamlit's  **pages folder**  lets you break your work into distinct chapters, just like creating pages in a website or sections in a book. The magic? Streamlit auto-detects every file in this folder as a page and creates a sidebar for easy navigation.

### Mini Project : Company Website Clone
Let’s build a mini company site—each section its own Python file, switching easily from Home to About Us to Contact via the sidebar menu.

**File structure:**

```
my_app/
  Home.py
  pages/
    1_About_Us.py
    2_Contact.py
``` 

**`Home.py`**

```
import streamlit as st

st.title("🏢 Welcome to Our Company")
st.write("We build amazing products for amazing people.")
``` 
**`pages/1_About_Us.py`**

```
import streamlit as st

st.title("👥 About Us")
st.write("We are a team of passionate developers building web apps with Streamlit.")
```

**`pages/2_Contact.py`**

```
import streamlit as st

st.title("📬 Contact Us")
st.write("Email: hello@ourcompany.com")
st.write("Phone: +1 234 567 890")
``` 

**Expected Output**

-   **Sidebar with navigation**: Home, About Us, Contact.
    
-   Each page displays its own content when selected.  

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%207/company_website.png">

**Key Takeaways**

-   Creating a `pages/` folder makes Streamlit auto-generate navigation.
    
-   File names decide the page order (`1_`, `2_`, etc.).
    
-   Great for **company sites, dashboards, and portfolio apps**.

---
### Topic 7.2: Navigation 

Sometimes a sidebar isn’t enough—what if you want users to move through content at their own pace, like flipping through a cookbook? Custom navigation lets you control the order and flow: “Next”, “Previous”, just like turning pages in a recipe book or a photo album. By saving user position with session state, your app can remember exactly where each user left off.

### Mini Project : Recipe Book

We’ll create a simple **Recipe Book** with Previous and Next buttons so users explore recipes step by step, making the app feel interactive and personal.

**Code**

**`app.py`**

```
import streamlit as st

# Session state to remember which recipe is active
if "page" not in st.session_state:
    st.session_state.page = 0

recipes = [
    {"title": "🍝 Spaghetti Carbonara", "steps": ["Boil pasta", "Fry pancetta", "Mix with eggs & cheese"]},
    {"title": "🥗 Greek Salad", "steps": ["Chop veggies", "Add feta cheese", "Drizzle olive oil"]},
    {"title": "🍪 Chocolate Chip Cookies", "steps": ["Mix dough", "Add chocolate chips", "Bake until golden"]}
]

# Display current recipe
recipe = recipes[st.session_state.page]
st.title(recipe["title"])
for step in recipe["steps"]:
    st.write(f"- {step}")

# Navigation buttons
col1, col2 = st.columns(2)
if col1.button("Previous") and st.session_state.page > 0:
    st.session_state.page -= 1
if col2.button("Next") and st.session_state.page < len(recipes) - 1:
    st.session_state.page += 1

```

**Expected Output**

-   Displays a recipe (title + steps).
    
-   Buttons for **Previous** and **Next** to navigate between recipes.  

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%207/recipe1.png">

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%207/recipe2.png">
    
**Key Takeaways**

-   Use **session state** (`st.session_state`) to remember navigation.
    
-   Buttons let you control the flow like a **flipbook of recipes**.
    
-   Works well for **tutorials, portfolios, and storytelling apps**.

---
### Topic 7.3: Shared Utilities 

In bigger projects, you don’t want to duplicate work or get lost updating code in many places. Shared utilities act like a communal toolbox or library—all your pages can call common functions for tasks like scoring, logging, or formatting. Streamlit's modular design makes it easy to keep your code DRY (Don’t Repeat Yourself) and efficient.



### Mini Project : Quiz App

We’ll make a **Quiz App** where a single score-tracking utility is imported and used on every question page and the results page—just like all workers in a company sharing the same set of tools.

**File structure:**
```
quiz_app/
  Home.py
  pages/
    1_Question1.py
    2_Question2.py
    3_Results.py
  utils.py
``` 

**utils.py**
```
import streamlit as st 
def  init_score(): 
    if  "score"  not  in st.session_state:
        st.session_state.score = 0  
def  update_score(points):
    st.session_state.score += points
``` 

**Home.py**

```
import streamlit as st 
import utils

utils.init_score()
st.title("🎯 Welcome to the Quiz")
st.write("Navigate through the pages to answer questions!")
```

**pages/1_Question1.py**

```
import streamlit as st 
import utils

utils.init_score()

st.title("Question 1")
answer = st.radio("What is 2 + 2?", [3, 4, 5]) 
if st.button("Submit"): 
    if answer == 4:
        utils.update_score(1)
        st.success("Correct!") 
    else:
        st.error("Oops, try again.")
``` 

**pages/2_Question2.py**

```
import streamlit as st import utils

utils.init_score()

st.title("Question 2")
answer = st.radio("What is the capital of France?", ["Berlin", "Paris", "Rome"]) if st.button("Submit"): if answer == "Paris":
        utils.update_score(1)
        st.success("Correct!") else:
        st.error("Oops, try again.")
```

**pages/3_Results.py**

```
import streamlit as st 
import utils

utils.init_score()

st.title("📊 Quiz Results")
st.write(f"Your final score: {st.session_state.score}")
```

**Expected Output**

-   Sidebar navigation for quiz questions.
    
-   Score tracked across pages using `utils.py`.  

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%207/quiz1.png">

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%207/quiz2.png">

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%207/quiz3.png">

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%207/quiz4.png">
    
**Key Takeaways**

-   Shared utilities (`utils.py`) avoid **duplicate code**.
    
-   `st.session_state` helps track progress across pages.
    
-   Perfect for **quizzes, surveys, and multi-step workflows**.
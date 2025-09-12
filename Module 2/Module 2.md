
# Module 2: Displaying Text and Information

## Topic 2.1: Titles & Headings

### **Introduction**

In any app, text isn’t just decoration—it’s the main tool for  _guiding and reassuring_  users. Imagine opening a food delivery app: it isn’t the flashy images or buttons that first grab your attention, but the bold  **titles**  ("Welcome!"), the friendly  **messages**  ("Order received!"), and the clear  **instructions**  ("Enter your address below").

Text shapes the narrative your app tells. If the app were a book, text would be the chapters, headers, and notes that provide structure and orientation.

Well-structured text achieves three powerful goals:

-   **Attracts attention**  with bold, scannable titles and highlights.
    
-   **Breaks up information**  into digestible chunks, reducing cognitive overload.
    
-   **Creates flow and hierarchy**, leading users step by step without confusion.
    

Without text hierarchy, users encounter a "wall of words"—overwhelmed, disoriented, and likely to abandon the app.

----------

### **Core Display Elements in Streamlit**

Streamlit provides several specialized text display functions that let you build this structure effectively:

-   **st.title()**  
    The  _main banner_  of your app—like the cover of a book or a movie poster. It should communicate the app’s purpose instantly.
    
    `st.title("🍕 Food Delivery Tracker")` 
    
    This immediately signals the app’s identity.
    
-   **st.header()**  
    Use headers for primary sections. They’re your chapter titles, dividing content into logical, easy-to-scan blocks.
    

    `st.header("Track Your Order")` 
    
-   **st.subheader()**  
    Subheaders are like smaller sub-chapters. They draw attention to details inside a section—steps, tooltips, or clarifications.
    
    `st.subheader("Step 1: Enter Your Address")` 
    
-   **st.divider()**  
    Dividers visually separate different ideas or tasks. They are essential for pacing content, so users never face an endless stream of text or widgets.
 
    `st.divider()` 
    
-   **st.write()**  
    The most flexible element,  `st.write()`  can display plain text, formatted Markdown, numbers, DataFrames, and more. Use it for all-purpose explanations and inline content.
   
    ```python
    st.write("Your order will be delivered in **30 minutes** 🚚")  
    st.write("Here’s a quick summary of your details:")  
    st.write({"Name":  "John",  "Order":  "Margherita Pizza",  "ETA":  "30 mins"})
    ``` 
    

----------

### **Best Practices**

-   Always begin with a  **clear title**  that defines the app’s core purpose.
    
-   Break down sections using  **headers and subheaders**, just like academic papers, blog posts, or structured documents.
    
-   Insert  **dividers**  after major actions or transitions to keep the page scannable.
    
-   Use  **st.write()**  creatively for inline messaging, confirmations, explanations, and visual “anchors” for dynamic outputs.
    

----------

### **Pro Tip**

Before adding interactivity (buttons, inputs, sliders), map out your  **text hierarchy**  first. Draft your app like an outline:

-   A  **title**  that sets the stage.
    
-   **Headers**  representing the big blocks of functionality.
    
-   **Subheaders**  breaking down smaller tasks.
    
-   Inline  **st.write() statements**  for reassurance and clarity.
    
-   **Dividers**  to introduce breathing space.
    

This ensures that as you add logic and visuals, users always know  _what is happening_  and  _where to look next_.

----------

## **Mini Project: One-Page Resume**

Resumes are often the first impression you make on employers. In this mini project, we’ll create a simple one-page resume app using Streamlit. It’s a fun way to showcase your profile while also learning how to organize content with different Streamlit display elements.

- Create a file `app.py`  

```python
import streamlit as st

st.title("💼 John Doe - Data Scientist")  
st.header("Experience")  
st.subheader("Machine Learning Engineer at XYZ Corp (2020-Present)")  
st.write("- Built scalable NLP pipelines using LSTM and Transformers.")  
st.write("- Improved sentiment analysis accuracy by 15%.")  
st.divider()  
st.header("Education")  
st.subheader("M.Sc. in Artificial Intelligence")  
st.write("University of Example, 2018-2020")  
st.divider()  
st.header("Skills")  
st.write("- Python, TensorFlow, PyTorch")  
st.write("- Natural Language Processing, Deep Learning, Data Visualization")
```
---

**Run the app**
- `streamlit run app.py`

### Expected Output


### Explanation

- `st.title()` → Creates the main heading of the resume.

- `st.header()` → Defines key sections like Experience, Education, Skills.

- `st.subheader()` → Highlights specific details (like job role or degree).

- `st.write()` → Displays text, bullet points, or descriptions.

- `st.divider()` → Adds a clean horizontal line to separate sections.

----


## Topic 2.2: Markdown

###  **Introduction to Markdown**

Great text isn’t just  _what you say_—it’s also  _how you present it_. Imagine walking into a restaurant where the menu is typed in  **one font, one size, no bold headings**. You’d struggle to find your favorite dish, right?

That’s exactly why  **Markdown**  exists. Markdown is a lightweight formatting language that helps your text stand out, stay organized, and feel polished. You don’t need CSS or HTML—just simple symbols like  `*`,  `_`, and  `#`.

With Markdown in Streamlit (`st.markdown()`), you can:

-   Add  **bold text**  → highlight the star of the menu (e.g., dish name).
    
-   Use  _italics_  → make soft notes or smaller remarks.
    
-   Create bullet  `lists`  → perfect for menus, steps, or features.
    
-   Add headings (`#`,  `##`,  `###`) → structure your sections.
    
-   Insert emojis 🎉 → bring personality and friendliness.
    
-   Even mix in  **inline code**  `print("Hello")`  → for tutorials or developer apps.
    

**Pro Tip**: Think of Markdown styling like  **seasoning food**. A small amount makes the dish delicious—too much makes it overwhelming.

###  **Mini Project: Restaurant Menu App**
Digital menus are becoming increasingly popular in restaurants and cafés. In this mini project, we’ll design a **stylish restaurant menu app** using Streamlit and Markdown formatting. This will help you practice combining text, emojis, and styling to create an engaging layout.

- Create a file `app.py`

```python
import streamlit as st  

# Page setup
st.set_page_config(page_title="🍽️ Bistro Café Menu", layout="centered")  

# Title
st.title("🍴 Welcome to Bistro Café")  
st.markdown("### 🌟 **Today’s Special Menu**")  
st.write("---")  

# Starters
st.header("🥗 Starters")  
st.markdown("""  
- **Bruschetta** 🥖  
  _Toasted bread topped with fresh tomatoes, garlic & basil_ — ₹180  

- **Caesar Salad** 🥬  
  _Crisp romaine lettuce, parmesan, and croutons_ — ₹220  
""")  

st.divider()  

# Main Course
st.header("🍝 Main Course")  
st.markdown("""  
- **Pasta Alfredo** 🍝  
  _Creamy white sauce with mushrooms & herbs_ — ₹350  

- **Grilled Chicken** 🍗  
  _Served with mashed potatoes and sautéed veggies_ — ₹420  
""")  

st.divider()  

# Desserts
st.header("🍰 Desserts")  
st.markdown("""  
- **Chocolate Lava Cake** 🍫  
  _Warm chocolate cake with gooey center_ — ₹180  

- **Cheesecake** 🍮  
  _Classic New York style, rich & smooth_ — ₹200  
""")  

st.divider()  

# Beverages
st.header("🥂 Beverages")  
st.markdown("""  
- **Cold Coffee** ☕ — ₹120  
- **Fresh Lime Soda** 🥤 — ₹100  
- **Iced Tea** 🍹 — ₹130  
""")  

```

---
**Run the app**
-  streamlit run `app.py`
----------

### Expected Output


----------

### Explanation

-   `st.set_page_config()` → Defines the page title and layout.
    
-   `st.title()` → Displays the main café welcome title.
    
-   `st.markdown()` → Adds rich text formatting with **bold**, _italics_, and emojis.
    
-   `st.header()` → Creates clear section titles (Starters, Main Course, etc.).
    
-   `st.write("---")` and `st.divider()` → Insert horizontal separators for neat structure.

----


## Topic 2.3: Code & Formulas

----------

### **Introduction**

Not every app is about menus or dashboards—some are  **teaching tools, study aids, or scientific calculators**. In these cases, plain text is often not enough. Users need  **structured code examples, neat math, and quick-reference highlights**. That’s where Streamlit shines with its academic-friendly display options:

-   **`st.code()`**  → Think of it as a  **digital blackboard for code**. Instead of dumping messy text, it formats your code with syntax highlighting and proper indentation—easy to read, easy to copy.
    
-   **`st.latex()`**  → Designed for  **math and science apps**. Just like professors writing equations neatly on a board, LaTeX renders formulas beautifully. Users don’t just “see” the formula—they  _understand_  it.
    
-   **`st.badge()`**  → A newer micro-component for emphasizing quick facts, tags, or statuses. Perfect for  **exam tips**, difficulty levels, or topic labels (e.g.,  _“Easy”, “Important”, “Formula to Memorize”_).
    

Imagine being a student revising before an exam:

-   Instead of a cluttered notebook, you open an app.
    
-   All  **formulas are beautifully arranged**  with LaTeX.
    
-   **Code snippets**  show implementation, so you know  _how to apply the math_.
    
-   **Badges**  highlight “high-yield” or “must-memorize” items.
    

This combination makes your learning resource  **structured, professional, and exam-ready**.

**Pro Tip**: Use  `st.latex()`  to present key formulas,  `st.code()`  for applying them in real-life coding, and  `st.badge()`  for tagging and prioritizing information. It’s like having a  **digital exam cheatsheet**  that looks polished and reliable.

----------

### **Mini Project: Exam Prep Sheet App**

Revision during exams can be overwhelming if you don’t have everything in one place. In this project, we’ll build a **one-stop exam prep app** that combines math formulas, Python code snippets, and study badges to highlight the most important topics.

- Create a file `app.py`

```python
import streamlit as st  

# Page Setup  
st.set_page_config(page_title="📘 Exam Prep Sheet", layout="centered")  

st.title("📘 Quick Exam Prep Sheet")  
st.write("Your go-to revision notes with formulas, code, and important highlights ✅")  
st.divider()  

# Section: Percentages  
st.header("📊 Percentages")  
st.badge("High Yield")  
st.latex(r"\text{Percentage (\%)} = \frac{\text{Value}}{\text{Total}} \times 100")  
st.code(""" 
# Example: Calculating percentage 
value = 45 
total = 60 
percentage = (value/total) * 100 
print(percentage)  # 75.0% 
""", language="python")  
st.caption("👉 Percentages are often tested in competitive exams like SSC, Banking, and Aptitude tests.")  
st.divider()  

# Section: Interest  
st.header("💰 Simple & Compound Interest")  
st.badge("Formula to Memorize")  
st.latex(r"SI = \frac{P \times R \times T}{100}")  
st.latex(r"CI = P \times \left(1 + \frac{R}{100}\right)^T - P")  
st.code(""" 
# Example: Simple Interest 
P = 1000  # Principal 
R = 5     # Rate per year 
T = 2     # Time in years 
SI = (P*R*T)/100 
print(SI)  # 100 
""", language="python")  
st.caption("Where P = Principal, R = Rate (%), T = Time (years)")  
st.divider()  

# Section: Averages  
st.header("📈 Averages")  
st.badge("Core Concept")  
st.latex(r"\text{Average} = \frac{\text{Sum of terms}}{\text{Number of terms}}")  
st.code(""" 
# Example: Finding average 
nums = [12, 15, 20, 25, 30] 
average = sum(nums)/len(nums) 
print(average)  # 20.4 
""", language="python")  
st.divider()  

# Section: Probability  
st.header("🎲 Probability")  
st.badge("Exam Favorite")  
st.latex(r"P(E) = \frac{\text{Favorable outcomes}}{\text{Total outcomes}}")  
st.code(""" 
# Example: Probability of rolling a 6 on dice 
favorable = 1    # only '6' 
total = 6        # six outcomes 
P = favorable / total 
print(P)  # 0.1667 or 16.67% 
""", language="python")  
st.divider()  

# Section: Permutations & Combinations  
st.header("🔢 Permutations & Combinations")  
st.badge("Important")  
st.latex(r"nPr = \frac{n!}{(n-r)!}")  
st.latex(r"nCr = \frac{n!}{r!(n-r)!}")  
st.code(""" 
import math 

# Example: nCr and nPr 
n, r = 5, 2 
nPr = math.factorial(n)//math.factorial(n-r) 
nCr = math.factorial(n)//(math.factorial(r)*math.factorial(n-r)) 
print(nPr, nCr)  # 20 , 10 
""", language="python")  


```
---

**Run the app**
- `streamlit run app.py`
----------
### **Expected Output**

-----
### **Explanation**

-   **`st.latex(...)`**  → Renders formulas like a math book for clarity.
    
-   **`st.code(...)`**  → Shows matching Python implementation with syntax highlighting.
    
-   **`st.badge(...)`**  → Marks critical facts (“High Yield”, “Important”) to guide learners on what’s essential for exams.
    
-   **`st.caption(...)`**  → Provides quick notes or context below formulas.
    
-   **`st.success(...)`**  → Acts as a motivational closer or completion note.
    

This combination gives the  _feel of a smart revision notebook_, bridging theory with practice.
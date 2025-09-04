# Module 2: Working with Text & Messages in Streamlit
### Introduction
Text is the heart of user communication in apps.

Think about your favorite mobile app—whether it’s a food delivery app, a news portal, or WhatsApp. What keeps you engaged? It’s not just the buttons and images, but  **the words**: titles, helpful hints, warnings, and even emojis. In Streamlit, text is more than decoration—it’s how your app  **guides, teaches, and reassures users.**

This module helps you master text in **Streamlit**:

-   Organize content using  **titles and headings**
    
-   Style your text using  **Markdown**
    
-   Present  **code snippets & math equations**  neatly
    
-   Guide users with  **status messages**
    

----------

### Topic 2.1 Titles & Headings

**Introduction**  
Think of your app as a  **storybook**. If a story had no chapters, readers would feel lost. Similarly, if an app has no titles or headings, users won’t know where to focus. Headings are your  **navigation beacons**.

-   `st.title()`  → The  **main identity**  of your app (like a book title or the banner at a conference).
    
-   `st.header()`  → Major sections that divide content logically (like big chapters).
    
-   `st.subheader()`  → Smaller sub-sections that explain finer details (like subheadings in a blog).
    

Without these, your app becomes a  **text wall**, which quickly overwhelms users.

**Pro Tip**: Start with one title (like a welcome banner), then logically structure everything with headers so that your users can  **scan instead of read everything**.

### Mini Project: Restaurant Menu App

Imagine you're creating a digital menu for a restaurant. You'd want to organize the menu into sections like "Starters," "Main Course," and "Desserts." Streamlit's `st.title`, `st.header`, and `st.subheader` functions are perfect for this!

**Code**
```python
import streamlit as st

st.title("Welcome to Our Restaurant!")

st.header("Starters")
st.write("Garlic Bread - $5")
st.write("Soup of the Day - $7")

st.header("Main Course")
st.write("Steak - $25")
st.write("Pasta Carbonara - $18")

st.subheader("Desserts")
st.write("Chocolate Cake - $8")
st.write("Ice Cream - $6")

```

**Explanation:**

-   `st.title("Welcome to Our Restaurant!")`: This displays the main title of the app, making it clear what the app is about.
    
-   `st.header("Starters")`: This creates a header for the "Starters" section. Headers are larger and bolder than regular text, helping to visually separate sections.
    
-   `st.subheader("Desserts")`: This creates a subheader for the "Desserts" section. Subheaders are smaller than headers but still useful for further dividing content.
    
-   `st.write(...)`: This displays the menu items and their prices. `st.write` is a versatile function that can display text, numbers, dataframes, and more.
    

**Expected Output:**

The Streamlit app will display a title "Welcome to Our Restaurant!", followed by headers for "Starters" and "Main Course", and a subheader for "Desserts". Each section will list the menu items and their prices.

**Key Takeaways:**

-   Use `st.title` for the main title of your app.
    
-   Use `st.header` to create section headings.
    
-   Use `st.subheader` to create sub-section headings.
    
-   Use `st.write` to display text and other content.
----------

### Topic 2.2 Markdown & Styling

**Introduction**  
Great text isn’t just about “what you write,” it’s also “how it looks.” Imagine reading a newspaper where  **all text is the same size**  and  **no bold headings exist**. Boring and confusing, right?

This is what Markdown helps you avoid. Markdown is like a  **mini design tool for text**. With it, you can:

-   Add  **bold emphasis**  → Perfect for drawing attention.
    
-   Add  _italics_  → Great for side notes or soft expression.
    
-   Create  `lists`  → Helps structure steps, features, or instructions.
    
-   Insert emojis  → Add human-friendly, casual tone.
    

Streamlit’s  `st.markdown()`  allows you to use these styles instantly. It brings your text alive,  **without needing HTML or CSS**.

**Pro Tip**: Use Markdown to  **highlight key ideas**, but don’t overdo styling. Think of it like  **seasoning food**—a little enhances flavor, too much ruins the dish.


### Mini Project: Blog Post Page

Markdown is a lightweight markup language that allows you to format text using simple symbols. Streamlit supports Markdown, making it easy to create styled text, lists, and more. Let's create a simple blog post page.

```python
import streamlit as st

st.set_page_config(page_title="My Blog Post", layout ='wide')

st.title("Building My First Streamlit Blog Page")
st.markdown("**Author:** John Doe | 📅 August 16, 2025")

st.markdown("---")

st.header("Introduction")
st.markdown("""
Welcome to my first blog post built with **Streamlit**!  
In this post, I’ll walk you through how I created a simple blog page using 
Streamlit’s `st.markdown()` feature.
""")
```

This is a blog post about Streamlit! It's a great way to build interactive web apps using Python.

_Here are some reasons why Streamlit is awesome:_

-   Easy to learn
    
-   Fast development
    
-   Great for data science projects
    
**Different Text Formats**

-   `st.markdown(...)`: This function renders Markdown text. The triple quotes (`"""`) allow you to write multi-line strings.
    
-   `## Introduction`: This creates a level 2 heading in Markdown.
    
-   `*Here are some reasons...`: This creates an unordered list.
    
-   `**Let's try some emojis!** 🎉 🚀`: This displays bold text with emojis.
    
-   `_This is italicized text._`: This displays italicized text.
    
-   `**This is bold text.**`: This displays bold text.
    
-   `st.write("---")`: This creates a horizontal line to visually separate sections.
    

**Expected Output:**

The Streamlit app will display a blog post with a title, publication date, an introduction with a heading, a bulleted list, emojis, and examples of italicized and bold text.

**Key Takeaways:**

-   Use `st.markdown` to display formatted text using Markdown.
    
-   Use headings (`#`, `##`, `###`) to structure your content.
    
-   Use lists (`*`, `-`, `1.`) to create bulleted or numbered lists.
    
-   Use `**bold**` and `_italic_` for text styling.
    
-   Use emojis to add visual appeal.

----------

### Topic 2.3 Code & Formulas

**Introduction**  
Some apps are teaching tools, dashboards, or scientific platforms. In such cases, plain text won’t cut it—you need structured code and math.

-   `st.code()`  → Think of it as a  **digital blackboard for your code**. Instead of messy plain text, it formats your code with colors and indentation, making it readable, copy-friendly, and professional.
    
-   `st.latex()`  → Designed for math lovers! Just like how professors neatly write formulas on the board, LaTeX lets you present math beautifully. Users don’t just “see” the formula—they understand it.
    

Apps that  **teach, train, or calculate**  need this neat formatting. Just imagine searching for the quadratic formula and finding it as plain text like “x=(-b±√(b^2-4ac))/2a”. Painful to read. With  `st.latex()`, it looks like a real math book.

**Pro Tip**: Use  `st.code()`  for tutorials, code samples, or examples. Use  `st.latex()`  when equations need visual clarity. Both help you  **gain users’ trust**  by looking polished and professional.

### Mini Project: Math Formula Helper


Streamlit can render LaTeX equations, making it perfect for displaying mathematical formulas. 
Let's create a simple app that displays some common formulas.

```python
import streamlit as st

st.title("Math Formula Helper")

st.write("Here are some useful formulas:")

st.latex(r'''
    a + b x^2 + c
    ''')

st.latex(r'''
    \int_a^b f(x) \,dx
    ''')

st.latex(r'''
    e^{i\pi} + 1 = 0
    ''')

```

**Explanation:**

-   `st.latex(...)`: This function renders LaTeX code as a mathematical formula.
    
-   `r'''...'''`: The `r` prefix indicates a raw string, which prevents Python from interpreting backslashes as escape sequences. This is important for LaTeX code, which uses backslashes extensively.
    
-   The LaTeX code within the triple quotes defines the mathematical formulas.
    

**Expected Output:**

The Streamlit app will display the title "Math Formula Helper" followed by the three LaTeX equations, rendered as mathematical formulas.

**Key Takeaways:**

-   Use `st.latex` to display mathematical formulas.
    
-   Use raw strings (`r'''...'''`) to prevent Python from interpreting backslashes in LaTeX code.
    
-   Learn basic LaTeX syntax to create different mathematical expressions.
----------

### Topic 2.4 Status Messages

**Introduction**  
Apps don’t just show results—they also  **talk back**  to users. And the way they talk matters. Imagine booking a ticket, and at the end, the app is silent. Did it work? Did it fail? Should you retry?

This is where status messages come in. They’re your app’s  **traffic signals**:

-   🟢  **Success (`st.success()`)**  → Confirms things went well (like “Payment successful!”).
    
-   🔵  **Info (`st.info()`)**  → Shares neutral helpful updates (e.g., “Your report is being generated”).
    
-   🟡  **Warning (`st.warning()`)**  → Alerts about potential issues but doesn’t stop the process (e.g., “Network is slow, results might take time”).
    
-   🔴  **Error (`st.error()`)**  → Tells users something failed (like “Invalid password!”).
    

These functions don’t just show messages—they  **build trust**. A user who receives clear feedback feels in control and safe. Without it, they feel confused and abandoned.

**Pro Tip**:

-   Success/information = Encourage and motivate users.
    
-   Warning = Prepare them gently, suggest action.
    
-   Error = Be direct but helpful (tell them how to fix it, not just what’s wrong).
    
### Mini Project: Customer Support Panel


Status messages are useful for providing feedback to users about the progress of a task or the status of a system. Streamlit provides functions for displaying info, warning, and error messages. Let's create a customer support panel that shows different types of messages.

```python
import streamlit as st
import time

st.title("Customer Support Panel")

ticket_id = st.text_input("Enter Ticket ID:")

if ticket_id:
    st.info(f"Ticket ID: {ticket_id}")
    st.warning("Please wait while we process your request.")
    time.sleep(2) # Simulate processing time
    st.success("Your request has been processed successfully!")
    st.error("There might be a slight delay in the update. Please check again in 5 minutes.")

```

**Explanation:**

-   `st.info(...)`: Displays an informational message.
    
-   `st.warning(...)`: Displays a warning message.
    
-   `st.success(...)`: Displays a success message.
    
-   `st.error(...)`: Displays an error message.
    
-   `time.sleep(2)`: This pauses the execution of the code for 2 seconds, simulating a processing delay.
    

**Expected Output:**

The Streamlit app will display a text input field for entering a ticket ID. When a ticket ID is entered, it will display an info message with the ticket ID, followed by a warning message. After a 2-second delay, it will display a success message, and finally an error message indicating a potential delay in the update.

**Key Takeaways:**

-   Use `st.info` to display informational messages.
    
-   Use `st.warning` to display warning messages.
    
-   Use `st.success` to display success messages.
    
-   Use `st.error` to display error messages.
    
-   Use status messages to provide feedback to users and improve the user experience.
----------

### **Conclusion**

-   Text is structure + style + feedback.
    
-   Headings organize, Markdown styles, code/math explain, and messages guide.
    
-   Good text = Clear app navigation + engaging communication + user confidence.
    

 In short, treat your app’s text as a  **conversation with the user**—guide them, reassure them, and keep them engaged.
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

col1,col2=st.columns(2)

with col1:
    st.header("Starters")
    st.write("Cheese Burger")
    st.write("Cheese Sandwich")
    st.write("Hot Dog")
    st.write("Chicken Sandwich")

    st.header("Main Course")
    st.write("Steak ")
    st.write("Pasta Carbonara")

    st.subheader("Desserts")
    st.write("Chocolate Cake")
    st.write("Ice Cream ")

with col2:
    st.header("")
    st.write("$34")
    st.write("$21")    
    st.write("$30")
    st.write("$34")

    st.header("")
    st.write("$40")
    st.write("$54")

    st.subheader("")
    st.write("$25")
    st.write("$20")
```

**Explanation:**

-   `st.title("Welcome to Our Restaurant!")`: This displays the main title of the app, making it clear what the app is about.
    
-   `st.header("Starters")`: This creates a header for the "Starters" section. Headers are larger and bolder than regular text, helping to visually separate sections.
    
-   `st.subheader("Desserts")`: This creates a subheader for the "Desserts" section. Subheaders are smaller than headers but still useful for further dividing content.
    
-   `st.write(...)`: This displays the menu items and their prices. `st.write` is a versatile function that can display text, numbers, dataframes, and more.
    

**Expected Output:**

The Streamlit app will display a title "Welcome to Our Restaurant!", followed by headers for "Starters" and "Main Course", and a subheader for "Desserts". Each section will list the menu items and their prices.

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%202/restaurant.png">

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

st.set_page_config(page_title="My Fitness Blog", layout="centered")

st.title("🏋️ My Fitness Journey")
st.markdown("**Author:** John Doe | 📅 Sept 6, 2025")
st.markdown("---")

st.header("🌟 Why I Started")
st.markdown("""
I wanted **more energy**, *better health*, and a stronger body.  
Sitting all day was taking its toll, so I committed to change. 💪
""")

st.header("💪 My Routine")
st.markdown("""
- 🏃 **Cardio**: 3 times a week  
- 🏋️ **Strength Training**: 4 times a week  
- 🧘 **Stretching**: every day  
""")

st.header("🥗 Nutrition")
st.markdown("""
> *"You can’t out-train a bad diet."*  
I focus on whole foods, hydration 💧, and balance — but I still enjoy a 🍕 sometimes!
""")

st.header("💡 Key Lesson")
st.markdown("""
✅ **Consistency > Motivation**  
Small daily habits compound into big results over time.
""")

st.success("🚀 Stay strong, stay consistent, and enjoy the process!")

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

<img src ="https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%202/blog1.png">

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

st.title("📘 Aptitude Formula Cheatsheet")
st.write("Quick reference for common aptitude formulas 🧮")

# Section 1: Percentages
st.header("📊 Percentages")
st.latex(r"\text{Percentage (\%)} = \frac{\text{Value}}{\text{Total}} \times 100")
st.latex(r"\text{Profit \%} = \frac{\text{Profit}}{\text{Cost Price}} \times 100")
st.latex(r"\text{Loss \%} = \frac{\text{Loss}}{\text{Cost Price}} \times 100")

# Section 2: Simple & Compound Interest
st.header("💰 Interest")
st.latex(r"SI = \frac{P \times R \times T}{100}")
st.latex(r"CI = P \times \left(1 + \frac{R}{100}\right)^T - P")
st.caption("where P = Principal, R = Rate %, T = Time")

# Section 3: Averages
st.header("📈 Averages")
st.latex(r"\text{Average} = \frac{\text{Sum of terms}}{\text{Number of terms}}")

# Section 4: Probability
st.header("🎲 Probability")
st.latex(r"P(E) = \frac{\text{Favorable outcomes}}{\text{Total outcomes}}")

# Section 5: Permutations & Combinations
st.header("🔢 Permutations & Combinations")
st.latex(r"nPr = \frac{n!}{(n-r)!}")
st.latex(r"nCr = \frac{n!}{r!(n-r)!}")

st.success("✅ Cheatsheet ready! Use this as a quick reference during practice.")


```

**Explanation:**

-   `st.latex(...)`: This function renders LaTeX code as a mathematical formula.
    
-   `r'''...'''`: The `r` prefix indicates a raw string, which prevents Python from interpreting backslashes as escape sequences. This is important for LaTeX code, which uses backslashes extensively.
    
-   The LaTeX code within the triple quotes defines the mathematical formulas.
    

**Expected Output:**

The Streamlit app will display the title "Math Formula Helper" followed by the three LaTeX equations, rendered as mathematical formulas.

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%202/math1.png">

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

# Page config
st.set_page_config(page_title="Customer Support Panel", layout="wide")

st.title("💬 Customer Support Panel")

st.write("Welcome! Submit your issue below and track support status.")

# User issue form
with st.form("support_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Email")
    issue = st.text_area("Describe your issue")
    submitted = st.form_submit_button("Submit Ticket")

if submitted:
    if not name or not email or not issue:
        st.error("⚠️ Please fill out all fields before submitting.")
    else:
        st.success(f"✅ Ticket submitted successfully! A support agent will contact {email}.")
        st.info("📌 Your Ticket ID: #12345")

st.subheader("📂 Support History")
st.chat_message("user").write("I am facing login issues.")
st.chat_message("assistant").write("Thanks for reporting. We are checking it.")
st.chat_message("user").write("Any update?")
st.chat_message("assistant").write("✅ Issue fixed. Please try again.")

```

**Explanation:**

-   `st.info(...)`: Displays an informational message.
    
-   `st.warning(...)`: Displays a warning message.
    
-   `st.success(...)`: Displays a success message.
    
-   `st.error(...)`: Displays an error message.
    
-   `time.sleep(2)`: This pauses the execution of the code for 2 seconds, simulating a processing delay.
    

**Expected Output:**

The Streamlit app will display a text input field for entering a ticket ID. When a ticket ID is entered, it will display an info message with the ticket ID, followed by a warning message. After a 2-second delay, it will display a success message, and finally an error message indicating a potential delay in the update.

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%202/customerpanel.png">

**Key Takeaways:**

-   Use `st.info` to display informational messages.
    
-   Use `st.warning` to display warning messages.
    
-   Use `st.success` to display success messages.
    
-   Use `st.error` to display error messages.
    
-   Use status messages to provide feedback to users and improve the user experience.

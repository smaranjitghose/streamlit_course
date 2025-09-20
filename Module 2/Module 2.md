
# Module 2: Displaying Text and Information

### Topic 2.1: Titles & Headings


<br>

#### **Introduction**

Visual hierarchy is the arrangement of text and sections to show their relative importance. Think of it like organizing a filing cabinet—everything has its proper place and level of importance.

Clear visual hierarchy is essential for creating professional, scannable applications that guide users through content logically. Just as a well-structured document uses headings and sections to organize information, Streamlit apps need proper hierarchy to prevent content from appearing scattered and confusing.

Streamlit provides a simple but effective hierarchy system:

-   **Title** (`st.title`) – The main identity of your page, used once
-   **Header** (`st.header`) – Major section dividers that break up content
-   **Subheader** (`st.subheader`) – Smaller sections within each major area
-   **Divider** (`st.divider`) – Visual breathing room between unrelated content

This top-down arrangement ensures users can navigate your app intuitively, finding information exactly where they expect it to be.

#### **Mini Project**

You're a data analyst in today's competitive job market, tired of sending static PDF resumes that get lost in the pile. You want something that stands out—a modern, interactive digital resume that showcases both your technical skills and creative thinking. Instead of another boring document, you'll create a shareable Streamlit app that recruiters can explore with just a click.

##### **Project Setup**

Create a new file called `app.py`:

```python
import streamlit as st

st.title("Rohit Raghuvanshi – Data Analyst")
st.write("Transforming complex data into actionable business insights")

st.divider()

st.header("🎓 Education")
st.subheader("Master of Science in Data Analytics")
st.write("MIT | 2019-2021 | GPA: 3.8/4.0")

st.divider()

st.header("📞 Contact")
st.write("📧 rohit.raghuvanshi@email.com")
st.write("💼 linkedin.com/in/rohit")
st.write("🐙 github.com/rohit")

```

**Run your app with:**

```bash
streamlit run app.py

```
----

##### **Output**



<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%202/resume1mod2.png">


---

#### **Step-by-Step Walkthrough**

Let's examine how each function creates the professional structure:

- **`st.title("Rohit Raghuvanshi – Data Analyst")`**: This creates the most prominent heading on your page—the main identity. Notice how we use it only once at the very top. This immediately tells visitors who you are and what you do.

- **`st.write("Transforming complex data into...")`**: A brief tagline that provides context. This sits naturally below the title, giving a quick professional summary without competing with the main heading.

- **`st.divider()`**: These horizontal lines create visual breathing room between major sections. Without them, your resume would feel cramped and hard to scan. Each divider signals "this section is complete, here's something new."

- **`st.header("🎓 Education")`**: Headers mark the beginning of major resume sections. The emoji adds visual interest and helps with quick scanning—recruiters can instantly jump to the section they want.

- **`st.subheader("Master of Science...")`**: Subheaders break down each major section into specific items. Under "Education," each degree gets its own subheader, making individual qualifications easy to find.

---


#### **Key Learning Points**

-   **One title rule**: Use `st.title()` only once per app to establish clear identity and avoid visual confusion
  
-   **Logical grouping**: Headers should represent major categories of information that naturally belong together
   
-   **Breathing room matters**: Dividers prevent cognitive overload by giving users visual breaks between unrelated content

-   **Scannable structure**: Users should be able to quickly jump to any section without reading everything in order

---

#### **Conclusion**

Structuring your app with `st.title()`, `st.header()`, and `st.subheader()` gives it instant polish and clarity. These simple commands are the foundation for building professional-looking dashboards and tools that are intuitive for any user.

-----


### Topic 2.2: Markdown


<br>

#### **Introduction**

**Markdown** is a lightweight formatting language that transforms plain text into polished, professional content with just a few simple symbols. Instead of writing complex HTML or CSS, you can make text bold, create lists, add headings, and structure your content using intuitive shortcuts that feel natural to write. In Streamlit, the `st.markdown()` function unlocks this formatting power, letting you create visually appealing applications that look professional without any design expertise. Whether you're highlighting key insights in a data report or organizing information in a clear hierarchy, markdown helps your content stand out and stay organized.


---

#### **Mini Project**

Every morning at Sunrise Café, Sarah faces the same problem: outdated menus. Customers constantly ask about daily specials, updated prices and allergens information, while the endless cycle of reprinting is costly and laborious. Sarah needs a digital solution that can be updated instantly, making her café more efficient, modern, and eco-friendly.

To simulate this challenge and build a solution, let's create a Streamlit application that serves as a dynamic, digital menu.

##### **Project Setup**

Create a new file called `app.py`:

```python
import streamlit as st

st.title(":orange[:material/restaurant: Sunrise Café]")
st.markdown(":small[:material/wb_sunny: Fresh Daily Specials - Updated Live!]")

st.divider()

st.markdown("""
## 🌟 Today's Special  
**Masala Chai Latte** :material/local_cafe: — :violet-background[₹120]  
:small[_A comforting blend of spices, tea & milk — café’s signature favorite_]
""")

st.divider()

st.markdown("""
### :material/emoji_food_beverage: Appetizers  
- **Avocado Toast** :avocado: — :green-background[₹220]  
  :small[_Multigrain bread with fresh avocado and lime_]  

- **Paneer Tikka Bites** :material/local_fire_department: — :blue-badge[₹180]  
  :small[_Spicy marinated paneer cubes grilled to perfection_]
""")

st.divider()

st.markdown("""
### :cake: Desserts  
- **Chocolate Brownie** :chocolate_bar: — :red-background[₹150]  
- **Seasonal Fruit Tart** :strawberry: — :yellow-badge[₹170]  
""")

st.divider()
st.markdown(":material/eco: :green[Eco-friendly digital menu — no reprints needed!]")

```

**Run your app with:**

```bash
streamlit run app.py
```

---

##### **Output**

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%202/mod2menu1.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%202/mod2menu2.png">


----

#### **Step-by-Step Walkthrough**

Let's examine how each markdown element enhances your menu's readability and appeal:

-   **`st.markdown()`** → Converts a string into GitHub-flavored Markdown. If something other than a string is passed, it’s converted with `str(body)`. Streamlit extends Markdown with :
    
    -   **Emoji Shortcodes**: Use codes like `:wave:` to insert emojis.
    
    -   **Streamlit Logo**: Add the official Streamlit logo with `:streamlit:`.
        
    -   **Typographical Symbols**: Automatically converts symbols like `->` to a proper arrow (`→`).
        
-   **Headings with Icons & Colors** → You can style headings using color + icons.  
    Example: `:orange[:material/restaurant: Sunrise Café]` creates an orange title with a restaurant icon.
    
-   **Small Text** → Use `:small[]` for footnotes or subtle text.  
    Example: `:small[:material/wb_sunny: Fresh Daily Specials - Updated Live!]`.
    
-   **Multi-line Markdown** → Triple quotes `""" """` let you format multiple lines in one call.
-   **Bulleted Lists** → Start lines with `-` for clean menus.  
    Example: `- **Avocado Toast** :avocado: — :green-background[₹220]`.
    
-   **Italics for Descriptions** → Use `_..._` inside `:small[]` to style descriptions differently.  
    Example: `:small[_Multigrain bread with fresh avocado and lime_]`.
    
-   **Badges for Prices** → Highlight prices with colored tags.  
    Example: `:blue-badge[₹180]` or `:yellow-badge[₹170]`.
    
-   **Icons for Emphasis** → Add flair with emoji shortcodes (`:avocado:`) or Material icons (`:material/eco:`)
---

#### **Conclusion**

`st.markdown()` empowers you to transform plain text into polished, structured, and visually engaging content that guides users naturally through your app. By using simple formatting like bold, italics, and lists, you can create hierarchy, highlight key points, and make information easier to digest. This makes your Streamlit applications not only more professional-looking but also more effective at communicating without any design expertise.

---

### Topic 2.3: Code & Formulae


<br>

#### **Introduction**

While building educational apps or technical documentation, plain text alone often falls short in conveying complex ideas clearly. Code needs proper formatting to be readable, mathematical formulas demand precise typesetting, and important concepts should stand out from the surrounding details.

Streamlit provides functions designed for these needs:

-   **`st.code()`**: Displays code with proper formatting and syntax highlighting, making it easy to read and understand.
    
-   **`st.latex()`**: Renders mathematical expressions in clean, professional typeset, perfect for formulas or equations.
    
-   **`st.badge()`**: Highlights important points or status indicators, drawing attention to key concepts.
    
-   **`st.caption()`**: Adds supporting notes or context beneath content, helping users grasp additional details without cluttering the main text.

#### **Mini Project**

You're preparing for a competitive exam where you need to memorize dozens of mathematical formulas and their corresponding code implementations. Instead of flipping through multiple textbooks and notebooks, you want a single digital exam prep sheet that combines clean formulas, working code examples, and priority indicators all in one place. This would let you review everything efficiently during those crucial final study sessions.

##### **Project Setup**

Create a new file called `app.py`:

```python
import streamlit as st

st.title("🎓 CS Exam Prep Cheatsheet")

st.divider()
st.header("📐 Mathematics")

st.subheader("Quadratic Equation")
st.badge("Medium")
st.caption("General formula for solving ax² + bx + c = 0")

st.latex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
st.latex(r"ax^2 + bx + c = 0")

st.caption("Python implementation with an example")
st.code('''
import math

def solve_quadratic(a,b,c):
    d = b**2 - 4*a*c
    if d > 0: return (-b+math.sqrt(d))/(2*a), (-b-math.sqrt(d))/(2*a)
    if d == 0: return -b/(2*a)
    return "No real solutions"

print(solve_quadratic(1,-5,6))  # x² - 5x + 6 = 0
''', language='python')

```

**Run your app with:**

```bash
streamlit run app.py

```

##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%202/exam1mod2.png">



<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%202/exam2mod2.png">


---

#### **Step-by-Step Walkthrough**

Let's examine how each function enhances the presentation of technical information:

- **`st.latex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")`**: This renders mathematical formulas in clean, textbook-quality typography. The `r` before the string tells Python to treat it as a raw string, preventing backslashes from being interpreted as escape characters. LaTeX formatting makes complex mathematical expressions readable and professional.

- **`st.code()` with language parameter**: This function displays code with proper syntax highlighting, indentation, and a copy button for users. The `language="python"` parameter tells Streamlit to apply Python-specific color coding, making the code much easier to read than plain text.

- **Multi-line code blocks**: The triple quotes allow you to include complete, runnable code examples that demonstrate how to implement each formula. This bridges the gap between theoretical knowledge and practical application.

- **`st.badge("Medium")`**: These create small, visually distinct tags that help categorize or emphasize content. They're perfect for indicating difficulty levels, importance, or topic categories without disrupting the main content flow.

- **`st.caption("General formula for solving ax² + bx + c = 0")`**: Captions provide additional context or explanatory notes in a smaller, less prominent font. 

---

#### **Key Learning Points**

-   **LaTeX for professional formulas**: `st.latex()` renders mathematical expressions with the same quality as textbooks and academic papers

-   **Syntax highlighting improves readability**: `st.code()` with language specification makes code much easier to understand than plain text

-   **Badges provide visual hierarchy**: Use `st.badge()` to highlight important concepts without disrupting content flow

-   **Captions add context efficiently**: `st.caption()` lets you include helpful details without cluttering the main presentation

---

#### **Conclusion**

These specialized display functions transform technical content from confusing text blocks into clear, professional presentations. By combining `st.latex()` for formulas, `st.code()` for implementations, `st.badge()` for emphasis, and `st.caption()` for context, you can create educational resources that effectively communicate complex information.

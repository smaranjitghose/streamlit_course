# Module 7: Layouts & Structuring Apps

### Topic 7.1: Columns

<br>

#### **Introduction**

Imagine trying to compare two snacks at the store. If you look at one, put it back, and then walk over to check the other, you end up juggling details in your memory. But when both are side by side, the choice feels effortless—you can see ingredients, prices, and packaging at once. Our brains naturally handle information more easily this way because direct comparisons cut down on mental effort. 

Streamlit’s `st.columns()` works the same way for apps, letting you place related content next to each other, so comparisons feel clear, natural, and easy to follow. The `st.columns()` function transforms your linear app layout into flexible, side-by-side presentations. Instead of forcing users to scroll through information vertically, you can create intuitive comparison layouts where related information sits adjacent to each other. This spatial organization mirrors how we naturally think about choices and makes complex comparisons feel effortless by reducing mental load and enabling direct visual comparison.

#### **Mini Project** 

Imagine you’re shopping for a new phone but stuck choosing between two top models. Instead of scrolling through endless specs, what if you could see them side by side — their images, prices, features, pros, and cons — all in one clean dashboard?

In this project, you’ll build a smartphone comparison tool with Streamlit columns, where users can instantly spot differences, weigh trade-offs, and get an expert verdict. It’s like having your own tech reviewer right inside the app!

##### **Project Setup**

Create a new file `app.py`:

```python
import streamlit as st

st.title("📱 Smartphone Comparison Tool")
st.write("Compare phones side-by-side to make informed decisions")

# Product data
phones = [
    {
        'name': 'iPhone 15 Pro',
        'price': 'Rs. 90,999*',
        'image_url': 'https://cf-img-a-in.tosshub.com/sites/visualstory/wp/2024/08/iphone-15-pro-max-natural-titanium-desktop-detail-1-Format-488.png?size=*:900',
        'specs': {
            'Display': '6.1" Super Retina XDR',
            'Processor': 'A17 Pro chip',
            'Storage': '128GB / 256GB / 512GB / 1TB',
            'Camera': '48MP Main + 12MP Ultra Wide',
            'Battery': 'Up to 23 hours video',
            'Weight': '187g'
        },
        'pros': ['Premium titanium build quality', 'Excellent camera system', 
                 'Fast A17 Pro performance', 'Great ecosystem integration'],
        'cons': ['Higher price point', 'Limited customization', 
                 'No USB-C to Lightning adapter'],
        'verdict': 'Perfect for Apple users wanting premium build and top-tier cameras.',
        'rating': 4.5
    },
    {
        'name': 'Samsung S24 Ultra',
        'price': 'Rs. 97,999*',
        'image_url': 'https://cdn.beebom.com/mobile/samsung-galaxy-s24-ultra/samsung-galaxy-s24-ultra-front-back-5.png',
        'specs': {
            'Display': '6.8" Dynamic AMOLED 2X',
            'Processor': 'Snapdragon 8 Gen 3',
            'Storage': '256GB / 512GB / 1TB',
            'Camera': '200MP Main + 50MP Periscope',
            'Battery': 'Up to 30 hours video',
            'Weight': '232g'
        },
        'pros': ['S Pen included', 'Larger high-res display', 
                 'Superior zoom cameras', 'More storage options'],
        'cons': ['Heavier than competitors', 'Higher starting price', 
                 'Complex UI for some users'],
        'verdict': 'Best for power users needing S Pen, huge screen, and zoom cameras.',
        'rating': 4.7
    }
]

# Two-column layout
col1, col2 = st.columns(2)

for col, phone in zip([col1, col2], phones):
    with col:
        st.subheader(f"📱 {phone['name']}")
        st.image(phone['image_url'], use_container_width=True)
        st.metric("💰 Starting Price", phone['price'])
        
        st.write("**🔧 Key Specifications:**")
        for spec, val in phone['specs'].items():
            st.write(f"- **{spec}:** {val}")
        
        st.write("**✅ Pros:**")
        for pro in phone['pros']:
            st.write(f"- {pro}")
        
        st.write("**❌ Cons:**")
        for con in phone['cons']:
            st.write(f"- {con}")
        
        st.metric("⭐ Expert Rating", f"{phone['rating']}/5.0")
        st.write("**🎯 Final Verdict:**")
        st.write(phone['verdict'])

# Quick helper
st.divider()
st.subheader("🤔 Quick Decision Helper")
colA, colB = st.columns(2)

with colA:
    st.info("**Choose iPhone 15 Pro if you:**\n- Want seamless Apple ecosystem\n- Prefer compact premium design\n- Value consistent updates")

with colB:
    st.success("**Choose Galaxy S24 Ultra if you:**\n- Need S Pen for productivity\n- Want best zoom camera\n- Prefer larger screen & customization")

```

**Run your app with:**

```bash
streamlit run app.py
```

##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%207/col1mod7.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%207/col2mod7.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%207/col3mod7.png">

-----

#### **Step-by-Step Walkthrough**

-   **`st.columns()`**: Creates a multi-column layout, enabling side-by-side comparison instead of stacking content vertically.
    
-   **Column scoping (`with col:`)**: Ensures all elements inside render within that specific column, keeping each phone’s details aligned.
    
-   **`zip([col1, col2], phones)`**: Pairs each column with a phone entry so both devices are rendered in parallel without code duplication.
    
-   **Nested columns (`colA, colB = st.columns(2)`)**: Reused again for the “Quick Decision Helper,” showing how columns can organize content into clear comparison boxes.

#### **Conclusion**

The strategic use of `st.columns()` elevates basic Streamlit applications into professional-grade interfaces that maximize screen real estate while improving information hierarchy. This layout flexibility transforms single-purpose tools into comprehensive dashboards where metrics, comparisons, and controls coexist harmoniously, creating user experiences that rival dedicated business intelligence platforms while maintaining Streamlit's signature development simplicity.

----

### Topic 7.2: Tabs

<br>

#### **Introduction**

When applications grow more complex, they often contain multiple sections that users need to access quickly. Traditional web layouts typically rely on menus or separate pages, but these can feel cluttered and disrupt the flow of exploration. What users really want is the ability to focus on one section at a time while still being able to switch smoothly to related areas—without losing their context.

Streamlit’s `st.tabs()` provides exactly this solution. By dividing content into logical tabs, it creates clean and organized layouts where each section has its own space. Instead of overwhelming users with all content at once—or forcing them through multiple pages—tabs offer focused views with effortless navigation. This approach keeps interfaces tidy, intuitive, and familiar while ensuring users stay engaged with the content that matters most.

#### **Mini Project**

You're building an investment dashboard to help users monitor multiple asset classes in one place.

They need to track Indian and US stocks, follow cryptocurrency performance, and review ETF allocations—all with the right metrics and visualizations. By organizing these views into clean, switchable tabs, users can move seamlessly between categories while keeping a clear picture of their overall portfolio.

##### **Project Setup**

Create a new file `app.py`:

```python
import streamlit as st
import pandas as pd
import numpy as np

st.title("📈 Investment Portfolio Dashboard")
st.write("Organize your investments into clean sections with tabs")

# Sample dates for charts
dates = pd.date_range("2024-01-01", periods=30, freq="D")

# Tabs for different asset classes
tab1, tab2, tab3, tab4 = st.tabs(["🇮🇳 Stocks India", "🇺🇸 Stocks US", "₿ Crypto", "📊 ETFs"])

# --- Tab 1: Indian Stocks ---
with tab1:
    st.header("Indian Stock Holdings")
    st.metric("Total Value", "₹2,45,000", "+₹12,500")
    
    data = pd.DataFrame({
        "Date": dates,
        "Value": np.cumsum(np.random.randn(30) * 1000) + 200000
    })
    st.line_chart(data.set_index("Date"))

# --- Tab 2: US Stocks ---
with tab2:
    st.header("US Stock Holdings")
    st.metric("Total Value", "$45,600", "+$2,100")
    
    data = pd.DataFrame({
        "Date": dates,
        "Value": np.cumsum(np.random.randn(30) * 500) + 40000
    })
    st.line_chart(data.set_index("Date"))

# --- Tab 3: Cryptocurrency ---
with tab3:
    st.header("Cryptocurrency Holdings")
    st.metric("Total Value", "$12,400", "-$800")
    
    data = pd.DataFrame({
        "Date": dates,
        "Value": np.cumsum(np.random.randn(30) * 400) + 10000
    })
    st.line_chart(data.set_index("Date"))

# --- Tab 4: ETFs ---
with tab4:
    st.header("ETF Holdings")
    st.metric("Total Value", "$28,900", "+$450")
    
    data = pd.DataFrame({
        "Date": dates,
        "Value": np.cumsum(np.random.randn(30) * 200) + 25000
    })
    st.line_chart(data.set_index("Date"))

```

**Run your app with:**


```bash
streamlit run app.py
```
----

##### **Output**

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%207/tabs1mod7.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%207/tabs2mod7.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%207/tabs3mod7.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%207/tabs4mod7.png">


----
#### **Step-by-Step Walkthrough**

-   **Numpy (Numerical Python):** is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

-   Generating random numbers to simulate daily investment value changes `np.random.randn()`

-   Calculating cumulative sums to show portfolio growth over time `np.cumsum()`

-   **`st.tabs(["🇮🇳 Stocks India", "🇺🇸 Stocks US", "₿ Crypto", "📊 ETFs"])`**: Creates four tab objects (`tab1, tab2, tab3, tab4`) for different asset classes.
    
-   **`with tab1:` / `with tab2:` / ...**: Directs all subsequent Streamlit elements (headers, metrics, charts) into the respective tab.
    
-   **Consistent structure across tabs:** By repeating a uniform layout (header → metric → chart) inside each tab, users develop expectations and can navigate the dashboard intuitively.
    
-   **Content isolation**: Each tab shows only its assigned content without affecting other tabs.
    
-   **Seamless switching**: Users can move between tabs without losing displayed data or app state.
    

----------

#### **Conclusion**

`st.tabs()` transforms Streamlit apps by **organizing complex, multi-category content into clean, navigable sections**. It improves usability by letting users **switch seamlessly between logical groups**, keeps dashboards uncluttered, and ensures that analytical workflows remain focused and efficient. This approach is ideal for multi-asset dashboards, comparison tools, or any interface where related but distinct information must coexist in a single app.


----

### Topic 7.3: Expanders

<br>

#### **Introduction**

Too much visible information on a page can easily feel overwhelming, making it harder for users to focus on what truly matters. Often, people prefer to see just the essentials first and then choose to dive deeper only when they need more detail. This approach, known as  _progressive disclosure_, helps reduce distractions while keeping everything accessible.

Streamlit’s  `st.expander()`  brings this idea into practice by creating collapsible sections that stay hidden until clicked. This simple yet powerful feature keeps interfaces clean, organized, and easy to navigate, while still allowing users to reveal additional content whenever they need it.

#### **Mini Project**

You're building a customer support FAQ page for a software company. Users arrive with specific problems and need quick answers. You'll create an organized FAQ system where each question appears as a clickable header, and the detailed answer (including step-by-step instructions and links) only shows when the user needs it, keeping the page clean and scannable.

##### **Project Setup**

Create a new file `app.py`:


```python
import streamlit as st

st.title("🆘 Customer Support FAQ")
st.write("Click on any question below to reveal the answer")

# FAQ list
faqs = [
    {
        "question": "🔑 How do I reset my password?",
        "answer": """
**Steps to reset your password:**
1. Go to the login page and click "Forgot Password"
2. Enter your registered email
3. Check your email for the reset link
4. Click the link and create a new password

**Need help?** Contact support@company.com
"""
    },
    {
        "question": "👤 My account is locked or suspended",
        "answer": """
**Possible reasons:**
- Too many failed login attempts
- Suspicious activity detected
- Payment issues

**What to do:**
1. Wait 30 minutes if multiple failed logins
2. Check your email for security notifications
3. Contact security@company.com if still locked
"""
    },
    {
        "question": "📞 How can I contact customer support?",
        "answer": """
**Email Support:** support@company.com  
**Live Chat:** Mon-Fri 9 AM–6 PM via website  
**Phone Support:** 1-800-SUPPORT, Mon-Fri 8 AM–8 PM EST
"""
    }
]

# Render FAQs with expanders
for faq in faqs:
    with st.expander(faq["question"]):
        st.markdown(faq["answer"])

st.divider()
st.info("💡 Didn't find what you're looking for? Email support@company.com for help!")


```

**Run your app with:**

```bash
streamlit run app.py
```
-----

##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%207/expander1mod7.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%207/expander2mod7.png">

----

#### **Step-by-Step Walkthrough**

-   **`st.expander("Question")`**: Creates a collapsible section for each FAQ item. Users can click the question to reveal or hide the answer, keeping the interface clean and interactive.
    
-   **Interactive content display**: Inside the expander, you can use any Streamlit element (like `st.markdown()` as we have used it in the app), allowing rich formatting while still maintaining a compact layout.
    

This functionality is ideal for FAQs, step-by-step instructions, or any scenario where users should focus on one piece of information at a time without overwhelming the page.


#### **Conclusion**

The power of `st.expander()` lies in shifting control from the application to the user, enabling self-directed exploration of content at individual pace and interest levels. This approach eliminates information overwhelm while ensuring comprehensive coverage, creating applications that serve both quick reference needs and detailed learning requirements through the same intuitive interface that adapts to diverse user goals.

----

### Topic 7.4: Sidebar

<br>

#### **Introduction**

The sidebar in Streamlit provides a dedicated space for user controls, keeping your main content area clean and focused. Instead of mixing input widgets with your data displays, the sidebar creates a clear separation between user interactions and results. This organizational pattern is essential for building professional-looking applications that feel intuitive to users.

When users open your app, they immediately understand where to find controls (the sidebar) and where to view results (the main area). This visual hierarchy makes your applications more user-friendly and easier to navigate, especially as they grow in complexity.

#### **Mini Project**

You're building a movie recommendation system for a streaming service. Users need to filter through thousands of movies by genre, minimum rating, and release year to find their next watch. The sidebar will house all the filtering controls while the main page displays the matching movies.

##### **Project Setup**

Create a new file `app.py`:

```python
import streamlit as st

# Sample movie data
movies = [
    {"title": "The Matrix", "genre": "Sci-Fi", "rating": 8.7, "year": 1999},
    {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8, "year": 2010},
    {"title": "The Godfather", "genre": "Drama", "rating": 9.2, "year": 1972},
    {"title": "Pulp Fiction", "genre": "Drama", "rating": 8.9, "year": 1994},
    {"title": "Toy Story", "genre": "Animation", "rating": 8.3, "year": 1995},
    {"title": "Finding Nemo", "genre": "Animation", "rating": 8.2, "year": 2003}
]

st.title("Movie Recommendations")

# Sidebar filters
genre = st.sidebar.selectbox("Choose Genre", ["All", "Sci-Fi", "Drama", "Animation"])
min_rating = st.sidebar.slider("Minimum Rating", 0.0, 10.0, 7.0)
min_year = st.sidebar.number_input("From Year", min_value=1900, max_value=2024, value=1990)

# Filter movies
filtered_movies = []
for movie in movies:
    if (genre == "All" or movie["genre"] == genre) and \
       movie["rating"] >= min_rating and \
       movie["year"] >= min_year:
        filtered_movies.append(movie)

# Display results
st.write(f"Found {len(filtered_movies)} movies:")
for movie in filtered_movies:
    st.write(f"**{movie['title']}** ({movie['year']}) - {movie['genre']} - Rating: {movie['rating']}")
```

**Run your app with:**
```
streamlit run app.py
```
---

##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%207/sidemod7.png">


-----

#### **Step-by-Step Walkthrough**

-   **`st.sidebar.selectbox("Choose Genre", [...])`**: Adds a dropdown menu in the sidebar for genre selection, keeping the main page uncluttered while letting users filter movies easily.
    
-   **`st.sidebar.slider("Minimum Rating", 0.0, 10.0, 7.0)`**: Provides an interactive slider in the sidebar to set the minimum movie rating. Users can adjust numeric thresholds without affecting the main results area.
    
-   **`st.sidebar.number_input("From Year", min_value=1900, max_value=2024, value=1990)`**: Adds a precise numeric input in the sidebar for selecting the starting year. Ensures controlled input with min, max, and default values.
    
-   **Sidebar separation**: Placing controls in the sidebar organizes user inputs independently from the main display, making the interface cleaner and more user-friendly.
    
-   **Input-driven filtering**: Sidebar inputs are passed to the main script’s filtering logic, dynamically updating the displayed list of movies based on user selections.

#### **Conclusion**

The sidebar transforms your Streamlit apps from simple scripts into organized applications. By moving input controls to a dedicated area, you create a clear user interface pattern that scales well as your applications grow more complex. Users immediately understand where to interact with your app and where to view results, making the entire experience more intuitive and professional.

----

### Topic 7.5: Containers & Placeholders

<br>

#### **Introduction**

You know that annoying thing when you click a button in an app and it just keeps adding more stuff to the screen? Click three times and you get three results piled up. Good apps don't do this - when something needs to update, it replaces the old info cleanly instead of making a mess.

Streamlit containers and placeholders let you control this. Placeholders are spots you can update in place - perfect for things like counters or status messages. Containers group things together and let you keep adding to them - great for lists or feeds. With these two tools, your apps start looking clean and working the way users expect.

#### **Mini Project**

You're building a live sports scoreboard that shows the current game score and a running feed of commentary. The score needs to update in place (replacing old scores), while commentary should accumulate below it (appending new updates). This demonstrates when to use placeholders versus containers.

##### **Project Setup**

Create a new file `app.py`:

```python
import streamlit as st
import time

st.title("Live Sports Scoreboard")

# Create placeholder for score (will replace content)
score_placeholder = st.empty()

# Create container for commentary (will append content)
with st.container():
    st.subheader("Live Commentary")
    commentary_area = st.container()

# Simulate live updates
if st.button("Start Game Simulation"):
    # Game data
    home_team = "Lakers"
    away_team = "Warriors"
    
    # Simulate score updates
    for quarter in range(1, 5):
        home_score = quarter * 25 + (quarter * 3)
        away_score = quarter * 23 + (quarter * 2)
        
        # Update score (replaces previous score)
        score_placeholder.metric(
            label=f"Quarter {quarter}",
            value=f"{home_team} {home_score} - {away_score} {away_team}"
        )
        
        # Add commentary (appends to container)
        with commentary_area:
            st.write(f"⏰ End of Quarter {quarter}: Great plays from both teams!")
            if quarter == 2:
                st.write("🏀 Halftime: Players heading to locker rooms")
            elif quarter == 4:
                st.write("🎉 Game Over! What an exciting finish!")
        
        time.sleep(2)  # Simulate real-time delay
```

**Run your app with:**
```
streamlit run app.py
```
---

##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%207/cont1mod7.png">

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%207/cont2mod7.png">


----

#### **Step-by-Step Walkthrough**


-   **`st.empty()`**: Creates a placeholder for dynamic content. Writing to it later replaces existing content, used here to **update the score each quarter** without stacking old scores.
    
-   **`st.container()`**: Creates a container that **accumulates content**. In the scoreboard, this holds the live commentary feed so each new line is appended rather than replacing previous text.
    
-   **`.metric()` with placeholders**: Calling `score_placeholder.metric()` **overwrites previous metrics**, keeping the score display clean and focused on the latest update.
    
-   **Context manager with containers (`with commentary_area:`)**: Ensures all new `st.write()` calls are **added inside the container**, building a chronological commentary feed that grows over time.

#### **Conclusion**

Containers and placeholders solve different layout problems in dynamic applications. Placeholders excel at showing current status or live data that should replace previous values, while containers organize related content that should accumulate over time. This combination gives you precise control over how your application updates, creating professional interfaces that update smoothly without overwhelming users with outdated information.

---

### Topic 7.6: Popovers

<br>

#### **Introduction**

Picture using a music app—you mostly just want to hit play and enjoy the song. But sometimes you might want to adjust the sound quality, shuffle the playlist, or check the lyrics. If all those options were crowded onto the main screen, it would feel overwhelming. Hide them completely, and you might never find them.

That’s where popovers come in. They keep the main interface clean and focused on what you use most, while neatly tucking extra controls into a small popup. With just a click, those secondary options appear when you need them—simple, easy, and clutter‑free.

#### **Mini Project**

You're building a comment box where users can leave feedback. The main focus is writing the comment, but users should also be able to set who can see it and add an emoji to show their mood. The popover will keep these options accessible but out of the way.

##### **Project Setup**

Create a new file `app.py`:

```python
import streamlit as st

st.title("Comment Box")

# Main comment input
comment = st.text_area("Leave a comment:", placeholder="What's on your mind?")

# Popover for additional settings
with st.popover("⚙️ Settings"):
    visibility = st.selectbox("Who can see this?", ["Everyone", "Friends Only", "Private"])
    mood = st.selectbox("Your mood:", ["😊 Happy", "😐 Neutral", "😢 Sad", "😍 Excited", "🤔 Thoughtful"])

# Submit and display
if st.button("Post Comment"):
    if comment:
        st.success("Comment posted!")
        
        # Display the comment with settings
        st.markdown("---")
        st.subheader("Your Comment")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"💬 {comment}")
        with col2:
            st.write(f"Visibility: {visibility}")
            st.write(f"Mood: {mood}")
    else:
        st.error("Please write a comment first!")
```
**Run your app with:**

`streamlit run app.py`

----

##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%207/pop1mod7.png">

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%207/pop2mod7.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%207/pop3mod7.png">


----

#### **Step-by-Step Walkthrough**

- **st.popover()** creates a clickable button that opens a popup window. The button shows "⚙️ Settings" but you can put any text or emoji. When clicked, it reveals the content inside without taking up permanent space on your page.

- **Inside the popover**, the selectbox widgets work exactly like normal, but they're hidden until the user clicks the popover button. This keeps the main interface focused on the comment text area while making additional options easily accessible.

- **The submit logic** uses both the main area input and the popover inputs together. Even though the settings are in a popup, their values are available just like any other widget, letting you combine everything when the user posts their comment.


#### **Conclusion**

Popovers help you build interfaces that feel both simple and powerful. By hiding secondary options in clickable popups, you avoid overwhelming users while still providing all the functionality they might need. This creates cleaner, more focused apps that don't sacrifice features for simplicity.

---

### Topic 7.7: Modal Dialog

<br>

#### **Introduction**

Ever been using an app when something pops up that demands your attention - like "Are you sure you want to delete this?" or "Please confirm your email address"? Your whole screen dims except for this small box, and you can't do anything else until you deal with it. That's a modal dialog at work.

Modal dialogs are like having a conversation where someone gently taps you on the shoulder and says "Hey, before you continue, I need you to focus on this one thing." They temporarily take over your screen to make sure important tasks get the attention they deserve, then politely step aside when you're done.

#### **Mini Project**

You're building an app and want users to easily report bugs when they find them. The main page should stay focused on your app's core features, but users need a quick way to submit detailed bug reports when something goes wrong.

##### **Project Setup**

Create a new file `app.py`:

```python
import streamlit as st

st.title("My Awesome App")
st.write("Welcome to the app! Click around and explore.")
st.write("If you find any bugs, please report them using the button below.")

# Bug report modal
@st.dialog("Bug Report")
def bug_report_form():
    st.write("Help us improve by reporting any issues you've found:")
    
    # Form fields
    title = st.text_input("Bug Title", placeholder="Brief description of the issue")
    severity = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
    description = st.text_area("Description", placeholder="What happened? What did you expect?")
    email = st.text_input("Your Email (optional)", placeholder="your@email.com")
    
    # Submit button
    if st.button("Submit Report", type="primary"):
        if title and description:
            st.success("Bug report submitted successfully!")
            st.write("**Your Report:**")
            st.write(f"**Title:** {title}")
            st.write(f"**Severity:** {severity}")
            st.write(f"**Description:** {description}")
            st.write(f"**Contact:** {email if email else 'Anonymous'}")
        else:
            st.error("Please fill in title and description")

# Button to open modal
if st.button("🐛 Report a Bug"):
    bug_report_form()
```

**Run your app with:**

```
streamlit run app.py
```

##### **Output**

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%207/bug1mod7.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%207/bug2mod7.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%207/bug3mod7.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%207/bug4mod7.png">


----

#### **Step-by-Step Walkthrough**

-   **`@st.dialog("Bug Report")`** — Decorates a function to become a modal dialog; the string is the modal title.
    
-   **Calling the decorated function (`bug_report_form()`)** — Opens the modal overlay immediately (no navigation away from the page).

-   **Modal focus & overlay behavior** — The modal captures user focus and overlays the page while preserving underlying app state (you can reopen it later without losing the page context).
    
-   **Synchronous validation & feedback** — Perform checks and show success/error messages inside the modal without a page reload; the modal is self-contained and reusable.


#### **Conclusion**

Modal dialogs are a powerful way to keep apps clean and user-friendly while still supporting important interactions. Whether it’s collecting input, confirming an action, or highlighting details, modals focus the user’s attention on the task at hand. By using them thoughtfully, you can deliver functionality without overwhelming the main interface.
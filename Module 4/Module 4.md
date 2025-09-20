# Module 4: Input & Interaction with Widgets

### Topic 4.1: Buttons


<br>

#### **Introduction**

Ever used a website where you could filter data, type something into a search bar, or click a button to see a result? Those little interactive components are called **widgets.** They're the magic that turns a static page into a dynamic application that responds to what you do. In Streamlit, widgets like buttons, sliders, text inputs, and checkboxes are your secret to building powerful, user-friendly tools. The moment a user interacts with a widget—say, by moving a slider or clicking a button—Streamlit automatically reruns your entire script from top to bottom. 

#### **Mini Project**

You’re at a lively party. In the corner stands a playful robot entertainer. Guests can walk up and press one of two big glowing buttons:
- Hit the **Balloon Button**, and the robot gleefully releases colorful balloons that float around, filling the room with a festive vibe.
- Press the **Snowflake Button**, and suddenly the space transforms into a magical winter scene, with snowflakes gently falling around you.

That’s exactly what MoodSwitch does in app form. With just one click, you can flip the entire mood — from festive fun to magical calm — showing how interactive buttons can instantly transform the experience.

##### **Project Setup**

Create a new file `app.py`:

```python
import streamlit as st

# App title
st.title("🌀 MoodSwitch")

st.write("Flip the vibe instantly — will it be balloons or snow?")

# Party Mode button
if st.button("🎈 Party Mode"):
    st.balloons()
    st.write("The mood is set: 🎉 It's party time with balloons!")

# Snow Mode button
if st.button("❄️ Snow Mode"):
    st.snow()
    st.write("The mood is set: ❄️ A magical winter wonderland begins!")
```

**Run your app with:**

```bash
streamlit run app.py
```
##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%204/mod4button1.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%204/mod4button2.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%204/mod4button3.png">

---

#### **Step-by-Step Walkthrough**

-   Buttons are interactive widgets that create event-driven user experiences - the `st.button()` function generates a clickable element that returns True only during the exact moment it's pressed, then immediately reverts to False, making buttons perfect for triggering instant actions.
    
-   In our **MoodSwitch** app, we have two separate `if` statements, each tied to a different button. When the **"🎈 Party Mode"** button is clicked, `st.button("🎈 Party Mode")` evaluates to `True`, and the code inside that block executes, calling `st.balloons()` to release a fun balloon animation across the screen.
    
-   Similarly, when the **"❄️ Snow Mode"** button is clicked, `st.snow()` is triggered, which creates a snowfall animation effect. These built-in Streamlit effects are designed to add delightful, interactive touches to your apps with just a single line of code.

----

#### **Key Learning Points**

- **User experience design:** Buttons should signal clear intent — use descriptive labels or emojis to make their purpose instantly obvious.

- **Grouping actions:** When multiple buttons exist, arrange them logically (e.g., side by side or under related sections) to reduce user confusion.

- **Feedback matters:** Pair buttons with visible outcomes (animations, status messages, or results) so users know their click was successful.

- **Scalability tip:** For many related actions, consider menus or radio buttons instead of crowding the interface with too many buttons.
----

#### **Conclusion**

Buttons are the foundation of interactivity in Streamlit. They turn a static app into a dynamic experience that responds to a user's direct input. With just a few lines of Python, you can give users the power to control your application, making your data-driven projects feel responsive and alive.

-----

### Topic 4.2: Basic Input Widgets


<br>

#### **Introduction**

User input transforms static applications into interactive experiences where people can provide their own data and see immediate results. Streamlit's basic input widgets—`st.text_input()` for capturing text and `st.number_input()` for numerical values—create the foundation for any application that needs to collect information from users. These widgets handle the complex mechanics of form processing automatically, returning clean Python variables that your code can use instantly.
What makes these input widgets powerful is their immediate responsiveness. The moment a user types a name or adjusts a number, your application updates to reflect those changes in calculations, charts, or processed results.

#### **Mini Project**

You're at dinner with friends enjoying good food and conversation. When the bill arrives, everyone pulls out their phones trying to calculate tips—"Is 18% of $47.50... wait, let me try again..." You watch the familiar scene of squinting at numbers and debating percentages. You'll build a simple tip calculator, **TipMate** that handles these calculations instantly, letting everyone get back to enjoying the evening without the mental math struggle.   


##### **Project Setup**

Create a new file `app.py`:

```python
import streamlit as st

# App Title
st.title("💸 TipMate")

st.write("No more mental math — calculate your tip in seconds!")

# Static bill amount
bill_amount = 1000.0  

# User inputs
name = st.text_input("👤 Enter Your Name")
tip_percent = st.number_input("💯 Enter Tip Percentage (%)", min_value=0.0, max_value=100.0, step=1.0)

# Calculations
tip_amount = (bill_amount * tip_percent) / 100
final_bill = bill_amount + tip_amount

# Bill Summary section
st.subheader("📊 Bill Summary")
st.metric(label="💵 Bill Amount", value=f"₹{bill_amount:.2f}")
st.metric(label="💰 Tip Amount", value=f"₹{tip_amount:.2f}")
st.metric(label="🧾 Final Bill (with Tip)", value=f"₹{final_bill:.2f}")

if name and tip_percent > 0:
    st.write(f"Thanks, {name}! Your tip is ₹{tip_amount:.2f}, making the total ₹{final_bill:.2f}.")

```

**Run your app with:**

```bash
streamlit run app.py

```
##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%204/mod4tip2.png">



---

#### **Step-by-Step Walkthrough**

-   The `st.text_input()` function creates an input field where users can type text. In this app, it’s used to capture the diner’s **name**. If the field is empty, it returns an empty string; once the user types something, the value updates instantly.
    
-   The `st.number_input()` function creates an input field that accepts numeric values. It takes several important parameters:
    
    -   `label` is what users see above the input field
        
    -   `min_value` sets the lowest acceptable number
        
    -   `max_value` sets the highest
        
    -   `step` determines how much the value changes when users click the up/down arrows.  
        In this app, it’s used to enter the **tip percentage**.
- When users type in these input fields or use the arrow buttons, Streamlit immediately captures the new values and stores them in the variables (`bill_amount` and `tip_percent`).


---

#### **Conclusion**

Understanding `st.text_input()` and s`t.number_input()` establishes your foundation for building interactive Streamlit applications. These functions demonstrate how effortlessly user input can drive application behavior, automatically validating data and updating results in real-time. With these core input capabilities mastered, you're ready to create responsive applications that adapt to user needs and provide immediate, personalized feedback. 

---

### Topic 4.3: Selection Elements


<br>

#### **Introduction**

Selection widgets transform open-ended user input into structured decision-making by presenting curated options that users can choose from with simple clicks, slides, or toggles. Unlike text input fields, selection widgets like `st.radio()`, `st.selectbox()`, `st.slider()`, and `st.checkbox()` eliminate guesswork and ensure valid inputs by constraining choices to predefined alternatives, reducing user errors and creating more predictable application behavior.
Each selection widget serves a specific purpose: `st.radio()` for single choices from small sets, `st.selectbox()` for longer option lists, `st.slider()` for numeric ranges, and `st.checkbox()` for binary decisions. Understanding these distinctions enables you to match the right widget to each decision type, creating interfaces that feel natural and reduce cognitive load for users.

#### **Mini Project**

You’re at a bustling coffee shop, and the barista hands you a tablet to place your order. You pick your favorite coffee type, choose the perfect size, slide to adjust the sweetness, and tap your favorite toppings. With each choice, the order updates instantly, giving you a fully customized drink exactly the way you like it.
You'll build an app, to let users customize their drinks using these selection elements.


##### **Project Setup**

Create a new file `app.py`:

```python
import streamlit as st

# Project title
st.title("🍩 Sip & Smile: Craft Your Drink")

# Coffee selection widgets
coffee_type = st.radio(
    "Choose your coffee type:",
    ["Espresso", "Latte", "Cappuccino"]
)

coffee_size = st.selectbox(
    "Select coffee size:",
    ["Small", "Medium", "Large"]
)

sugar = st.slider(
    "Sugar level (teaspoons):",
    min_value=0, max_value=5, step=1
)

whipped_cream = st.checkbox("Add whipped cream topping")

# Display order summary
st.subheader("📝 Your Coffee Order:")
order_summary = f"- {coffee_size} {coffee_type}\n- Sugar: {sugar} tsp"

# Add whipped cream only if selected
if whipped_cream:
    order_summary += "\n- With whipped cream 🍦"

st.write(order_summary)

```

**Run your app with:**

```bash
streamlit run app.py

```
##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%204/mod4coffee.png">

---

#### **Step-by-Step Walkthrough**

-   **`st.radio()`** function creates a set of radio buttons where users can select **exactly one option** from a provided list. It takes at least two parameters:
    
    -   `label`: The text displayed above the buttons.
        
    -   `options` (list): The set of choices users can pick from.  
        
-   **`st.selectbox()`** function creates a **dropdown menu**, which saves vertical space while offering multiple choices. Like `st.radio()`, it takes:
    
    -   `label`: The text shown above the dropdown.
        
    -   `options` (list): The set of values to choose from. 
        
-   **`st.slider()`** provides an intuitive way to select numeric values within a range. Users can drag the slider handle or click to jump to a specific value. Parameters include:
    
    -   `label`: Text shown above the slider.
        
    -   `min_value` / `max_value`: Define the numeric range.
        
    -   `step`: The increment for each move. 
        
-   **`st.checkbox()`** returns `True` when checked and `False` when unchecked, making it ideal for optional add-ons like whipped cream. It takes:
    
    -   `label`: Text displayed next to the checkbox.  
      

---

#### **Conclusion**

Mastering these fundamental selection widgets enables you to build Streamlit applications that guide users toward valid inputs while maintaining flexibility where needed. The key lies in understanding when to constrain choices and when to allow freedom, creating the optimal balance between usability and data integrity.

---

### Topic 4.4: Advanced Selection


<br>

#### **Introduction**

While basic selection widgets handle single choices effectively, many real-world applications require more sophisticated interaction patterns. Advanced selection widgets like `st.multiselect()`, `st.pills()`, and `st.feedback()` address scenarios where users need to select multiple options simultaneously, rate experiences, or interact with modern visual interfaces that traditional dropdowns cannot provide.
These specialized widgets fill specific gaps: `st.multiselect()`handles multiple simultaneous selections, `st.pills()` provides modern button-like visual choices, and `st.feedback()` standardizes rating collection. Each addresses distinct interaction needs that basic single-selection widgets cannot accommodate effectively.

#### **Mini Project**

You’re building a movie night planner that turns indecision into excitement. Users can pick all their favorite genres, choose the streaming platform they prefer, and get tailored film recommendations for the perfect night in. After watching, they can share feedback on the recommended movie.

##### **Project Setup**

Create a new file `app.py`:


```python
import streamlit as st

st.title("🎥 Movie Night Planner")

# Select multiple movie genres
genres = st.multiselect(
    "Select your favorite movie genres:",
    ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance"]
)

# Select streaming service using pills
service = st.pills(
    "Choose your preferred streaming service:",
    ["Netflix", "Hulu", "Disney+", "Amazon Prime"]
)

# Movie recommendations based on genre
recommendations = {
    "Action": "Extraction",
    "Comedy": "The Mask", 
    "Drama": "The Godfather",
    "Horror": "A Quiet Place",
    "Sci-Fi": "Interstellar",
    "Romance": "La La Land"
}

# Show recommendation if genres selected
if genres and service:
    recommended_movie = recommendations.get(genres[0], "Movie Not Found")
    st.subheader(f"🎬 Recommended: {recommended_movie}")
    st.write(f"Available on {service}")
    
    # Collect feedback using st.feedback
    st.write("Rate this recommendation:")
    feedback = st.feedback("stars")
    
    if feedback is not None:
        rating_text = ["Poor", "Fair", "Good", "Very Good", "Excellent"]
        st.write(f"Thanks for rating: {rating_text[feedback]} ({feedback + 1} stars)")
else:
    if not genres:
        st.write("Select at least one genre to get started.")
    if not service:
        st.write("Choose a streaming service to see recommendations.")
```

**Run your app with:**

```bash
streamlit run app.py
```

##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%204/mod4movie.png">



---

#### **Step-by-Step Walkthrough**

- The `st.multiselect()` function creates a dropdown that allows users to select multiple items from the provided list, returning a list of all selected options.

- The `st.pills()` function displays options as pill buttons, providing a modern, visually appealing way to select a single option. This creates a more engaging interface than traditional radio buttons.

- The `st.feedback()` function creates a star rating widget that returns an integer index (0-4) representing the selected star rating, making it perfect for collecting user feedback on recommendations.

- The conditional logic ensures recommendations appear only when both genres and streaming service are selected, creating a complete user input before showing results.

---

#### **Conclusion**

With `st.multiselect()`, `st.pills()`, and `st.feedback()` in your toolkit, you can handle the complex user interactions that single-choice widgets cannot accommodate. These advanced functions enable applications to capture multiple selections, visual preferences, and structured ratings, transforming simple interfaces into sophisticated tools that respond to nuanced user needs while maintaining reliable data collection.
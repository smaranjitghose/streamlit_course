# Module 4: Input & Interaction with Widgets

## Topic 4.1: Widgets

### What are Widgets?

Widgets are  **interactive components**  in Streamlit apps that allow users to input data or make selections. Examples include buttons, checkboxes, sliders, text inputs, dropdowns, and more.

### Widget Basics & Streamlit’s Rerun Model

-   Every time a user interacts with a widget,  **Streamlit reruns your entire script from top to bottom**, preserving widget states automatically.
    
-   Each widget returns its  **current value**  as a Python variable, which you can use to update the app.
    
-   This rerun model means you write simple, declarative Python code. When a widget changes, the entire app uses the new input to execute fresh and update the UI instantly.
    
-   Widgets have parameters like  `label`,  `default value`, and optional  `key`  (to uniquely identify and persist state).
    

This  **simplicity allows you to build complex, dynamic interfaces without callbacks or frontend code**.


### Tips on Widgets

-   Use  `st.text_input()`,  `st.slider()`,  `st.checkbox()`,  `st.selectbox()`, etc. to gather different types of user input.
    
-   Use  `st.sidebar.*`  variants to neatly organize input widgets in a sidebar panel.
    
-   Widgets can be controlled and accessed programmatically via  `st.session_state`  for advanced scenarios.
----------


### **Mini Project: Add a Button**

Streamlit makes it easy to add **interactive widgets** that respond to user actions. The simplest one is a **button**, which runs code when clicked.

- Create a fie `app.py`

```python
import streamlit as st

st.title("Widget Demo: Button")

if st.button("Say Hello"):
    st.write("Hello!")
else:
    st.write("Click the button to greet.")

``` 
----

**Run the app**
- `streamlit run app.py`
----------

### **Expected Output**

-   A **title**: “Widget Demo: Button”.
    
-   A **button** labeled _“Say Hello”_.
    
-   Before clicking → text shows _“Click the button to greet.”_
    
-   After clicking → text changes to _“Hello!”_
    

----------

### **Explanation**

-   **`st.button("Say Hello")`** → creates a clickable button.
    
-   The button **returns `True` only when clicked**, which triggers the first branch of the `if`.
    
-   On click → the app reruns and displays _Hello!_.
    
-   Otherwise → it prompts the user to click.
    
This demo helps learners see **Streamlit’s rerun behavior** in real-time: each interaction triggers a re-execution of the script.

---


## Topic 4.2: Button 


### Introduction

Buttons are fundamental interactive elements in almost every web or mobile app. They act as the  **main triggers**  for events—from submitting a form, starting a calculation, to triggering animations or fun visual effects.

In Streamlit, buttons are incredibly straightforward to use yet powerful. Each button creates a clickable widget that  **returns  `True`  only on the instant it is clicked**, causing Streamlit to rerun the script and update the app. This rerun model means that button clicks act as  **events**  that your app can respond to gracefully with simple, linear Python code — no complex frontend or callback management required.

Using buttons, you can build highly interactive and engaging apps with  **event-driven reactions**  like showing celebratory balloons, snow effects, or switching app modes. This immediate visual feedback creates a delightful user experience and solidifies the concept of interactivity for learners.

----------

### Mini Project : Celebration App with Buttons

This mini project demonstrates how to use Streamlit buttons to trigger  **fun, event-based effects**  that respond instantly to user input.

The app will have:

-   A  **“🎉 Party Mode” button**  that, when clicked, displays a balloon animation using  `st.balloons()`.
    
-   A  **“❄️ Snow Mode” button**  that triggers a snow animation using  `st.snow()`.
    
-----
- Create a file `app.py`

```python
import streamlit as st

st.title("🎊 Celebration App")

if st.button("🎉 Party Mode"):
    st.balloons()

if st.button("❄️ Snow Mode"):
    st.snow()
```
----
**Run the app**
- `streamlit run app.py`

----

### Expected Output

-----

### Explanation
-   **`st.button()`** → creates interactive buttons. Each click reruns the app and evaluates the condition.
    
-   **`st.balloons()`** → launches a **balloon animation** for a celebration effect.
    
-   **`st.snow()`** → launches a **snow animation**, adding a cool visual effect.
    
-   By combining these with buttons, we make the app **event-driven** — animations trigger instantly when users interact.
    
This project shows how Streamlit can go beyond data apps and be used for **playful, interactive experiences**.

---

## Topic 4.3: Basic Input Widgets 


### Introduction

User inputs are the heart of interactivity in Streamlit apps. Widgets like  `st.number_input`,  `st.text_input`, and  `st.slider`  let users feed  **numeric or text data**  into your app effortlessly. Streamlit then  **reruns the script automatically**  and uses the new input values to update outputs instantly — no complex callback code needed.

This declarative, real-time reaction model makes it easy to build apps where user input controls live computations and visualizations.

One practical and relatable example is a  **Restaurant Tip Calculator**  — where the bill amount and tip percent are inputs, and the app dynamically calculates the final amount to pay. This helps learners:

-   Understand how to collect numeric inputs with  `st.number_input`.
    
-   Perform live calculations based on input values.
    
-   Display updated results dynamically as users change inputs.
    

This project connects basic input widgets with real-world usefulness, reinforcing the power of interactive apps.

----------


### Mini  Tip Calculator

You often dine out and want a quick way to calculate the **total bill including tip**. This app helps you do just that in seconds.

- Create a file `app.py`

```python
import streamlit as st

st.title("💸 Tip Calculator")

# Input fields
bill_amount = st.number_input("Enter Bill Amount (₹)", min_value=0.0, step=50.0)
tip_percent = st.number_input("Enter Tip Percentage (%)", min_value=0.0, max_value=100.0, step=1.0)

# Calculations
tip_amount = (bill_amount * tip_percent) / 100
final_bill = bill_amount + tip_amount

# Results
st.subheader("📊 Bill Summary")
st.metric(label="Tip Amount", value=f"₹{tip_amount:.2f}")
st.metric(label="Final Bill (with Tip)", value=f"₹{final_bill:.2f}")
```
---

**Run the app**
- `streamlit run app.py`
----------

### Expected Output

        

----------

### Explanation

-   **`st.number_input()`** → lets the user input numeric values (bill and tip percentage).
    
-   **Live computation** → as inputs change, the script recalculates tip and final bill instantly.
    
-   **`st.metric()`** → displays key results in **highlighted cards** for easy visibility.
    

Learners practice numeric input handling and connect it to **real-time calculations**, making a **practical utility app** that gives immediate visual feedback.

---
## Topic 4.4: Selection Elements

### **Introduction**

You walk into your favorite café. The barista smiles and asks, “What would you like today?” Your choices matter: type of coffee, size, sweetness, maybe some whipped cream on top... It’s a small but exciting decision-making moment that shapes your perfect cup.

Just like ordering coffee,  **apps often need users to select options**—and Streamlit makes building that selection experience a breeze.

----------

#### **Why Selection Widgets Matter**

Selection widgets are the  **interactive menus, sliders, and toggles**  of your app world. They let users  **express their preferences clearly and quickly**—and your app instantly reacts with what they choose.

Here’s the secret sauce:

-   **`st.radio()`**  is like a set of sturdy buttons lined up. It works great when users must pick  **exactly one**  option from a handful. Like choosing your favorite brew.
    
-   **`st.selectbox()`**  hides all choices neatly in a dropdown—perfect for longer lists where space matters, think of picking your coffee size: Small, Medium, or Large.
    
-   **`st.slider()`**  invites users to slide a knob along a range, just like adding sugar or strength level. It’s tactile, intuitive, and fun to use.
    
-   **`st.checkbox()`**  is a simple yes/no toggle—do you want whipped cream? Check it or leave it unchecked. Easy!
    

----------

#### **How Does It Work?**

Each widget waits patiently for your input. When you make a choice, Streamlit reruns the script with your new preferences baked in. Widgets return these choices as Python variables you can use right away to update your app’s display.

No confusing callbacks, no boilerplate code—just  _declarative_  and  _immediate_  interaction.

----


### **Mini Project: Coffee Order App**

Imagine walking into your favorite café where you get to be your own barista. With just a few clicks, you can customize every detail of your coffee — from the type and size to sugar levels and toppings.

In this mini project, we’ll learn how **Streamlit selection elements** like `st.radio()`, `st.selectbox()`, `st.slider()`, and `st.checkbox()` work together to build an **interactive ordering experience**.


- Create a file `app.py`

```python
import streamlit as st
st.title("☕ Coffee Order App")

# Coffee type selection
coffee_type = st.radio(
    "Choose your coffee type:",
    ["Espresso", "Latte", "Cappuccino"]
)

# Coffee size selection
coffee_size = st.selectbox(
    "Select coffee size:",
    ["Small", "Medium", "Large"]
)

# Sugar level
sugar = st.slider(
    "Select sugar level (teaspoons):",
    min_value=0, max_value=5, step=1
)

# Extra topping
whipped_cream = st.checkbox("Add whipped cream topping")

# Display order summary
st.subheader("📝 Your Coffee Order Summary:")
order_summary = f"- {coffee_size} {coffee_type}\n- Sugar: {sugar} tsp"
if whipped_cream:
    order_summary += "\n- With whipped cream 🍦"
else:
    order_summary += "\n- No whipped cream"

st.write(order_summary)
```

----------

### **Expected Output**

    

----------

### **Explanation**

-   **`st.radio()`** → lets the user pick one option from a list (coffee type).
    
-   **`st.selectbox()`** → dropdown for selecting coffee size.
    
-   **`st.slider()`** → provides a simple way to choose a numeric value (sugar level).
    
-   **`st.checkbox()`** → toggle option for whipped cream topping.
    
-   **Dynamic summary logic** → combines all the above inputs into a single formatted summary.
    
-   **`st.success()`** → adds a polished, friendly confirmation at the end.
    

This project teaches how multiple **selection widgets** can work together to create an **interactive, real-time decision-making app**.

---


## Topic 4.5: Advanced Selection Widgets


### Introduction

Planning a movie night with friends can be a fun but sometimes tricky task. Everyone has different tastes, streaming service subscriptions, and moods. What if there was an app that made this choice easier and more interactive?

Advanced selection widgets in Streamlit empower you to build exactly that kind of app—where users select multiple options, enjoy sleek new styles, and even rate suggestions.



### Advanced Selection Widgets:  `st.multiselect()`,  `st.pills()`, and  `st.feedback()`

-   **`st.multiselect()`**  lets users select  **multiple options**  from a dropdown list. Perfect for scenarios like picking several movie genres. The result is a list of all chosen items.
    
-   **`st.pills()`**  displays options as  **pill-shaped clickable buttons**, great for choosing a single option with a modern look. Ideal for selecting one streaming service from a few choices.
    
-   **`st.feedback()`**  provides an icon-based feedback widget (like stars, thumbs up/down, or faces) that lets users rate or give sentiment about recommendations or app responses easily.
    

Together, these widgets allow your app to collect  **rich input**, present it with style, and gather  **valuable feedback**  for an engaging user experience.
    

----------

### Mini Project: Movie Night Planner


Planning a movie night can be tricky when everyone has different tastes. This mini project shows how Streamlit’s **selection widgets** can be combined to create a fun, interactive **Movie Night Planner**. Users can pick genres, choose their preferred streaming service, get a movie recommendation, and even give feedback on the suggestion.

This project demonstrates how multiple **advanced widgets** like `st.multiselect()`, `st.pills()`, and `st.feedback()` work together to build a **real-world, interactive app**.

- Create a file `app.py`

```python
import streamlit as st

st.title("🎥 Movie Night Planner")

# Select movie genres
genres = st.multiselect(
    "Select your favorite movie genres:",
    ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance"]
)

# Select streaming service
service = st.radio(
    "Choose your preferred streaming service:",
    ["Netflix", "Hulu", "Disney+", "Amazon Prime"]
)

# Simple movie recommendation mapping
recommendations = {
    "Action": "Extraction",
    "Comedy": "The Mask",
    "Drama": "The Godfather",
    "Horror": "A Quiet Place",
    "Sci-Fi": "Interstellar",
    "Romance": "La La Land"
}

# Recommend a movie based on first selected genre 
if genres:
    recommended_movie = recommendations.get(genres[0], "Movie Not Found")
    st.subheader(f"🎬 Recommended Movie: {recommended_movie} on {service}")
else:
    st.write("Select at least one genre to get a recommendation.")

# Feedback
st.subheader("⭐ Rate this recommendation")
feedback = st.radio("Your feedback:", ["Loved it ❤️", "It’s okay 🙂", "Not interested 😢"])
st.write(f"You selected: {feedback}")

```
---

**Run the app**
- `streamlit run app.py`
----------

### Expected Output


----------

###  Explanation

-   **`st.multiselect()`** → lets users pick multiple genres. Returns a list of selections.
    
-   **`st.radio()` / `st.pills()`** → choose one streaming service.
    
-   **Recommendation logic** → maps genres to a simple movie suggestion; for simplicity, it uses the first selected genre.
    
-   **`st.feedback()` / radio for feedback** → collects user opinion on the recommendation.
    
-   The app **updates dynamically** as selections change, showing immediate recommendations and feedback capture.
    

This project illustrates **interactive decision-making** using multiple Streamlit widgets, perfect for building fun, real-world apps.
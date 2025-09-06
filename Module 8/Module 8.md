# Module 8: Managing State & Performance in Streamlit

Building interactive apps is like running a busy café: you want to remember each customer’s order, keep the kitchen humming, and show everyone what’s happening. To achieve this, Streamlit offers powerful tools for tracking state and boosting speed:

-   **Session State:**  Remembers past actions, like a basket keeping track of everything a customer adds.
    
-   **Forms:**  Collects and submits groups of inputs like filling out an order slip—all at once, not piecemeal.
    
-   **Callbacks:**  Triggers specific events on demand, just like ringing a bell for the chef when an order is ready.
    
-   **Caching:**  Stores results to save time, much like prepping ingredients ahead of rush hour.
    
-   **Progress Bars:**  Visually indicate that something’s happening, keeping customers confident and patient.

---
### Topic 8.1: Session State

**Session state**  is the way your app remembers what users have done, even after many interactions—like keeping a customer’s basket handy at the checkout.  
Let’s understand session state by building a  **Shopping Cart App**.

### Mini Project : Shopping Cart App

By default, Streamlit resets variables on every user interaction. To **remember values**, you use **session state** (`st.session_state`).

Think of it as a **shopping basket** that remembers what you’ve added.

**Code**

```
import streamlit as st

st.title("🛒 Shopping Cart App")

# Initialize cart in session state
if "cart" not in st.session_state:
    st.session_state.cart = []

# Add items
item = st.text_input("Enter an item to add to cart")
if st.button("Add to Cart"):
    if item:
        st.session_state.cart.append(item)
        st.success(f"{item} added to cart!")

# Show cart
st.subheader("Your Cart")
for i, product in enumerate(st.session_state.cart, start=1):
    st.write(f"{i}. {product}")

```

**Expected Output**

-   A text box to enter an item.
    
-   Clicking “Add to Cart” keeps items in the list, even after new inputs.  
    (Screenshot placeholder: cart with multiple added items.)
    
**Key Takeaways**

-   `st.session_state` remembers data between user interactions.
    
-   Perfect for carts, counters, quiz scores, or any “memory.”
----------

### Topic 8.2: Forms

**Forms**  allow grouping user inputs so they’re submitted all at once—think of a restaurant order slip that’s filled out and sent when ready.  
Let’s understand forms by building a  **Feedback Collector**.

### Mini Project : Feedback Collector

Forms group inputs together and only submit when the user clicks the **Submit button**.

Think of it as filling out an **order slip** — you don’t send it until you’re ready.

**Code**

```
import streamlit as st

st.title("📝 Feedback Collector") 
with st.form("feedback_form"):
    name = st.text_input("Your Name")
    rating = st.slider("Rate your experience", 1, 5, 3)
    comments = st.text_area("Additional Comments")
    submitted = st.form_submit_button("Submit") 
    if submitted:
	    st.success(f"Thanks {name}! You rated us {rating}/5.") 
	    if comments:
            st.write("Your comments:", comments)
 ```

**Expected Output**

-   A form with text input, slider, and text area.
    
-   Submits only when “Submit” is clicked.  
    (Screenshot placeholder: feedback form before and after submission.)
    
**Key Takeaways**

-   Forms collect multiple inputs together.
    
-   They prevent actions from running on every keystroke.
----------

### Topic 8.3: Callbacks

**Callbacks**  attach targeted actions or events to widgets—like ringing a kitchen bell to signal a specific job needs to be done.  
Let’s understand callbacks by building a  **Counter Button App**.

### Mini Project : Counter Button App

Normally, Streamlit reruns the whole script when you click something.

**Callbacks** let you attach a **function to a widget** so it runs when the widget changes.

Think of it like a **kitchen bell** — press it, and something specific happens.

**Code**

```
import streamlit as st

st.title("🔢 Counter Button App")
st.markdown('---')

if "count" not in st.session_state:
    st.session_state.count = 0

def increment():
    st.session_state.count += 1


st.button("Increase", on_click=increment)

st.markdown(f"<h1 style='text-align: center; font-size: 72px;'>{st.session_state.count}</h1>", unsafe_allow_html=True)

```

**Expected Output**

-   A button labeled “Increase.”
    
-   Each click increases the counter by 1.  
    (Screenshot placeholder: counter going from 0 → 1 → 2.)
    
**Key Takeaways**

-   Callbacks (`on_click`, `on_change`) let you trigger **custom actions**.
    
-   Great for counters, toggles, or data processing buttons.
----------

### Topic 8.4: Caching

**Caching**  makes your app faster by saving the results of expensive or slow tasks, relying on prepared data instead of repeating work—like reheating a pre-cooked meal.  
Let’s understand caching by building a  **Stock Price Fetcher**.

### Mini Project : Stock Price Fetcher
Fetching data repeatedly can be slow. **Caching** stores results so the app reuses them instead of calling again.

Think of it like **meal prep** — once you’ve cooked a dish, reheating it is faster than cooking again.

**Code**
```
import streamlit as st
import time
import random

st.title("📈 Stock Price Fetcher")

@st.cache_data
def get_stock_price(symbol):
    time.sleep(2)  # simulate slow API call
    return round(random.uniform(100, 200), 2)

symbol = st.text_input("Enter stock symbol", "AAPL")
if st.button("Get Price"):
    price = get_stock_price(symbol)
    st.metric(label=f"{symbol} Price", value=f"${price}")

```

**Expected Output**

-   Input for stock symbol.
    
-   Clicking “Get Price” shows a metric.
    
-   First call takes ~2 seconds, repeated calls return instantly.  
    (Screenshot placeholder: AAPL price with metric card.)
    
**Key Takeaways**

-   Use `@st.cache_data` to cache expensive computations.
    
-   Speeds up APIs, data loads, and heavy calculations.
----------

### Topic 8.5: Progress & Status

**Progress bars and status messages**  help users stay patient and informed during lengthy tasks, just as "Order in Progress" signs do in a busy café.  
Let’s understand progress and status indicators by building a  **File Upload Monitor**.

### Mini Project : File Upload Monitor

Long tasks feel slow without feedback. A **progress bar** shows that something is happening.

Think of it as a **loading bar on a file upload** — it keeps users patient.

**Code**

```
import streamlit as st
import time

st.title("📂 File Upload Monitor")

uploaded_file = st.file_uploader("Upload a file")

if uploaded_file:
    st.info("Processing your file...")
    progress_bar = st.progress(0)  # start at 0%

    for percent in range(100):
        time.sleep(0.01)  # simulate processing
        progress_bar.progress(percent + 1)  # update bar

    st.success("File processed successfully!")

``` 

**Expected Output**

-   File uploader widget.
    
-   Progress bar fills up after file upload.
    
-   Ends with a success message.  
    (Screenshot placeholder: progress bar during upload.)
    

**Key Takeaways**

-   Progress bars (`st.progress`) keep users informed.
    
-   Combine with status messages (`st.info`, `st.success`, etc.) for better UX.
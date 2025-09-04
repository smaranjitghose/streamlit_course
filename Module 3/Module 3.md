
# Module 3: Input Forms & Media Uploads in Streamlit

## Introduction
_Input widgets turn a passive app into an interactive experience—like moving from a static museum display to a hands-on science lab_.

Just as a hotel lobby needs forms for check-in and a scanner for passports, Streamlit apps come alive with controls for entering data, choosing between options, and uploading media.  
**Input widgets are the hands and voice of your app, letting users take part in the action.**

----------

### Topic 3.1 Buttons & Checkboxes

**Introduction**

Buttons and checkboxes are the  **simplest tools for getting user feedback**—think of them like everyday gadgets.

-   **Buttons**  act as instant triggers, just like a  **doorbell**  or “Submit” on a website. They’re perfect for “one-off” actions—submitting a form, starting a process, confirming a choice.
    
-   **Checkboxes**  work as simple toggles, like a  **light switch**  or a checklist item. They let users indicate YES/NO, DONE/PENDING, or turn a setting ON/OFF.
    

These controls make everyday app tasks intuitive and visual, replacing clunky text commands or ambiguous input fields.

**Tip:**  Use checkboxes for tracking lists, preferences, or toggling features. Use buttons for actions that only happen when the user is ready.


### Mini Project: Task Toggle App


Buttons and checkboxes are fundamental for binary choices and triggering actions.
Let's build a simple to-do list where tasks can be toggled on or off using checkboxes.

**Code:**

```python
import streamlit as st

st.title("Task Toggle App")

task1 = st.checkbox("Buy groceries")
task2 = st.checkbox("Walk the dog")
task3 = st.checkbox("Pay bills")

if task1:
    st.write("Groceries purchased!")
if task2:
    st.write("Dog walked!")
if task3:
    st.write("Bills paid!")

```

**Explanation:**

-   `st.checkbox()` creates a checkbox widget. The label inside the parentheses is what the user sees.
    
-   The checkbox returns `True` if checked and `False` otherwise.
    
-   We use `if` statements to check the state of each checkbox and display a message accordingly.
    

**Output:**

The app displays three checkboxes labeled "Buy groceries," "Walk the dog," and "Pay bills." When a checkbox is checked, a message appears below it confirming the task completion.

**Key Takeaways:**

-   Checkboxes are ideal for on/off switches and binary selections.
    
-   The state of a checkbox can be easily accessed and used to control other parts of your app.
----------

### Topic 3.2 Radio & Select Menus

**Introduction**

Choice menus turn your app into a clean, guided experience—like a  **restaurant menu**  with clear options, instead of typing out your order.

-   **Radio buttons**  (`st.radio()`) are great for choices where only one answer is valid, presented upfront—ideal for “one among a few” selections (pizza size, survey answers).
    
-   **Select boxes**  (`st.selectbox()`) compress multiple options into a dropdown—best for long lists or when screen space is tight.
    

These inputs remove guesswork, speed up decision-making, and prevent accidental “multi-choice” errors.

**Tip:**  Use radio buttons when choices are few and clarity is important. Use select boxes for lists that could get long or clutter the page.

### Mini Project: Coffee Order App

Radio buttons and select menus allow users to choose one option from a list.
Let's create an app where users can select their coffee type and size, then display an order summary.

**Code:**

```python
import streamlit as st

st.title("Coffee Order App")

coffee_type = st.radio("Choose your coffee:", ("Latte", "Cappuccino", "Espresso"))
coffee_size = st.selectbox("Select size:", ("Small", "Medium", "Large"))

st.write("---")
st.write(f"You ordered a {coffee_size.lower()} {coffee_type.lower()}.")

```

**Explanation:**

-   `st.radio()` creates a set of radio buttons. The first argument is the label, and the second is a tuple of options.
    
-   `st.selectbox()` creates a dropdown menu. Similar to `st.radio()`, it takes a label and a list of options.
    
-   The selected value is stored in the corresponding variable (`coffee_type`, `coffee_size`).
    
-   We use an f-string to display the order summary.
    

**Output:**

The app displays radio buttons for coffee types (Latte, Cappuccino, Espresso) and a dropdown menu for sizes (Small, Medium, Large). After selecting options, an order summary is displayed, e.g., "You ordered a small latte."

**Key Takeaways:**

-   Radio buttons are best for mutually exclusive choices when all options should be visible.
    
-   Select menus are useful when you have many options and want to save screen space.
----------

### Topic 3.3 Text & Number Inputs

**Introduction**

Some data can’t be predefined—users need to  **type**  things themselves. Just like a hotel check-in form asks for your name and age, Streamlit offers :

-   **Text inputs**  for free-form text: names, email, custom responses.
    
-   **Number inputs**  for precise numeric entries: quantities, amounts, ratings.
    

These fields are the  **keyboards of your app**, letting users feed in unique data. They’re vital for calculators, search bars, and custom feedback forms.

**Tip:**  Always label input boxes clearly so users know what’s expected. Add validations (like minimums or numeric limits) to prevent confusion.

### Mini Project: Tip Calculator

Text and number inputs allow users to enter custom values.
Let's build a tip calculator where users enter the bill amount and tip percentage to calculate the total.

**Code:**

```python
import streamlit as st

st.title("Tip Calculator")

bill_amount = st.number_input("Enter bill amount:", min_value=0.0)
tip_percentage = st.number_input("Enter tip percentage:", min_value=0, max_value=100, value=15)

tip_amount = bill_amount * (tip_percentage / 100)
total_amount = bill_amount + tip_amount

st.write("---")
st.write(f"Tip amount: ${tip_amount:.2f}")
st.write(f"Total amount: ${total_amount:.2f}")

```

**Explanation:**

-   `st.number_input()` creates a number input field. We specify `min_value`, `max_value`, and `value` (default value) to constrain the input.
    
-   We calculate the tip amount and total amount based on the user's input.
    
-   We use f-strings with formatting (`:.2f`) to display the amounts with two decimal places.
    

**Output:**

The app displays number input fields for the bill amount and tip percentage. After entering values, the calculated tip amount and total amount are displayed.

**Key Takeaways:**

-   Number inputs are ideal for numerical data entry.
    
-   You can use `min_value`, `max_value`, and `value` to control the input range and default value.
----------

### Topic 3.4 Date & Time Pickers

**Introduction**

Time is tricky to enter by hand. Typing “02/09/2025” can lead to mistakes (format, typos).  **Date pickers**  are like built-in calendars, and  **time pickers**  are like setting the alarm clock on your phone.

-   Users select from easy widgets—no formatting worries, quick selection.
    
-   Great for appointments, deadlines, reminders, and event planning.
    

These widgets cut down on user errors and streamline scheduling tasks—they also just feel modern and professional.

**Tip:**  Use date and time pickers for bookings, reminders, and anything tied to a calendar or clock. Always show users the format they’ve picked.

### Mini Project: Birthday Countdown App

Date and time pickers allow users to select specific dates and times.
Let's Create an app where users select a birthday, and the app displays how many days are left until that birthday.

**Code:**

```python
import streamlit as st
import datetime

st.title("Birthday Countdown")

birthday = st.date_input("Select your birthday:", datetime.date.today())

today = datetime.date.today()
days_left = (birthday - today).days

st.write("---")
st.write(f"Days left until your birthday: {days_left}")

```

**Explanation:**

-   `st.date_input()` creates a date picker. The default value is set to today's date.
    
-   We calculate the difference between the selected birthday and today's date using `datetime`.
    
-   We extract the number of days from the difference using `.days`.
    

**Output:**

The app displays a date picker for selecting a birthday. After selecting a date, the number of days left until that birthday is displayed.

**Key Takeaways:**

-   Date pickers are useful for selecting specific dates.
    
-   The `datetime` module provides powerful tools for working with dates and times.
----------

### Topic 3.5 Sliders

**Introduction**

Sliders turn numbers into smooth, visual controls. Like the  **volume knob on a music player**, sliders help users quickly adjust values—whether it’s a price, a rating, or a range for simulation results.

-   **Single-value sliders**  are great for one setting (temperature, loan amount).
    
-   **Range sliders**  let users pick “between X and Y” (age range, price window).
    
-   Also useful for dates, especially for selecting durations or periods.
    

Sliders make applications feel responsive, creative, and fun—especially for demo tools and “what-if” calculators.

**Tip:**  Use sliders for values that users want to adjust frequently. Always show the exact value picked, so users aren’t guessing.

### Mini Project: Loan EMI Estimator App

Sliders allow users to select a value within a continuous range.
Let's build a loan EMI estimator where users input the loan amount, interest rate, and tenure using sliders, then the app estimates the EMI.

**Code:**

```python
import streamlit as st

st.title("Loan EMI Estimator")

loan_amount = st.slider("Loan Amount:", min_value=1000, max_value=100000, value=50000)
interest_rate = st.slider("Interest Rate (%):", min_value=1, max_value=20, value=8)
loan_tenure = st.slider("Loan Tenure (years):", min_value=1, max_value=30, value=5)

monthly_interest_rate = interest_rate / (12 * 100)
emi = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate)**(loan_tenure * 12)) / ((1 + monthly_interest_rate)**(loan_tenure * 12) - 1)

st.write("---")
st.write(f"Estimated EMI: ${emi:.2f}")

```

**Explanation:**

-   `st.slider()` creates a slider widget. We specify `min_value`, `max_value`, and `value` to define the slider's range and default value.
    
-   We calculate the EMI using the standard formula.
    
-   We display the estimated EMI with two decimal places.
    

**Output:**

The app displays sliders for loan amount, interest rate, and loan tenure. As the user adjusts the sliders, the estimated EMI is updated in real-time.

**Key Takeaways:**

-   Sliders are ideal for selecting values within a continuous range.
    
-   They provide a visual and intuitive way for users to explore different scenarios.
----------

### Topic 3.6 File Uploads

**Introduction**

Giving users the ability to  **upload files**  makes your app a digital workspace—like dropping documents at an office front desk.

-   **File uploaders**  (`st.file_uploader()`) accept resumes, CSVs, PDFs, images, or any document users need to share or process.
    
-   Essential for forms, data analysis, resume screening, report uploads, and more.
    

They make data processing secure and user-friendly—users don’t have to email files or copy-paste large amounts of data.

**Tip:**  Always specify supported file types. Show a preview when possible (even partial content), so users see instant feedback.

### Mini Project: Resume Reviewer

File uploads allow users to upload files to your Streamlit app.
Let's create an app where users upload a resume, and the app previews its first few lines.

**Code:**

```python
import streamlit as st

st.title("Resume Reviewer")

uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])

if uploaded_file is not None:
    file_contents = uploaded_file.read().decode("utf-8")
    first_few_lines = "\n".join(file_contents.splitlines()[:5])
    st.write("---")
    st.write("First few lines of your resume:")
```
----------

### Topic 3.7 Media Uploads

**Introduction**

Modern apps are multimedia hubs. Users may wish to share  **photos, audio, or video**—whether for fun (like a selfie booth), proof (ID checks), or creativity (profile pics, artwork).

-   **Camera inputs**  (`st.camera_input`) let users snap pictures directly.
    
-   **Image, video, and audio uploaders**  allow sharing recordings or files.
    

This turns your app into a mini studio or kiosk, bridging online interaction and the real world.

**Tip:**  Use media elements for apps that need to  **capture identity, creativity, or evidence.**  Always confirm successful uploads and show results in the app.

----------

### Topic 3.8 Chat Elements

**Introduction**

Chat interfaces make apps  **feel alive and responsive**—users type a question, get instant feedback, and the app feels like a conversation with a helpful friend or assistant.

-   **Chat bubbles**  show dialogue, making interfaces less formal and more engaging.
    
-   **Input boxes**  let users enter freeform text, just like a messaging app.
    

Great for FAQs, customer support, or interactive Q&A bots—these elements build trust and foster ongoing engagement, not just single-use transactions.

**Tip:**  Structure chatbot answers clearly. Repeat the user’s question for clarity before replying. Always respond even if the answer is unknown—to keep the conversation flowing.

----------

## Conclusion

-   **Input elements are the voice and hands of your app**—they gather, confirm, and process what users want.
    
-   Each widget has a real-world analogy—think physical gadgets, forms, and kiosks.
    
-   Good input controls make apps intuitive, trustworthy, and a joy to use.
    

Streamlit’s widgets let any app move beyond passive reading and into true two-way interaction—**where users create, choose, and connect, not just watch.**
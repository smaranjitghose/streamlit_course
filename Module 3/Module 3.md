
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

st.set_page_config(page_title="Basic Task App")

st.title("Basic Task Toggle App")

# Input for new task
tasks =  ["Learn Streamlit", "Build an app", "Deploy to Cloud"] 
completed = []

new_task = st.text_input("Enter a new task")
if st.button("Add Task ➕"):
    tasks.append(new_task)

st.markdown("------")

# Show tasks
st.subheader("Your Tasks 📝")
for t in tasks:
    if st.checkbox(t, key=t):
        completed.append(t)

st.markdown("------")

st.subheader("Completed Tasks 📌")
for c in completed:
    st.write(f"✅ {c}")


```

**Explanation:**

-   `st.checkbox()` creates a checkbox widget. The label inside the parentheses is what the user sees.
    
-   The checkbox returns `True` if checked and `False` otherwise.
    
-   We use `if` statements to check the state of each checkbox and display a message accordingly.
    

**Expected Output:**

The app displays three checkboxes labeled "Buy groceries," "Walk the dog," and "Pay bills." When a checkbox is checked, a message appears below it confirming the task completion.

<img src ="https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%203/task_toggle.png">

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
import streamlit as st;

st.set_page_config(page_title='Coffee Order App')

st.title('Coffee Order App ☕')

coffee_type = st.radio('Choose your favourite Coffee',('Latte', 'Cappuccino', 'Espresso'))

coffee_size = st.radio('Select Size',('Small', 'Medium', 'Large'))

prices=['$10','$15', '$20']
if st.button("Order Coffee"):
    if coffee_size=='Small':
        coffee_price='$10'
    elif coffee_size=='Medium':
        coffee_price='$15'
    else:
        coffee_price='$20'

    st.write("------")
    st.write(f'You ordered {coffee_type} in size {coffee_size.lower()}')
    st.info(f'Your bill is {coffee_price}')

```

**Explanation:**

-   `st.radio()` creates a set of radio buttons. The first argument is the label, and the second is a tuple of options.
    
-   `st.selectbox()` creates a dropdown menu. Similar to `st.radio()`, it takes a label and a list of options.
    
-   The selected value is stored in the corresponding variable (`coffee_type`, `coffee_size`).
    
-   We use an f-string to display the order summary.
    

**Expected Output:**

The app displays radio buttons for coffee types (Latte, Cappuccino, Espresso) and a dropdown menu for sizes (Small, Medium, Large). After selecting options, an order summary is displayed, e.g., "You ordered a small latte."

**Key Takeaways:**

-   Radio buttons are best for mutually exclusive choices when all options should be visible.
    
-   Select menus are useful when you have many options and want to save screen space.

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%203/coffee.png">

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
import streamlit as st;

st.set_page_config(page_title='Tip Calculator App')

st.title('Tip Calculator')

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
    

**Expected Output:**

The app displays number input fields for the bill amount and tip percentage. After entering values, the calculated tip amount and total amount are displayed.

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%203/tip_calculator.png">

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

st.set_page_config(page_title='Birthday Countdown')

st.title('Birthday Countdown 🎊')

birth_date=st.date_input("Select your Birthday", value=datetime.date(2002,5,2), min_value=datetime.date(1990,1,1), max_value=datetime.date.today())

today = datetime.date.today() 

next_birthday = birth_date.replace(year=today.year)

if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

days_left=(next_birthday - today).days

st.write('-----')
st.write(f'🎂Days left until your birthday {days_left} days ')

```

**Explanation:**

-   `st.date_input()` creates a date picker. The default value is set to today's date.
    
-   We calculate the difference between the selected birthday and today's date using `datetime`.
    
-   We extract the number of days from the difference using `.days`.
    

**Expected Output:**

The app displays a date picker for selecting a birthday. After selecting a date, the number of days left until that birthday is displayed.

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%203/birthday.png">

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
st.info(f"Estimated EMI: ${emi:.2f}")

```

**Explanation:**

-   `st.slider()` creates a slider widget. We specify `min_value`, `max_value`, and `value` to define the slider's range and default value.
    
-   We calculate the EMI using the standard formula.
    
-   We display the estimated EMI with two decimal places.
    

**Expected Output:**

The app displays sliders for loan amount, interest rate, and loan tenure. As the user adjusts the sliders, the estimated EMI is updated in real-time.

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%203/loan_emi.png">

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

File uploads in Streamlit let users provide documents, images, or data directly to your app.

Think of it like a **job portal** — candidates upload their resumes, and the app can preview or analyze them. This is super useful for:

-   Checking the format of resumes.
    
-   Extracting key details.
    
-   Quickly previewing uploaded content.
    
**Code**

```
import streamlit as st
import PyPDF2

st.title("📄 Resume Reviewer")

uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])

if uploaded_file is not None:
    st.write("---")
    st.subheader("First few lines of your resume:")

    if uploaded_file.type == "text/plain":
        # Handle TXT files
        file_contents = uploaded_file.read().decode("utf-8")
        first_few_lines = "\n".join(file_contents.splitlines()[:5])
        st.text(first_few_lines)

    elif uploaded_file.type == "application/pdf":
        # Handle PDF files
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages[:1]:  # Read first page only
            text += page.extract_text() or ""
        first_few_lines = "\n".join(text.splitlines()[:5])
        st.text(first_few_lines)

```

----------

**Expected Output**

-   A **file upload box** that accepts TXT or PDF resumes.
    
-   When a file is uploaded:
    
    -   If TXT → The first 5 lines are shown.
        
    -   If PDF → The first few lines of the first page are extracted and displayed.  

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%203/resume_viewer.png">
        

**Key Takeaways**

-   `st.file_uploader()` accepts files directly from users.
    
-   Always check file type before processing (PDF vs TXT vs others).
    
-   Libraries like **PyPDF2** help extract text from PDF files.
----------


### Topic 3.7 Media Uploads

**Introduction**

Modern digital experiences go beyond text and numbers—**media uploads transform apps into interactive studios and creative workspaces**. Whether users want to share a selfie, provide identity proof, or upload audio for a podcast, these widgets empower personal and professional expression.

-   **Camera inputs**  (`st.camera_input`) work like a photo booth in your device, allowing direct image capture—from profile photos to on-the-spot document verification.
    
-   **Image, video, and audio uploaders**  collect a variety of media files, turning your app into a versatile entry point for creativity, evidence submission, or social sharing.
    

By supporting media, your app bridges the virtual and physical worlds, becoming a portal for identity, memory, and creativity.

**Tip:**  
Always provide clear guidance about what types of media are supported, and confirm successful uploads with visual feedback. Previewing the user’s submitted media helps build trust and excitement, making the app feel personal and responsive.

### Mini Project: Background Remover

Sometimes, you don’t just want to capture a photo — you want to transform it. That’s where background removal comes in.

Think of it like cutting a person out of a magazine picture: you keep the subject but remove the clutter behind them. Streamlit makes this super easy when combined with tools like rembg.

**Why is this useful?**

ID card photos need plain backgrounds.

E-commerce product listings often require clean, transparent images.

Fun apps can let users swap backgrounds (like Zoom virtual backgrounds).

With just a few lines of code, you can upload or capture an image, process it, and instantly get a clean cut-out with no background.

**Code**

```python

import streamlit as st
from rembg import remove
from PIL import Image
import io

st.title("🖼️ Background Remover")

st.write("Upload an image or take a selfie, and remove its background instantly.")

# Choose input method
option = st.radio("Choose an option:", ["Upload an image", "Take a selfie"])

if option == "Upload an image":
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        input_image = Image.open(uploaded_file)
elif option == "Take a selfie":
    picture = st.camera_input("Take a picture")
    if picture:
        input_image = Image.open(picture)
else:
    input_image = None

if "input_image" in locals():
    st.subheader("Original Image")
    st.image(input_image, use_column_width=True)

    with st.spinner("Removing background..."):
        output_image = remove(input_image)

    st.subheader("Image without Background")
    st.image(output_image, use_column_width=True)

    # Allow download
    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    st.download_button(
        label="Download without Background",
        data=buf.getvalue(),
        file_name="no_bg.png",
        mime="image/png"
    )
```

**Expected Output**

A radio button lets users choose between uploading an image or taking a selfie.
<img src =" https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%203/bgremove1.png">

Once the photo is provided, the original image is displayed.
<img src =" https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%203/bgremove2.png">

The app processes the picture and shows a new version with the background removed.

A download button appears so users can save the clean image.

<img src ="https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%203/bgremove3.png">

**Key Takeaways**

Streamlit can handle both uploads and live camera input.

Background removal makes apps practical (ID photos, product images) and fun (creative edits, virtual backdrops).

Combining Streamlit with external libraries like rembg unlocks AI-powered image processing inside your web apps.
    

----------

### Topic 3.8 Chat Elements

**Introduction**

Today’s users expect apps to “listen” and “talk back”—**chat widgets turn a static app into a living, conversational experience**. Chatting feels natural and engaging, whether for support, learning, or playful Q&A.

-   **Chat bubbles**  dynamically display the dialogue, replacing stiff forms with warm, friendly feedback—just like a real conversation.
    
-   **Input boxes**  invite users to type freely, supporting questions, messages, or commands in context.
    

Well-designed chat interfaces foster  **trust and repeat engagement**, moving beyond simple transactions to build relationships with users. They're indispensable for automated help desks, FAQs, and interactive guides.

**Tip:**  
Organize chat exchanges for clarity—echo the user’s query before responding, keep answers concise yet helpful, and always offer a response (even if it’s "I don't know yet") to maintain momentum and keep users engaged.


### Mini Project: Simple FAQ Bot

Chat interfaces are like a **virtual help desk**. Instead of navigating menus, users can **ask questions in plain language** and get answers.

In Streamlit, chat features include:

-   `st.chat_message()` → shows chat bubbles (like messages in WhatsApp).
    
-   `st.chat_input()` → lets the user type and send messages.
    

This makes your app feel **alive and conversational**. Great for FAQs, small bots, and even interactive storytelling.

**Code**

```
import streamlit as st

st.title("Simple FAQ Bot 💬")

faq = {
    "what is streamlit": "Streamlit is an open-source Python library for building web apps.",
    "how do i install streamlit": "Run `pip install streamlit` in your terminal.",
    "how do i run a streamlit app": "Use `streamlit run your_app.py`.",
    "who created streamlit": "Streamlit was created by Adrien Treuille, Thiago Teixeira, and Amanda Kelly."
}

# Initial assistant message
st.chat_message("assistant").write("Hi! I'm your FAQ bot. Ask me something about Streamlit.")

# Get user input
user_input = st.chat_input("Ask a question...")

if user_input:
    # Display user message
    st.chat_message("user").write(user_input)

    # Normalize input (lowercase, strip spaces)
    normalized = user_input.lower().strip()

    # Try to find a match (exact or partial)
    answer = None
    for question, response in faq.items():
        if question in normalized:  # partial match
            answer = response
            break

    if not answer:
        answer = "Sorry, I don’t know that one yet. Try another question!"

    # Display assistant answer
    st.chat_message("assistant").write(answer)

``` 

**Expected Output**

-   Chat opens with a friendly **bot greeting**.
    
-   User types a question (e.g., “What is Streamlit?”).
    
-   The bot replies with the correct FAQ answer.
    
-   If the bot doesn’t know, it politely says so.  

<img src = "https://github.com/smaranjitghose/streamlit_course/blob/master/image/Module%201/Module%203/faqbot.png">



**Key Takeaways**

-   Chat features make apps **conversational and engaging**.
    
-   Store chat history with `st.session_state` so it feels like a real conversation.
    
-   Great for FAQs, help desks, or interactive storytelling apps.
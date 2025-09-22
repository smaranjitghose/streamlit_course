# Module 8: Multi-Page Applications & Navigation

### Topic 8.1: Page Basics


<br>

#### **Introduction**

You know how confusing it gets when you cram everything onto one page? Your friend shows you their cool app, but it's this endless scroll of different features all mashed together—a calculator, then some charts, then a form, then more stuff. By the time you scroll down, you've forgotten what was at the top. Real apps don't work like this because users expect organized, navigable experiences where each section has a clear purpose.

Streamlit's pages system solves this organization challenge by allowing developers to split applications into focused, logical sections that users can navigate naturally. Just like Instagram separates feeds from profiles or Netflix divides browsing from account settings, Streamlit's multi-page functionality enables clean information architecture where each page serves a specific purpose, creating intuitive user experiences that scale effectively as applications grow in complexity.

#### **Mini Project**

Students at TechU University are frustrated because they need different types of information at different times but everything is crammed onto one overwhelming page. When they visit the website, they can't quickly distinguish between general university information, academic program details, and ways to get help or contact staff, making simple tasks unnecessarily time-consuming and confusing.
A multi-page university website would solve this by organizing content into dedicated sections, letting students navigate directly to the specific information they need without wading through irrelevant content.

##### **Project Setup**

Create a new file `app.py`:

```python
import streamlit as st

st.title("🎓 TechU University")

st.image("https://via.placeholder.com/600x200/blue/white?text=Campus+Photo")

st.write("Welcome to TechU University - where technology meets education!")

st.write("**Quick Facts:**")
st.write("• Students: 15,000+")
st.write("• Programs: 25+")
st.write("• Founded: 1995")

st.success("Applications now open for Fall semester!")

```

Next, create a folder called `pages` in the same directory as `app.py`.

Inside the `pages` folder, create `1_📚_Courses.py`:

```python
import streamlit as st

st.title("📚 Our Courses")

st.subheader("Undergraduate Programs")

courses = ["Computer Science", "Software Engineering", "Data Science", "Cybersecurity"]

for course in courses:
    st.write(f"🎯 **{course}** - 4 years, 120 credits")

st.subheader("Graduate Programs")
st.write("🎓 Master of Computer Science - 2 years")
st.write("🎓 PhD in AI - 4 years")

st.info("Need more info? Contact our admissions office!")

```

Finally, create `2_📞_Contact.py` in the `pages` folder:

```python
import streamlit as st

st.title("📞 Contact Us")

# Contact form
name = st.text_input("Your Name")
email = st.text_input("Email")
message = st.text_area("Message")

if st.button("Send Message"):
    if name and email and message:
        st.success("Message sent! We'll reply within 24 hours.")
    else:
        st.error("Please fill in all fields.")

st.write("---")
st.write("**Campus Address:** 123 University Drive, Tech City")
st.write("**Phone:** (555) 123-TECHU")
st.write("**Email:** info@techu.edu")

```

**Run your app with:**

```
streamlit run app.py

```

##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%208/mod8uni1.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%208/mod8uni2.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%208/mod8uni3.png">


----

#### **Step-by-Step Walkthrough**

- **The pages folder** is where Streamlit looks for additional pages. Any Python file you put in this folder automatically becomes a new page in your app. The folder must be named exactly `pages` and be in the same directory as your main app file.

- **File naming in pages** determines both the URL and display name. The format `1_📚_Courses.py` creates a page called "Courses" with a book emoji. The number `1_` controls the order of the file in the navigation menu.

- **Each page is independent** - they're separate Python files that run independently. You can import different libraries, use different layouts, or create completely different user experiences on each page.

- **Navigation happens automatically** - Streamlit creates a sidebar navigation menu based on your pages folder contents. Users can click between pages, and each page loads its own content without you writing any navigation code.

----

#### **Conclusion**

Multi-page architectures elevate applications from single-purpose tools to comprehensive platforms that can handle complex workflows across web and desktop environments. By organizing content into focused sections with automated navigation, these patterns create intuitive user experiences that scale naturally as functionality expands. This approach to application structure represents a fundamental strategy for building professional-grade systems that can grow from simple tools into full-featured platforms without sacrificing usability.

----

### Topic 8.2: Page Links

<br>

#### **Introduction**

Ever noticed how some apps feel more like websites? Instead of just having that sidebar menu, they have buttons right in the content that say things like "Go to Settings" or "View Your Orders." These buttons feel more natural than hunting through menus - they guide you exactly where you need to go next.

In Streamlit, **Page links** let you create these smooth navigation experiences. Instead of users figuring out where to click in a sidebar, you can put helpful "Next Step" buttons right where they make sense in your content flow.

#### **Mini Project**

Sarah needs to check her payslip before a meeting with her financial advisor, but navigating her company's employee portal is a frustrating maze of nested menus and confusing categories. She wastes precious time clicking through "Employee Services," then "Compensation," then "Pay History" just to find a simple document, and when she needs to request time off next week, she has to start the whole navigation process over again to find the leave section.
An efficient employee portal would give workers like Sarah direct access to their most-needed functions - payslips, leave requests, and profile updates - all from one central dashboard without the menu hunting.

##### **Project Setup**

Create a new file `app.py`:

```python
import streamlit as st

st.title("🏢 Employee Portal")
st.write("Welcome! What would you like to do?")

st.page_link("pages/payslips.py", label="💰 View Payslips")
st.page_link("pages/leave.py", label="🌴 Request Leave")
st.page_link("pages/profile.py", label="👤 Edit Profile")

```

Create a `pages` folder and add `payslips.py`:

```python
import streamlit as st

st.title("💰 Payslips")

st.write("**October 2024:** $3,800 (net)")
st.write("**September 2024:** $3,800 (net)")
st.write("**August 2024:** $3,800 (net)")

st.page_link("app.py", label="← Back to Portal")

```

Add `leave.py` to the `pages` folder:

```python
import streamlit as st

st.title("🌴 Leave Request")

st.write("**Your Balance:** 15 days available")

start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

if st.button("Submit Request"):
    st.success("Request submitted!")

st.page_link("app.py", label="← Back to Portal")

```

Add `profile.py` to the `pages` folder:

```python
import streamlit as st

st.title("👤 Profile")

name = st.text_input("Name", value="John Smith")
email = st.text_input("Email", value="john@company.com")

if st.button("Update Profile"):
    st.success("Profile updated!")

st.page_link("app.py", label="← Back to Portal")

```

**Run your app with:**

```
streamlit run app.py

```

##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%208/emp1mod8.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%208/emp2mod8.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%208/emp3mod8.png">



<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%208/emp4mod8.png">


----

#### **Step-by-Step Walkthrough**

- **st.page_link()** creates a button that navigates to another page in your app. The first parameter is the path to the page file, and you can add a custom label and icon to make it clear where the button leads.

- **The label parameter** lets you customize what text appears on the button. Instead of showing the filename, you can write something user-friendly like "View Payslips" or "Edit Profile."

- **The icon parameter** adds a visual element that makes buttons more recognizable. Users can quickly spot the payslip button by the money emoji or the profile button by the person icon.

- **Bidirectional navigation** works by putting page links on both the main page and the sub-pages. The main page links forward to specific sections, while each section links back to the main dashboard, creating a smooth user flow.


#### **Conclusion**

Strategic placement of navigation elements within content creates intuitive user journeys that guide users through complex workflows without relying on traditional menu systems. This contextual navigation approach transforms fragmented interfaces into cohesive experiences where each interaction feels purposeful and logically connected to the user's current task. Mastering these flow-based navigation patterns enables developers to build applications that feel less like software tools and more like natural, guided experiences.

-----

### Topic 8.3: Switch Pages


<br>

#### **Introduction**

You know how some apps automatically take you to the next screen after you do something? Like when you log into your bank app and it immediately shows your account dashboard, or when you complete a purchase and suddenly you're on the "Thank You" page? That's not you clicking a link - the app is moving you along automatically.

Streamlit switch pages help us create these smart, automatic redirects. Instead of users having to figure out where to go next after completing an action, we can programmatically send them to the right place at the right time, making our apps feel more professional and user-friendly.

#### **Mini Project**

Maria wants to quickly check her favorite online store for a specific item during her lunch break, but she's forced to navigate through multiple pages after logging in - first a generic welcome page, then clicking through menus to finally reach the products. By the time she gets to the actual shopping section, her break is nearly over and she's lost the momentum to browse. She just wants to log in and immediately see what's available without unnecessary steps slowing her down.
A streamlined e-commerce login system would get customers like Maria straight to the products they want to see, eliminating frustrating delays between authentication and actual shopping.

##### **Project Setup**

Create a new file `app.py`:

```python
import streamlit as st

st.title("🛒 Shop Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "admin" and password == "password":
        st.success("Login successful! Redirecting...")
        st.switch_page("pages/dashboard.py")
    else:
        st.error("Invalid username or password")

st.write("**Demo credentials:** admin / password")

```

Create a `pages` folder and add `dashboard.py`:

```python
import streamlit as st

st.title("🛒 Shopping Dashboard")
st.write("Welcome! Here are our featured products:")

products = [
    {"name": "Laptop", "price": "$999"},
    {"name": "Headphones", "price": "$199"},
    {"name": "Mouse", "price": "$49"}
]

for product in products:
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.write(f"**{product['name']}**")
    with col2:
        st.write(product['price'])
    with col3:
        if st.button(f"Buy", key=product['name']):
            st.switch_page("pages/checkout.py")

```

Add `checkout.py` to the `pages` folder:

```python
import streamlit as st

st.title("🛒 Checkout")

st.write("**Order Summary:**")
st.write("• Selected item: Laptop")
st.write("• Price: $999")
st.write("• Tax: $99")
st.write("• **Total: $1,098**")

name = st.text_input("Full Name")
email = st.text_input("Email")

if st.button("Complete Purchase"):
    if name and email:
        st.switch_page("pages/success.py")
    else:
        st.error("Please fill in all fields")

```

Finally, add `success.py` to the `pages` folder:

```python
import streamlit as st

st.title("🎉 Order Complete!")

st.success("Thank you for your purchase!")
st.write("Your order has been confirmed and will ship within 2 business days.")
st.write("**Order #12345**")

if st.button("Continue Shopping"):
    st.switch_page("pages/dashboard.py")

if st.button("Logout"):
    st.switch_page("app.py")

```

**Run your app with:**

```
streamlit run app.py

```

##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%208/ecom1mod8.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%208/ecom2mod8.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%208/ecom3mod8.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%208/ecom4mod8.png">

---

#### **Step-by-Step Walkthrough**

-   **`st.switch_page()`** — Instantly redirects users to another page programmatically, unlike links which require manual clicks.
    
-   **Conditional usage** — Typically placed inside actions like button clicks or form submissions to move users automatically (e.g., login → dashboard).
    
-   **Path argument** — Accepts the relative path of the target page file, ensuring smooth navigation without extra user steps.
    
-   **Sequential flows** — Enables chaining of pages (e.g., login → dashboard → checkout → success) for guided, app-like experiences.


#### **Conclusion**

Programmatic page switching transforms applications into guided user flows that lead users through logical progressions rather than leaving navigation entirely to chance. This approach creates polished, intuitive experiences that feel less like browsing separate sections and more like following a carefully designed journey. These flow control patterns represent essential techniques for building applications that actively guide users through complex processes, onboarding sequences, and multi-step workflows across any platform.
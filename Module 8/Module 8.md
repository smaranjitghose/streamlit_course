# Module 8: Multi-Page Applications & Navigation

### Topic 8.1: Page Basics

----

#### **Introduction**

Imagine opening an app that throws everything at you at once—a messy wall of calculators, charts, forms, and random features all crammed into one endless scroll. You start exploring at the top, but by the time you've scrolled halfway down, you've completely forgotten what was available at the beginning. Now compare that to opening Instagram, where you get clean tabs for your feed, search, and profile, or Netflix with its organized sections for browsing, your list, and settings. The difference is dramatic—organized apps feel intuitive and professional, while cluttered single-page apps feel overwhelming and amateur.

Streamlit's multi-page system transforms chaotic single-page applications into organized, professional experiences by enabling developers to split functionality into focused, logical sections that users can navigate naturally. This approach creates clean information architecture where each page serves a specific purpose, allowing applications to scale gracefully while maintaining the intuitive navigation patterns that users expect from modern digital experiences.

#### **Mini Project**

Students at TechU University are frustrated because they need different types of information but everything is crammed onto one overwhelming page. They can't quickly distinguish between general information, academic programs, and contact details, making simple tasks unnecessarily time-consuming. A multi-page university website would organize content into dedicated sections, letting students navigate directly to what they need.

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


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%208/mod8-uni1tldraw.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%208/mod8-uni2tldraw.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%208/mod8-uni3tldraw.png">


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

----

#### **Introduction**

Some apps feel like they're reading your mind—just as you finish uploading a file, a "Process Data" button appears right where you need it, or after completing a form, a "View Results" link guides you seamlessly to the next step. Compare that to apps where you constantly hunt through sidebar menus trying to figure out where to go next—the difference is striking. Modern applications use contextual navigation that feels natural and intuitive, placing navigation controls directly within content flows rather than hiding them in separate menu systems. Streamlit's page links enable this smooth, guided user experience.

Streamlit's page link functionality allows developers to embed navigation directly into content flows, creating "Next Step" buttons, contextual redirects, and guided workflows that appear exactly where users need them. This approach transforms rigid sidebar navigation into intuitive, content-driven experiences where users naturally progress through applications without hunting for the right menu option or losing track of their workflow.

#### **Mini Project**

Kavita needs to check her payslip before a meeting but navigating her company's employee portal is a frustrating maze of nested menus. She wastes time clicking through multiple sections just to find simple documents. An efficient employee portal would provide Kavita with clear page links to payslips, leave requests, and profile updates from one central dashboard, eliminating the navigation maze.

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

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%208/mod8-emp1tldraw.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%208/mod8-emp2tldraw.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%208/mod8-emp3tldraw.png">



<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%208/mod8-emp4tldraw.png">


----

#### **Step-by-Step Walkthrough**

- **`st.page_link()`** creates a button that navigates to another page in your app. The first parameter is the path to the page file, and you can add a custom label and icon to make it clear where the button leads.

  - **The label parameter** lets you customize what text appears on the button. Instead of showing the filename, you can write something user-friendly like "View Payslips" or "Edit Profile."
  
  - **The icon parameter** adds a visual element that makes buttons more recognizable. Users can quickly spot the payslip button by the money emoji or the profile button by the person icon.

- **Bidirectional navigation** works by putting page links on both the main page and the sub-pages. The main page links forward to specific sections, while each section links back to the main dashboard, creating a smooth user flow.


#### **Conclusion**

Strategic placement of navigation elements within content creates intuitive user journeys that guide users through complex workflows without relying on traditional menu systems. This contextual navigation approach transforms fragmented interfaces into cohesive experiences where each interaction feels purposeful and logically connected to the user's current task. 

-----

### Topic 8.3: Switch Pages

---

#### **Introduction**

Intelligent navigation creates smooth user experiences by automatically guiding users to their next destination after completing actions. When someone logs into their banking app, they expect to land directly on their account dashboard; when they finish an online purchase, they should automatically reach the confirmation page without manual navigation. This seamless flow eliminates confusion and makes applications feel professional and intuitive by anticipating user needs. Streamlit's switch page functionality enables these smart, automatic redirects.

Streamlit's `st.switch_page()` function allows you to programmatically navigate users to different pages based on actions, conditions, or workflow completion. Instead of users having to figure out where to go next after completing tasks, applications can automatically guide them to the appropriate destination, creating professional, intuitive experiences where navigation happens naturally as part of the user's workflow.

#### **Mini Project**

Anita wants to quickly check her favorite online store during lunch break, but she's forced to navigate through multiple pages after logging in - first a welcome page, then clicking through menus to reach products. By the time she gets to the shopping section, her break is nearly over. A streamlined e-commerce login system would get customers like Anita straight to the products they want to see, eliminating delays between authentication and actual shopping.

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


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%208/mod8-ecom1tldraw.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%208/mod8-ecom2tldraw.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%208/mod8-ecom3tldraw.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%208/ecom4mod8.png">

---

#### **Step-by-Step Walkthrough**

-   **`st.switch_page()`** — Instantly redirects users to another page programmatically, unlike links which require manual clicks.
    
-   **Conditional usage** — Typically placed inside actions like button clicks or form submissions to move users automatically (e.g., login → dashboard).
    
-   **Path argument** — Accepts the relative path of the target page file, ensuring smooth navigation without extra user steps.
    
-   **Sequential flows** — Enables chaining of pages (e.g., login → dashboard → checkout → success) for guided, app-like experiences.


#### **Conclusion**

Programmatic page switching transforms applications into guided user flows that lead users through logical progressions rather than leaving navigation entirely to chance. This approach creates polished, intuitive experiences that feel less like browsing separate sections and more like following a carefully designed journey. These flow control patterns represent essential techniques for building applications that actively guide users through complex processes, onboarding sequences, and multi-step workflows across any platform.
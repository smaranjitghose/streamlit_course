# Module 8: Multi-Page Applications & Navigation

### Topic 8.1: Page Basics


<br>

#### **Introduction**

You know how confusing it gets when you cram everything onto one page? Your friend shows you their cool app, but it's this endless scroll of different features all mashed together - a calculator, then some charts, then a form, then more stuff. By the time you scroll down, you've forgotten what was at the top.

Real apps don't work like this. When you open Instagram, you get separate tabs for your feed, search, and profile. Netflix has different pages for browsing, your list, and account settings. Each page has one clear job, making everything easier to find and use. That's exactly what Streamlit's pages system gives you - the power to split your app into focused, organized sections that users can navigate naturally.

#### **Mini Project**

You're building a university website with separate pages for different purposes. Students need a homepage with key information, a courses page to browse programs, and a contact page to get in touch. Each page serves a different need and deserves its own focused space.

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


![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/43tfadctp/content/43wzzj6zy/mod8uni1.png)


![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/43tfadctp/content/43wzzj6zy/mod8uni2.png)


![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/43tfadctp/content/43wzzj6zy/mod8uni3.png)


----

#### **Step-by-Step Walkthrough**

- **The pages folder** is where Streamlit looks for additional pages. Any Python file you put in this folder automatically becomes a new page in your app. The folder must be named exactly `pages` and be in the same directory as your main app file.

- **File naming in pages** determines both the URL and display name. The format `1_📚_Courses.py` creates a page called "Courses" with a book emoji. The number `1_` controls the order of the file in the navigation menu.

- **Each page is independent** - they're separate Python files that run independently. You can import different libraries, use different layouts, or create completely different user experiences on each page.

- **Navigation happens automatically** - Streamlit creates a sidebar navigation menu based on your pages folder contents. Users can click between pages, and each page loads its own content without you writing any navigation code.

----

#### **Conclusion**

Multi-page apps elevate Streamlit projects from single-page demos to full-fledged applications. By splitting content into focused pages, you deliver smoother, more intuitive user experiences that mirror professional web apps. Best of all, Streamlit’s pages system handles the navigation for you, so creating multi-page workflows is both simple and powerful.

----

### Topic 8.2: Page Links

<br>

#### **Introduction**

Ever noticed how some apps feel more like websites? Instead of just having that sidebar menu, they have buttons right in the content that say things like "Go to Settings" or "View Your Orders." These buttons feel more natural than hunting through menus - they guide you exactly where you need to go next.

In Streamlit, **Page links** let you create these smooth navigation experiences. Instead of users figuring out where to click in a sidebar, you can put helpful "Next Step" buttons right where they make sense in your content flow.

#### **Mini Project**

You're building an HR self-service portal where employees can access their information quickly. Instead of making them hunt through menus, you'll create a main dashboard with clear buttons that take them directly to payslips, leave requests, or profile updates.

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


![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/43tfadctp/content/43x22y9bw/emp1mod8.png)


![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/43tfadctp/content/43x22y9bw/emp2mod8.png)


![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/43tfadctp/content/43x22y9bw/emp3mod8.png)



![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/43tfadctp/content/43x22y9bw/emp4mod8.png)


----

#### **Step-by-Step Walkthrough**

- **st.page_link()** creates a button that navigates to another page in your app. The first parameter is the path to the page file, and you can add a custom label and icon to make it clear where the button leads.

- **The label parameter** lets you customize what text appears on the button. Instead of showing the filename, you can write something user-friendly like "View Payslips" or "Edit Profile."

- **The icon parameter** adds a visual element that makes buttons more recognizable. Users can quickly spot the payslip button by the money emoji or the profile button by the person icon.

- **Bidirectional navigation** works by putting page links on both the main page and the sub-pages. The main page links forward to specific sections, while each section links back to the main dashboard, creating a smooth user flow.


#### **Conclusion**

Page links transform your multi-page apps from menu-driven interfaces into guided experiences. By placing navigation buttons where they make logical sense in your content, you help users move through your app more naturally. This creates apps that feel less like collections of separate pages and more like cohesive, well-designed workflows.

-----

### Topic 8.3: Switch Pages


<br>

#### **Introduction**

You know how some apps automatically take you to the next screen after you do something? Like when you log into your bank app and it immediately shows your account dashboard, or when you complete a purchase and suddenly you're on the "Thank You" page? That's not you clicking a link - the app is moving you along automatically.

Streamlit switch pages help us create these smart, automatic redirects. Instead of users having to figure out where to go next after completing an action, we can programmatically send them to the right place at the right time, making our apps feel more professional and user-friendly.

#### **Mini Project**

You're building an e-commerce app where customers need to log in before they can browse products. After entering correct credentials, they should automatically land on the shopping dashboard - no extra clicks needed.

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


![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/43tfadctp/content/43x2556bn/ecom1mod8.png)


![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/43tfadctp/content/43x2556bn/ecom2mod8.png)


![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/43tfadctp/content/43x2556bn/ecom3mod8.png)


![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/43tfadctp/content/43x2556bn/ecom4mod8.png)

---

#### **Step-by-Step Walkthrough**

-   **`st.switch_page()`** — Instantly redirects users to another page programmatically, unlike links which require manual clicks.
    
-   **Conditional usage** — Typically placed inside actions like button clicks or form submissions to move users automatically (e.g., login → dashboard).
    
-   **Path argument** — Accepts the relative path of the target page file, ensuring smooth navigation without extra user steps.
    
-   **Sequential flows** — Enables chaining of pages (e.g., login → dashboard → checkout → success) for guided, app-like experiences.


#### **Conclusion**

Page switching takes multi-page apps a step further by turning them into guided user flows. Instead of leaving navigation entirely up to the user, you can design smooth progressions that lead them from one step to the next. The result is a more polished, intuitive experience that feels less like browsing and more like being guided through a journey.
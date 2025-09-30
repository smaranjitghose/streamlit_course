# Module 10: Building Chat Applications

### Topic 10.1: Chat Basics

----

#### **Introduction**

Getting help online often feels unnecessarily complicated—you click through endless dropdown menus, fill out contact forms, and scroll through FAQ pages that never quite answer your specific question. Meanwhile, you're thinking, "Why can't I just ask what I need like I would in a text message?" This disconnect between how we naturally communicate and how most websites force us to interact creates frustrating, impersonal experiences. Streamlit's chat functions bridge this gap by enabling natural, conversational interactions that feel familiar and intuitive.

The `st.chat_input()` function captures user messages with a familiar text input interface, while `st.chat_message()` displays conversations with proper message formatting and sender identification. These components work together with session state to preserve chat history across app reruns, enabling you to build conversational interfaces that maintain context over time and create engaging, messaging-style interactions that users intuitively understand.

#### **Mini Project**

Nisha places an online order but realizes she needs to cancel it immediately, so she opens the company's chat support expecting quick help. Instead, she's stuck typing exactly the right keywords to get responses, and when she makes a simple typo like "cancle order," the system doesn't understand and makes her start over. A customer service bot would understand Nisha's requests even with spelling mistakes, keep track of their entire conversation, and provide helpful responses that feel like talking to a real person rather than fighting with a rigid system.

##### **Project Setup**

Create a new file `app.py`:

```python
import streamlit as st
from difflib import get_close_matches

st.title("💬 Customer Service Bot")

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Available commands and their aliases
commands = {
    'cancel': ['cancel', 'stop', 'abort'],
    'postpone': ['postpone', 'delay', 'postpne'],
    'reschedule': ['reschedule', 'change', 'move'],
    'status': ['status', 'check', 'track'],
    'refund': ['refund', 'money', 'return'],
    'help': ['help', 'commands', 'options']
}

def find_command(user_input):
    user_input = user_input.lower().strip()
    
    # Check exact matches first
    for cmd, aliases in commands.items():
        if user_input in aliases:
            return cmd
    
    # Check fuzzy matches
    all_aliases = [alias for aliases in commands.values() for alias in aliases]
    matches = get_close_matches(user_input, all_aliases, n=1, cutoff=0.6)
    
    if matches:
        for cmd, aliases in commands.items():
            if matches[0] in aliases:
                return cmd
    
    return None

def get_bot_response(command):
    responses = {
        'cancel': "I can help you cancel your order. Please provide your order number.",
        'postpone': "I'll help you postpone your delivery. When would you like it delivered?",
        'reschedule': "Let me help you reschedule. What's your preferred new date?",
        'status': "I'll check your order status. Please share your order number.",
        'refund': "I can process your refund request. Please provide your order details.",
        'help': "Available commands: cancel, postpone, reschedule, status, refund, help"
    }
    
    return responses.get(command, "I didn't understand that. Type 'help' for available commands.")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Process command and generate response
    command = find_command(prompt)
    bot_response = get_bot_response(command)
    
    # Add bot response to history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    
    # Display bot response
    with st.chat_message("assistant"):
        st.write(bot_response)
```

**Run your app with:**

```bash
streamlit run app.py
```
---

##### **Output**

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%2010/mod10-chat.png">


---

#### **Step-by-Step Walkthrough**


-   **`difflib`**: A Python standard library module for comparing sequences. It provides `get_close_matches()`, which finds the closest matches to a given string within a list. Here, it’s used to detect typos or near matches in user input when identifying commands.
    
-   **`st.chat_message()`**: A Streamlit component that displays a single message in the chat interface. It takes a `"role"` parameter (`"user"` or `"assistant"`) to style messages differently, creating a clear conversation flow.
    
-   **`st.chat_input()`**: Provides an input box at the bottom of the chat interface for the user to type a message. It returns the entered text once submitted. In this app, the walrus operator (`:=`) is used so the input is captured and checked in one step.
    
-   **`commands` dictionary**: Defines main commands (`cancel`, `postpone`, `status`, etc.) along with their aliases and common misspellings. This enables flexible recognition of different user inputs mapping to the same intent.
    
-   **`find_command(user_input)`**: Identifies the intended command. It first checks for exact alias matches, then applies fuzzy matching with `get_close_matches()` to catch typos (e.g., `"canel"` → `"cancel"`).
    
-   **`get_bot_response(command)`**: Provides predefined responses linked to each recognized command. If no match is found, a default fallback message asks the user to type `"help"`.
    
-   **Help command**: Returns a list of all available commands so users know what options the bot can handle.

#### **Conclusion**

Chat-based interfaces transform rigid form interactions into natural conversations that feel more human and intuitive to users. These patterns enable applications to guide users through complex processes using simple dialogue, making everything from customer support to data entry more accessible and engaging. This conversational approach fundamentally changes how people interact with applications, creating experiences that feel like talking to a helpful assistant rather than navigating through menus and forms.

----

### Topic 10.2: Multi-Turn Conversations
----

#### **Introduction**

While basic chat interfaces handle simple question-and-answer exchanges, real conversations require memory and context to guide users through complex multi-step processes. When you call a restaurant for reservations, each exchange builds on previous information—party size leads to time preferences, which leads to availability checking—creating natural conversational flow. Traditional chatbots fail at this continuity by treating each message as isolated, losing the thread that makes interactions productive. Streamlit's session state enables multi-turn dialog management that maintains conversation context across exchanges, tracking what's been discussed and what questions remain, creating guided flows where applications can ask clarifying questions and branch conversations based on accumulated context for interactions that feel natural and purposeful.

#### **Mini Project**

Siddharth ordered a laptop online and wants to check its shipping status, but the company's current support system forces him through a frustrating maze of dropdown menus and form fields just to ask a simple question. When he finally enters his order number, the system often doesn't recognize it or asks him to verify information he already provided. A conversational support bot would let Siddharth simply ask about his order status and naturally guide him through providing his order ID, making the whole interaction feel like talking to a helpful person rather than wrestling with a confusing system.

##### **Project Setup**

Create a new file `app.py`:


```python
import streamlit as st, re

st.title("💬 Customer Support Chat")

# Initialize session state
st.session_state.setdefault("messages", [])
st.session_state.setdefault("dialog_state", {"waiting_for": None, "intent": None})

def detect_intent(msg):
    msg = msg.lower()
    if any(x in msg for x in ["order", "status", "track"]): return "order_status"
    if any(x in msg for x in ["refund", "return", "money"]): return "refund_policy"
    if any(x in msg for x in ["shipping", "delivery", "time"]): return "shipping_info"
    return "general"

def valid_order_id(order_id): 
    return bool(re.match(r"^[A-Za-z0-9]{6,10}$", order_id))

def bot_reply(user_msg):
    state = st.session_state.dialog_state
    if state["waiting_for"] == "order_id":
        if valid_order_id(user_msg):
            st.session_state.dialog_state = {"waiting_for": None, "intent": None}
            return f"✅ Order {user_msg} found. Status: Shipped - Delivery tomorrow."
        return "❌ Invalid order ID. Please enter 6–10 alphanumeric characters."
    if state["waiting_for"] == "refund_reason":
        st.session_state.dialog_state = {"waiting_for": None, "intent": None}
        return f"Refund noted: {user_msg}. Our team will email you in 24h."

    intent = detect_intent(user_msg)
    if intent == "order_status":
        st.session_state.dialog_state = {"waiting_for": "order_id", "intent": intent}
        return "Please provide your Order ID to check status."
    if intent == "refund_policy":
        st.session_state.dialog_state = {"waiting_for": "refund_reason", "intent": intent}
        return "Why would you like to return your item?"
    if intent == "shipping_info":
        return "🚚 Standard: 3–5 days | Express: 1–2 days"
    return "I can help with order status, refunds, or shipping info. What would you like to know?"

# Display chat history
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.write(m["content"])

# Chat input
if prompt := st.chat_input("Ask me about your order..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.write(prompt)

    reply = bot_reply(prompt)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"): st.write(reply)

```

**Run your app with:**

```bash
streamlit run app.py
```
---

##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%2010/mod10-customer.png">

---

#### **Step-by-Step Walkthrough**

-   **`re`**: Python’s standard library for regular expressions. It’s used to validate order IDs by matching them against a pattern of 6–10 alphanumeric characters.

-   **`st.chat_message()`**: A Streamlit component that displays a single message in the chat interface. It takes a `"role"` parameter (`"user"` or `"assistant"`) to style messages differently, making the conversation visually clear.

-   **`st.chat_input()`**: Provides an input box at the bottom of the chat for the user to type messages. It returns the text once submitted. In this app, the walrus operator (`:=`) is used to capture and process the input in one step.

-   **`st.session_state`**: A persistent storage object that retains data across reruns. In this app, `messages` stores the full conversation as a list of dictionaries (`{"role": "...", "content": "..."}`), and `dialog_state` tracks the current state of the conversation (e.g., waiting for order ID or refund reason).

-   **`detect_intent(user_input)`**: Analyzes the user’s message to determine intent based on keywords. Possible intents include `"order_status"`, `"refund_policy"`, `"shipping_info"`, or `"general"` if no keywords match.

-  ** `valid_order_id(order_id)`**: Validates whether the provided order ID meets the required format (6–10 alphanumeric characters). Returns `True` if valid, `False` otherwise.

-   **`bot_reply(user_input)`**: The main dialog handler that returns the assistant’s response. It uses `dialog_state` to determine if the bot is waiting for specific information (like order ID or refund reason). For new conversations, it calls `detect_intent()` to decide the next action and sets the appropriate state.

#### **Conclusion**

Multi-turn conversation management enables applications to handle complex workflows through structured dialogue that maintains context and intent across extended user interactions. These patterns transform rigid command interfaces into adaptive dialog systems that can guide users through troubleshooting, data collection, and decision-making processes with human-like understanding. This approach represents the evolution from static forms to intelligent conversational experiences that can adapt their flow based on user responses and provide personalized assistance at scale.

----

### Topic 10.3: Streaming Responses

---

#### **Introduction**

Instant response delivery in chat applications feels unnatural and robotic—imagine asking a complex question and receiving a complete, lengthy answer that appears all at once on your screen, missing the natural rhythm of human conversation where thoughts develop progressively and responses build piece by piece. Real conversations involve gradual communication that creates anticipation and maintains engagement, while traditional applications that dump complete responses instantly feel mechanical and disconnected from how people naturally interact. Streamlit's `st.write_stream()` function transforms this experience by creating the illusion of real-time thinking and typing, displaying content gradually as if it's being generated live, which maintains user engagement and creates more natural, conversational interactions that feel organic rather than mechanical.

#### **Mini Project**

Pooja wants to tell her 6-year-old daughter creative bedtime stories but often runs out of ideas after a long day at work. When she tries to make up stories on the spot, they lack structure and excitement, leaving her daughter unengaged and asking for "just one more story" that Pooja struggles to create. An interactive storytelling bot would transform bedtime into a magical experience, crafting engaging tales around any theme her daughter suggests while building suspense through gradual storytelling that keeps little listeners captivated until the very end.

##### **Project Setup**

Create a new file `app.py`:

```python
import streamlit as st
import time

st.title("📖 Storyteller Bot")

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'story_generated' not in st.session_state:
    st.session_state.story_generated = False

def generate_story(theme):
    """Generator function that yields story content with delays"""
    
    stories = {
        'space adventure': [
            "Captain Maya adjusted her helmet as the spaceship approached the mysterious planet.",
            "The surface was covered in crystalline structures that pulsed with an eerie blue light.",
            "As she stepped out of the airlock, the ground beneath her feet hummed with energy.",
            "Suddenly, one of the crystals began to glow brighter, revealing an ancient message."
        ],
        'mystery': [
            "Detective Chen examined the locked room where the victim was found.",
            "There were no signs of forced entry, yet the window was open to the rain.",
            "On the desk lay a half-finished letter with just two words: 'Trust nobody.'",
            "As thunder rolled overhead, Chen noticed something strange about the bookshelf."
        ],
        'fantasy': [
            "The old wizard's tower stood crooked against the stormy sky.",
            "Elara clutched her staff tighter as she climbed the winding stone steps.",
            "Each door she passed was marked with glowing runes that whispered secrets.",
            "At the top, she found not a wizard, but a dragon reading an ancient book."
        ],
        'magical animals': [
            "In the heart of the Enchanted Forest, a shimmering unicorn named Luna appeared.",
            "Her mane sparkled with the colors of the rainbow, and she spoke in a gentle, musical voice.",
            "Luna invited the young adventurer to follow her to a hidden glade filled with talking animals.",
            "Together, they solved riddles, discovered magical treasures, and made friends that would last a lifetime."
        ]
    }
    
    story_parts = stories.get(theme.lower(), [
        "Once upon a time, in a place far from here, something unusual happened.",
        "The main character faced a challenge they had never encountered before.",
        "With determination and courage, they began their journey.",
        "And that's how their greatest adventure began."
    ])
    
    for part in story_parts:
        yield part + "\n\n"
        time.sleep(3) 

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("What kind of story would you like? (space adventure, mystery, fantasy)"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.write(prompt)
  
    bot_response = f"Let me tell you a {prompt} story..."
 
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
   
    with st.chat_message("assistant"):
        st.write(bot_response)
   
    with st.chat_message("assistant"):
        story_content = st.write_stream(generate_story(prompt))
 
    st.session_state.messages.append({"role": "assistant", "content": story_content})

```

**Run your app with:**

```bash
streamlit run app.py
```
----

##### **Output**

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%2010/mod10-story.png">

----
#### **Step-by-Step Walkthrough**

-   **time**: Python standard library used to create delays between story segments. Here, `time.sleep(3)` pauses execution for 3 seconds to simulate real-time storytelling.
    
-   **st.session_state.messages**: Stores the conversation history as a list of dictionaries with `"role"` and `"content"` so previous messages remain visible.
    
-   **st.session_state.story_generated**: A boolean flag used to track whether a story has already been generated, preventing duplicate storytelling if needed.
    
-   **generate_story(theme)**: A generator function that produces story segments one by one.
    
    -   Accepts a `theme` (e.g., `"space adventure"`, `"mystery"`, `"fantasy"`, `"magical animals"`).
        
    -   Contains predefined story parts for each theme; defaults to a generic story if the theme is unrecognized.
        
    -   Uses `yield` to return each segment individually and `time.sleep(3)` between segments for a dynamic storytelling effect.
        
-   **Bot response**: After the user provides a theme:
    
    -   Generates an initial message: `"Let me tell you a {prompt} story..."`.
        
    -   Calls `st.write_stream(generate_story(prompt))` to display the story in parts.
        
    -   Appends the full story to `st.session_state.messages` to preserve it in chat history.
        
-   **Default story handling**: If the user enters a theme not in the predefined list, a generic 4-part story is generated and displayed dynamically, ensuring the bot always responds.
    
-   **Story display loop**: Iterates over `st.session_state.messages` to render previous messages, maintaining continuity of the conversation.

#### **Conclusion**

Progressive content delivery through streaming transforms passive waiting experiences into engaging, real-time interactions that keep users actively involved in the generation process. These patterns enable developers to build applications where the content creation itself becomes part of the user experience, from AI writing assistants to interactive storytelling platforms. This approach to real-time content streaming represents a fundamental shift toward more engaging user interfaces that turn potentially slow processes into captivating, interactive experiences.

----

### Topic 10.4: Data-Driven Chat
---

#### **Introduction**

Traditional chatbots fail when users ask "How do I get my money back?" but systems only recognize exact phrases like "refund policy," creating frustrating "I don't understand" responses despite having relevant information available. This rigid matching creates a disconnect between natural language and structured data, making helpful content inaccessible due to phrasing differences. **Data-driven chatbots** solve this by connecting conversational interfaces to knowledge sources and using similarity matching to understand that different phrasings mean the same thing—recognizing that "getting money back" relates to refund policies and "cancel my order" connects to cancellation procedures, enabling scalable systems that provide accurate responses while naturally handling the diverse ways people express questions.

#### **Mini Project**

Manisha manages customer support for a growing software company and watches her team answer the same basic questions dozens of times daily while complex issues pile up. Customers get frustrated waiting for simple answers, and support agents feel burnt out repeating identical responses. An intelligent FAQ chatbot would instantly recognize common questions and pull answers from the knowledge base, freeing up Manisha's team for complex issues while giving customers immediate help.

##### **Project Setup**

Create a csv file `faq_data.csv`:

```csv
Question,Answer
How do I track my order?,You can track your order using the tracking number sent to your email. Visit our tracking page and enter your number.
What is your return policy?,We accept returns within 30 days of purchase. Items must be in original condition with tags attached.
How long does shipping take?,Standard shipping takes 3-5 business days. Express shipping takes 1-2 business days.
Do you offer international shipping?,Yes we ship to most countries. International shipping takes 7-14 business days.
How do I cancel my order?,Orders can be canceled within 2 hours of placement. Contact customer service or use your order confirmation link.
What payment methods do you accept?,We accept all major credit cards PayPal and bank transfers.
How do I create an account?,Click the Sign Up button on our homepage and fill out the registration form with your email and password.

```

Create a new file `app.py`:

```python
import streamlit as st
import pandas as pd
from difflib import get_close_matches

st.title("Customer Service FAQ Bot")

# Load FAQ data
@st.cache_data
def load_faq():
    return pd.read_csv("faq_data.csv")

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

faq_df = load_faq()

def find_answer(question):
    questions = faq_df['Question'].tolist()
    match = get_close_matches(question.lower(), [q.lower() for q in questions], n=1, cutoff=0.4)
    if match:
        orig_q = questions[[q.lower() for q in questions].index(match[0])]
        return faq_df.loc[faq_df['Question']==orig_q, 'Answer'].iloc[0], orig_q
    return None, None

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
if prompt := st.chat_input("Ask me anything about our services..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    answer, matched_q = find_answer(prompt)
    if answer:
        bot_msg = f"**Answer:** {answer}"
        if matched_q.lower() != prompt.lower():
            bot_msg += f"\n\n*This answer is for: {matched_q}*"
    else:
        topics = ["Order Tracking", "Returns", "Shipping", "Payment", "Account"]
        bot_msg = "I don't have a specific answer. Try these topics:\n" + "\n".join(f"• {t}" for t in topics)
    
    st.session_state.messages.append({"role": "assistant", "content": bot_msg})
    with st.chat_message("assistant"):
        st.write(bot_msg)

```

**Run your app with:**

```bash
streamlit run app.py
```
----

##### **Output**

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%2010/mod10-faq.png">

-----

#### **Step-by-Step Walkthrough**

-   **`difflib.get_close_matches()`**: A function from Python’s standard library `difflib` that finds the closest matches to a given string within a list. It allows the bot to handle typos or near matches when comparing the user’s question to stored FAQ questions.
    
-   **`@st.cache_data`**: Decorator that caches the result of `load_faq()` so the CSV file is read only once, improving performance.
    
-   **`load_faq()`**: Reads the FAQ CSV file and returns a DataFrame containing `Question` and `Answer` columns for searching.
    
-   **`st.session_state.messages`**: Stores the chat history as a list of dictionaries with `"role"` and `"content"`, ensuring previous messages remain visible across reruns.
    
-   **`find_answer(question)`**: Searches for the best matching FAQ question.
    
    -   Converts stored questions to lowercase and uses `get_close_matches()` with a cutoff of 0.4.
        
    -   Returns the corresponding answer and the original matched question if found; otherwise, returns `(None, None)`.
        
-   **`Bot response logic`**:
    
    -   If a matching FAQ is found, the bot displays the answer.
        
    -   If the matched FAQ question differs from the user’s input, the bot notes which question it matched.
        
    -   If no match is found, the bot suggests general topics like `"Order Tracking"`, `"Returns"`, `"Shipping"`, `"Payment"`, `"Account"`.
        
-   **Chat history display**: Iterates through `st.session_state.messages` and displays all previous messages using `st.chat_message()`, maintaining conversation continuity.
    
-   **Chat input handling**: Captures user input via `st.chat_input()` using the walrus operator (`:=`) to process the input immediately, then appends both the user message and bot response to `st.session_state.messages`.


#### **Conclusion**

Connecting conversational interfaces to structured data sources creates powerful automation tools applicable across customer service, internal help desks, and knowledge management systems. This architecture pattern enables any organization to leverage existing documentation and databases through natural language queries, reducing support overhead while improving information accessibility. The combination of semantic search with backup responses ensures users always receive helpful answers, even as your content library grows larger and more complex.
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
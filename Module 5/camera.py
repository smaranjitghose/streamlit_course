import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.title("📷 ID Card Maker")

# Camera input
photo = st.camera_input("Take your ID photo")

if photo is not None:
    # Convert to PIL Image
    image = Image.open(photo)
    
    # Get user details
    name = st.text_input("Enter your name", "John Doe")
    id_number = st.text_input("Enter ID number", "ID-001")
    
    if name and id_number:
        # Create ID card
        # Resize photo to standard size
        image = image.resize((300, 400))
        
        # Create new image for ID card
        card_width, card_height = 500, 300
        card = Image.new('RGB', (card_width, card_height), 'white')
        
        # Paste photo on left side
        photo_resized = image.resize((150, 200))
        card.paste(photo_resized, (20, 50))
        
        # Add text
        draw = ImageDraw.Draw(card)
        
        # Add name
        draw.text((200, 80), f"Name: {name}", fill='black')
        
        # Add ID number  
        draw.text((200, 120), f"ID: {id_number}", fill='black')
        
        # Add title
        draw.text((200, 40), "ID CARD", fill='blue')
        
        # Display the ID card
        st.subheader("Your ID Card")
        st.image(card)
        
        # Download functionality
        buf = io.BytesIO()
        card.save(buf, format="PNG")
        
        st.download_button(
            "Download ID Card",
            data=buf.getvalue(),
            file_name=f"id_card_{name.replace(' ', '_')}.png",
            mime="image/png"
        )
    
else:
    st.info("Take a photo to create your ID card")
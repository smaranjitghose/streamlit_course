import streamlit as st

st.title("📱 Smartphone Comparison Tool")
st.write("Compare phones side-by-side to make informed decisions")

# Product data
phones = [
    {
        'name': 'iPhone 15 Pro',
        'price': 'Rs. 90,999*',
        'image_url': 'https://cf-img-a-in.tosshub.com/sites/visualstory/wp/2024/08/iphone-15-pro-max-natural-titanium-desktop-detail-1-Format-488.png?size=*:900',
        'specs': {
            'Display': '6.1" Super Retina XDR',
            'Processor': 'A17 Pro chip',
            'Storage': '128GB / 256GB / 512GB / 1TB',
            'Camera': '48MP Main + 12MP Ultra Wide',
            'Battery': 'Up to 23 hours video',
            'Weight': '187g'
        },
        'pros': ['Premium titanium build quality', 'Excellent camera system', 
                 'Fast A17 Pro performance', 'Great ecosystem integration'],
        'cons': ['Higher price point', 'Limited customization', 
                 'No USB-C to Lightning adapter'],
        'verdict': 'Perfect for Apple users wanting premium build and top-tier cameras.',
        'rating': 4.5
    },
    {
        'name': 'Samsung S24 Ultra',
        'price': 'Rs. 97,999*',
        'image_url': 'https://cdn.beebom.com/mobile/samsung-galaxy-s24-ultra/samsung-galaxy-s24-ultra-front-back-5.png',
        'specs': {
            'Display': '6.8" Dynamic AMOLED 2X',
            'Processor': 'Snapdragon 8 Gen 3',
            'Storage': '256GB / 512GB / 1TB',
            'Camera': '200MP Main + 50MP Periscope',
            'Battery': 'Up to 30 hours video',
            'Weight': '232g'
        },
        'pros': ['S Pen included', 'Larger high-res display', 
                 'Superior zoom cameras', 'More storage options'],
        'cons': ['Heavier than competitors', 'Higher starting price', 
                 'Complex UI for some users'],
        'verdict': 'Best for power users needing S Pen, huge screen, and zoom cameras.',
        'rating': 4.7
    }
]

# Two-column layout
col1, col2 = st.columns(2)

for col, phone in zip([col1, col2], phones):
    with col:
        st.subheader(f"📱 {phone['name']}")
        st.image(phone['image_url'], use_container_width=True)
        st.metric("💰 Starting Price", phone['price'])
        
        st.write("**🔧 Key Specifications:**")
        for spec, val in phone['specs'].items():
            st.write(f"- **{spec}:** {val}")
        
        st.write("**✅ Pros:**")
        for pro in phone['pros']:
            st.write(f"- {pro}")
        
        st.write("**❌ Cons:**")
        for con in phone['cons']:
            st.write(f"- {con}")
        
        st.metric("⭐ Expert Rating", f"{phone['rating']}/5.0")
        st.write("**🎯 Final Verdict:**")
        st.write(phone['verdict'])

# Quick helper
st.divider()
st.subheader("🤔 Quick Decision Helper")
colA, colB = st.columns(2)

with colA:
    st.info("**Choose iPhone 15 Pro if you:**\n- Want seamless Apple ecosystem\n- Prefer compact premium design\n- Value consistent updates")

with colB:
    st.success("**Choose Galaxy S24 Ultra if you:**\n- Need S Pen for productivity\n- Want best zoom camera\n- Prefer larger screen & customization")

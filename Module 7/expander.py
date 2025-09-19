import streamlit as st

st.title("🆘 Customer Support FAQ")
st.write("Click on any question below to reveal the answer")

# FAQ list
faqs = [
    {
        "question": "🔑 How do I reset my password?",
        "answer": """
**Steps to reset your password:**
1. Go to the login page and click "Forgot Password"
2. Enter your registered email
3. Check your email for the reset link
4. Click the link and create a new password

**Need help?** Contact support@company.com
"""
    },
    {
        "question": "👤 My account is locked or suspended",
        "answer": """
**Possible reasons:**
- Too many failed login attempts
- Suspicious activity detected
- Payment issues

**What to do:**
1. Wait 30 minutes if multiple failed logins
2. Check your email for security notifications
3. Contact security@company.com if still locked
"""
    },
    {
        "question": "📞 How can I contact customer support?",
        "answer": """
**Email Support:** support@company.com  
**Live Chat:** Mon-Fri 9 AM–6 PM via website  
**Phone Support:** 1-800-SUPPORT, Mon-Fri 8 AM–8 PM EST
"""
    }
]

# Render FAQs with expanders
for faq in faqs:
    with st.expander(faq["question"]):
        st.markdown(faq["answer"])

st.divider()
st.info("💡 Didn't find what you're looking for? Email support@company.com for help!")

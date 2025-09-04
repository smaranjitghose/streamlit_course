import streamlit as st

st.set_page_config(page_title="Math Formula Helper", layout="wide")

st.title("Math Formula Helper 📐")
st.write("Select a category to see useful math formulas:")

category = st.sidebar.radio("Choose a topic:", ["Algebra", "Calculus", "Geometry"])

if category == "Algebra":
    st.subheader("Algebra Formulas")
    st.latex(r'a^2 - b^2 = (a-b)(a+b)')
    st.latex(r'(a+b)^2 = a^2 + 2ab + b^2')
    st.latex(r'(a-b)^2 = a^2 - 2ab + b^2')

elif category == "Calculus":
    st.subheader("Calculus Formulas")
    st.latex(r'\frac{d}{dx} \big( x^n \big) = nx^{n-1}')
    st.latex(r'\int_a^b f(x)\,dx')
    st.latex(r'e^{i\pi} + 1 = 0')

elif category == "Geometry":
    st.subheader("Geometry Formulas")
    st.latex(r'Area\ of\ Circle = \pi r^2')
    st.latex(r'Perimeter\ of\ Circle = 2 \pi r')
    st.latex(r'Pythagoras:\ a^2 + b^2 = c^2')

st.markdown("---")
st.info("💡 Tip: Use `st.latex()` to render any LaTeX formula in Streamlit.")

import streamlit as st

st.title("🎓 CS Exam Prep Cheatsheet")

st.divider()
st.header("📐 Mathematics")

st.subheader("Quadratic Equation")
st.badge("Medium")
st.caption("General formula for solving ax² + bx + c = 0")

st.latex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
st.latex(r"ax^2 + bx + c = 0")

st.caption("Python implementation with an example")
st.code('''
import math

def solve_quadratic(a,b,c):
    d = b**2 - 4*a*c
    if d > 0: return (-b+math.sqrt(d))/(2*a), (-b-math.sqrt(d))/(2*a)
    if d == 0: return -b/(2*a)
    return "No real solutions"

print(solve_quadratic(1,-5,6))  # x² - 5x + 6 = 0
''', language='python')

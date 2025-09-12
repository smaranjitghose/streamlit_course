import streamlit as st  

# Page Setup  
st.set_page_config(page_title="📘 Exam Prep Sheet", layout="centered")  

st.title("📘 Quick Exam Prep Sheet")  
st.write("Your go-to revision notes with formulas, code, and important highlights ✅")  
st.divider()  

# Section: Percentages  
st.header("📊 Percentages")  
st.badge("High Yield")  
st.latex(r"\text{Percentage (\%)} = \frac{\text{Value}}{\text{Total}} \times 100")  
st.code(""" 
# Example: Calculating percentage 
value = 45 
total = 60 
percentage = (value/total) * 100 
print(percentage)  # 75.0% 
""", language="python")  
st.caption("👉 Percentages are often tested in competitive exams like SSC, Banking, and Aptitude tests.")  
st.divider()  

# Section: Interest  
st.header("💰 Simple & Compound Interest")  
st.badge("Formula to Memorize")  
st.latex(r"SI = \frac{P \times R \times T}{100}")  
st.latex(r"CI = P \times \left(1 + \frac{R}{100}\right)^T - P")  
st.code(""" 
# Example: Simple Interest 
P = 1000  # Principal 
R = 5     # Rate per year 
T = 2     # Time in years 
SI = (P*R*T)/100 
print(SI)  # 100 
""", language="python")  
st.caption("Where P = Principal, R = Rate (%), T = Time (years)")  
st.divider()  

# Section: Averages  
st.header("📈 Averages")  
st.badge("Core Concept")  
st.latex(r"\text{Average} = \frac{\text{Sum of terms}}{\text{Number of terms}}")  
st.code(""" 
# Example: Finding average 
nums = [12, 15, 20, 25, 30] 
average = sum(nums)/len(nums) 
print(average)  # 20.4 
""", language="python")  
st.divider()  

# Section: Probability  
st.header("🎲 Probability")  
st.badge("Exam Favorite")  
st.latex(r"P(E) = \frac{\text{Favorable outcomes}}{\text{Total outcomes}}")  
st.code(""" 
# Example: Probability of rolling a 6 on dice 
favorable = 1    # only '6' 
total = 6        # six outcomes 
P = favorable / total 
print(P)  # 0.1667 or 16.67% 
""", language="python")  
st.divider()  

# Section: Permutations & Combinations  
st.header("🔢 Permutations & Combinations")  
st.badge("Important")  
st.latex(r"nPr = \frac{n!}{(n-r)!}")  
st.latex(r"nCr = \frac{n!}{r!(n-r)!}")  
st.code(""" 
import math 

# Example: nCr and nPr 
n, r = 5, 2 
nPr = math.factorial(n)//math.factorial(n-r) 
nCr = math.factorial(n)//(math.factorial(r)*math.factorial(n-r)) 
print(nPr, nCr)  # 20 , 10 
""", language="python")  

st.success("✅ Exam Prep Sheet ready! Use it for last-minute revision 📝")

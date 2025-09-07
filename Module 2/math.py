import streamlit as st

st.title("📘 Aptitude Formula Cheatsheet")
st.write("Quick reference for common aptitude formulas 🧮")

# Section 1: Percentages
st.header("📊 Percentages")
st.latex(r"\text{Percentage (\%)} = \frac{\text{Value}}{\text{Total}} \times 100")
st.latex(r"\text{Profit \%} = \frac{\text{Profit}}{\text{Cost Price}} \times 100")
st.latex(r"\text{Loss \%} = \frac{\text{Loss}}{\text{Cost Price}} \times 100")

# Section 2: Simple & Compound Interest
st.header("💰 Interest")
st.latex(r"SI = \frac{P \times R \times T}{100}")
st.latex(r"CI = P \times \left(1 + \frac{R}{100}\right)^T - P")
st.caption("where P = Principal, R = Rate %, T = Time")

# Section 3: Averages
st.header("📈 Averages")
st.latex(r"\text{Average} = \frac{\text{Sum of terms}}{\text{Number of terms}}")

# Section 4: Probability
st.header("🎲 Probability")
st.latex(r"P(E) = \frac{\text{Favorable outcomes}}{\text{Total outcomes}}")

# Section 5: Permutations & Combinations
st.header("🔢 Permutations & Combinations")
st.latex(r"nPr = \frac{n!}{(n-r)!}")
st.latex(r"nCr = \frac{n!}{r!(n-r)!}")

st.success("✅ Cheatsheet ready! Use this as a quick reference during practice.")

import streamlit as st

st.divider()
st.title("Statistical Analysis")
st.divider()
st.header("Normal Distribution Formula")
st.latex(r"\mu = \frac{\sum x_i}{n}")
st.latex(r"\sigma^2 = \frac{\sum(x_i - \mu)^2}{n}")
st.subheader("Sample Implementation")
st.code("def calculate_mean(data):\n    return sum(data) / len(data)", language="python")


st.divider()

st.subheader("📚 References")
st.markdown("""
1. **Johnson et al.** (2024) - *Machine Learning in Healthcare*  
   `DOI:10.1234/ml.2024` | Status: :green[Peer Reviewed]
   
2. **Chen & Wong** (2023) - *Neural Network Architectures*  
   `DOI:10.5678/nn.2023` | Status: :orange[In Press]
""")

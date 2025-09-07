import streamlit as st

st.title("Quantum Computing Bootcamp FAQ ❓")

with st.expander("What is Quantum Computing?"):
    st.write(
        "Quantum computing is a type of computation that uses quantum bits (qubits) "
        "and principles of quantum mechanics such as superposition and entanglement to perform operations."
    )

with st.expander("Who should attend this bootcamp?"):
    st.write(
        "This bootcamp is ideal for students, researchers, and professionals interested in learning "
        "the fundamentals of quantum computing and practical implementation using Qiskit or similar frameworks."
    )

with st.expander("Do I need prior knowledge of quantum mechanics?"):
    st.write(
        "No prior knowledge is required. We will cover the necessary concepts in a beginner-friendly manner."
    )

with st.expander("What tools and software will be used?"):
    st.write(
        "Participants will use Python and Qiskit (an open-source quantum computing framework by IBM) "
        "to simulate and run quantum circuits."
    )

with st.expander("Is there any certification?"):
    st.write(
        "Yes, upon successful completion, participants will receive a certificate of completion from the bootcamp."
    )

with st.expander("Is the bootcamp free or paid?"):
    st.write(
        "The bootcamp may have both free and paid tiers depending on the content and access to resources."
    )

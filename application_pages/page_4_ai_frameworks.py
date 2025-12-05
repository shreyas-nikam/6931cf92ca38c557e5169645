
import streamlit as st
from utils import go_to_page  # Import the navigation helper


def main():
    st.header("4. Foundations: SR 11-7 & NIST AI RMF 1.0")
    st.markdown("""
    ## Foundations of Financial Model Risk: SR 11-7 in an AI Context

    As a Quantitative Analyst in a financial institution, SR 11-7 (Supervisory Guidance on Model Risk Management) is your bedrock for model governance. While it predates modern AI, its core principles of Model Risk Management (MRM) remain highly relevant. You must consider how SR 11-7's pillars—model development, implementation, validation, and governance—translate to AI systems. This conceptual mapping ensures that even novel AI models are subject to the same rigor and oversight as traditional financial models, especially concerning "effective challenge" and sound governance.

    The definition of model risk under SR 11-7 is broad and encompasses the potential for adverse consequences from decisions based on incorrect or misused model outputs. This includes financial loss, reputational damage, and flawed decisions. The guidance emphasizes that model risk intensifies with greater model complexity, higher input uncertainty, broader extent of use, and larger potential impact. These considerations are particularly amplified with AI models due to their opacity and emergent behaviors.
    """)
    st.info("As a Quant Analyst, SR 11-7 is your bedrock for model governance. Remember: model risk intensifies with complexity, input uncertainty, and broader use.")

    st.markdown("""
    ## Embracing Trustworthy AI: The NIST AI RMF 1.0 Framework

    Beyond SR 11-7's financial focus, the NIST AI Risk Management Framework (AI RMF 1.0) provides a broader, cross-sector lens for managing AI risks and promoting trustworthy AI. As an AI Risk Manager, you recognize the need to integrate these principles, which encompass attributes like validity, reliability, safety, security, transparency, fairness, accountability, and privacy-preserving. This framework complements SR 11-7 by offering a structured approach to identifying, measuring, and managing the unique risks posed by AI systems across their entire lifecycle. You will leverage its taxonomy and attributes to ensure a comprehensive risk assessment.
    """)
    st.markdown(r"""
    The NIST AI RMF categorizes trustworthiness attributes as follows:
    -   **Validity**: Ensuring the AI system accurately performs its intended function and produces correct outputs for its specified purpose.
    -   **Reliability**: Guarantees consistent and stable performance of the AI system over time and across various operational conditions.
    -   **Safety**: Minimizing the potential for the AI system to cause harm to individuals, society, or the environment.
    -   **Security**: Protecting AI systems from adversarial attacks and ensuring data integrity.
    -   **Transparency**: Understanding how AI systems arrive at outputs, often through interpretability methods.
    -   **Fairness**: Identifying and mitigating biases encoded and amplified by AI to ensure equitable outcomes.
    -   **Accountability**: Establishing clear roles and policies for AI risk oversight to ensure responsibility for AI outcomes and decisions.
    -   **Privacy-Preserving**: Implementing strategies to address data sensitivity and integrating privacy by design.
    """)
    st.info("NIST AI RMF broadens the view beyond financial models, focusing on trustworthy AI attributes like Fairness, Transparency, and Accountability, which are crucial for any AI deployment.")

    st.markdown("---")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Previous Step", key="page4_prev_btn", use_container_width=True):
            go_to_page(2)  # Navigate to "Data Overview & Card"
    with col2:
        if st.button("Next: Identify AI Risks", key="page4_next_btn", use_container_width=True):
            go_to_page(4)  # Navigate to "AI Risk Register: Identify Risks"

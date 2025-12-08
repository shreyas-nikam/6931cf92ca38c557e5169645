
import streamlit as st
from utils import go_to_page  # Import the navigation helper


def main():
    st.markdown("""
In this lab, you will step into the shoes of a Quantitative Analyst at QuantBank, tasked with a critical mission: to conduct a formal risk assessment of a new AI-powered Credit Risk Scoring Model. This model is poised to automate loan approvals and flag high-risk applicants, making its integrity and compliance paramount.

This application will guide you through a systematic process, from understanding the model and its data to identifying, assessing, mitigating, and reporting AI risks. All steps are framed within the context of stringent financial regulations (SR 11-7) and best practices for trustworthy AI (NIST AI RMF 1.0). Each interactive step reflects a real-world task you would perform, moving you closer to ensuring responsible AI deployment at QuantBank.
""")
    st.markdown(r"""
    # 1. Setting the Scene: The Critical Role of an AI Risk Manager

    As a Quantitative Analyst at QuantBank, your primary responsibility is to ensure the integrity and compliance of all models used in critical financial decisions. Today, you've been tasked with a formal risk assessment of a newly developed AI-powered Credit Risk Scoring Model. This model, if deployed, will automate loan approval processes and flag high-risk applicants for manual review. Your assessment is crucial for compliance with regulatory standards like SR 11-7 and internal governance policies.

    The core principle guiding this assessment is the understanding that risk is a function of potential impact and likelihood. In quantitative terms, this can be expressed as:

    $$ Risk = Impact \times Likelihood $$

    Where *Impact* refers to the severity of adverse outcomes (e.g., financial loss, reputational damage, regulatory penalties), and *Likelihood* refers to the probability of the adverse event occurring. Your job is to systematically identify potential failure points and quantify these two dimensions for the AI model.
    """)

    st.markdown("""As a Quant Analyst at QuantBank, this first step sets the stage for a crucial task: ensuring the new AI Credit Risk Model is safe and compliant. Understanding the core concept that risk is a product of impact and likelihood is fundamental to your role, as it guides all subsequent assessments and prioritizations. This narrative introduces the stakes involved and the basic formula that will underpin your entire workflow.""")

    if st.button("Start Assessment", key="start_assessment_btn"):
        # Navigate to the next page (index 1 for "Model Overview & Card")
        go_to_page(1)


import streamlit as st
# Import the navigation helper
from utils import generate_risk_register_report, plot_risk_distribution, go_to_page


def main():
    st.header("9. Comprehensive AI Risk Report")
    st.markdown("""
    The ultimate deliverable of your assessment is a comprehensive AI Risk Register. This living document consolidates all identified risks, their assessment (impact, likelihood, score), and the proposed mitigation strategies. As a Risk Manager, you understand that this register is crucial for ongoing monitoring, auditability, and demonstrating compliance. It serves as the single source of truth for the AI model's risk profile, empowering the organization to manage it effectively throughout its lifecycle.
    """)
    st.subheader(
        "Comprehensive AI Model Risk Register: Credit Risk Scoring Model")
    final_ai_risk_register = generate_risk_register_report(
        st.session_state.risk_register_df)
    st.dataframe(final_ai_risk_register, use_container_width=True)

    st.subheader("Risk Distribution Across AI Dimensions")
    plot_risk_distribution(final_ai_risk_register)
    st.markdown("""
    The generated table represents the complete AI Risk Register, a critical deliverable. It provides a clear, sortable overview of all identified and assessed risks, along with their proposed mitigation strategies and responsible parties. The bar chart further aids in understanding the overall risk exposure, quickly showing which dimensions (e.g., Model, Data, Human) have the highest number of identified risks. This document is now ready for presentation, audit, and ongoing management, fulfilling a core requirement of both SR 11-7 and NIST AI RMF.
    """)

    st.markdown("""
    ## Concluding the Assessment: Preparing for Effective Challenge

    As a Quantitative Analyst, your detailed AI Risk Register and associated artifacts (Model Card, Data Card) form the basis for the "Effective Challenge" process. This principle, central to SR 11-7, mandates that objective and informed reviewers critically test models to identify hidden errors, biases, or limitations. By systematically identifying risks, assessing their impact, and proposing mitigations, you've provided the necessary documentation for internal validation teams, auditors, and senior management to rigorously scrutinize the Credit Risk Scoring Model. Your work ensures that QuantBank can deploy AI models with confidence, upholding regulatory compliance and fostering trustworthiness in AI. This iterative process of identification, assessment, mitigation, and challenge is crucial for continuous improvement and adaptive governance in AI risk management.
    """)
    st.markdown("---")
    if st.button("Restart Assessment", key="restart_assessment_btn"):
        go_to_page(0)  # Navigate back to the welcome page

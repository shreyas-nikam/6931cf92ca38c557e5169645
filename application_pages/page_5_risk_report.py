
import streamlit as st
import pandas as pd
from utils import generate_risk_report

def main():
    st.title("Comprehensive AI Risk Report")
    st.markdown("""
    As a Risk Manager, periodically generating a comprehensive AI Risk Report is vital for communicating the organization's risk posture to senior leadership, board members, and regulators. This report summarizes the key findings from the risk register, highlights high-priority items, and demonstrates adherence to frameworks like NIST AI RMF and SR 11-7. It provides an actionable overview that supports informed decision-making and demonstrates robust governance.
    """)

    if 'ai_risk_register_df' not in st.session_state or st.session_state.ai_risk_register_df.empty:
        st.warning("No AI Risk Register data available to generate a report. Please go to the 'Home' page to generate synthetic data or add risks via the 'AI Risk Register' page.")
        return

    st.header("Generate Risk Report")
    st.markdown("""
    Click the button below to generate a detailed markdown report based on the current AI Risk Register.
    """)
    if st.button("Generate Comprehensive Risk Report", key="generate_risk_report_button"):
        report_markdown = generate_risk_report(st.session_state.ai_risk_register_df)
        st.markdown(report_markdown)
        st.success("Risk report generated successfully!")

    st.divider()
    st.header("Conclusion")
    st.markdown("""
    This lab has guided you through the essential steps of establishing and managing an AI Model Risk Register, incorporating principles from SR 11-7 and the NIST AI Risk Management Framework. We've covered:

    *   **Understanding AI Risk Taxonomy**: Categorizing risks into Data, Model, System, Human, and Organizational dimensions.
    *   **Quantifying Risk Severity**: Calculating `Risk_Priority_Scores` based on `Likelihood` and `Impact`.
    *   **Visualizing Risk Landscape**: Using various charts to interpret risk distributions and priorities.
    *   **Tracking Mitigation Efforts**: Demonstrating how to update risk statuses dynamically.
    *   **Leveraging Assurance Artifacts**: Outlining the conceptual importance of Model Cards and Data Cards.
    *   **Generating Actionable Reports**: Creating a comprehensive summary for stakeholders.

    By applying these structured approaches, risk managers and data engineers can proactively identify, assess, mitigate, and monitor AI-specific risks, fostering trust, ensuring compliance, and supporting the responsible deployment of AI within their organizations. Continuous adaptation and monitoring are key to navigating the evolving landscape of AI risks.
    """)

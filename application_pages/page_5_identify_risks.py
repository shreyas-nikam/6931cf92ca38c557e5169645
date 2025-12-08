
import streamlit as st
from utils import add_risk_to_register, go_to_page  # Import the navigation helper


def main():
    st.header("5. AI Risk Register: Systematic Identification")
    st.markdown("""
    Now equipped with the model and data cards, and frameworks like SR 11-7 and NIST AI RMF, you begin the systematic identification of risks. You'll work through the five dimensions of the AI Risk Taxonomy: Data, Model, System, Human, and Organizational.
    """)

    # Pre-populate button logic
    if st.button("Pre-populate Initial Risks", key="prepopulate_risks_btn"):
        add_risk_to_register(dimension="Data", category="Data Quality",
                             description="Inconsistent or missing data in 'EmploymentStatus' could lead to inaccurate risk assessments, violating Validity.")
        add_risk_to_register(dimension="Data", category="Data Bias",
                             description="Historical bias in income data from specific 'ResidentialStatus' groups could lead to unfair decisions for future applicants, violating Fairness.")
        add_risk_to_register(dimension="Data", category="Data Provenance & Relevance",
                             description="CreditScore data from an older system, updated quarterly, may not reflect real-time creditworthiness, impacting model Reliability and Validity.")
        add_risk_to_register(dimension="Data", category="Data Privacy",
                             description="Potential exposure of sensitive demographic data if access controls are insufficient, violating Privacy-Preserving.")
        add_risk_to_register(dimension="Model", category="Algorithmic Bias & Fairness",
                             description="The Gradient Boosting Classifier's complex decision boundaries might amplify subtle biases present in training data, leading to disparate impact on underrepresented groups, violating Fairness.")
        add_risk_to_register(dimension="Model", category="Accuracy & Reliability",
                             description="Model performance (Precision@90%Recall: 0.60) might be insufficient for high-stakes decisions, leading to higher false negatives (approving defaulters), violating Validity and Reliability.")
        add_risk_to_register(dimension="Model", category="Model Robustness",
                             description="Model performance may degrade significantly with concept drift due to changing economic conditions (e.g., recession), leading to unstable predictions, violating Reliability.")
        add_risk_to_register(dimension="Model", category="Interpretability",
                             description="The black-box nature of Gradient Boosting makes it difficult to explain individual loan decisions to applicants or regulators, impacting Transparency and Accountability.")
        add_risk_to_register(dimension="System", category="Integration Flaws",
                             description="API integration into the legacy Loan Origination System might introduce latency or data corruption, leading to incorrect or delayed decisions, violating Validity and Safety.")
        add_risk_to_register(dimension="System", category="AI Supply Chain Vulnerabilities",
                             description="Reliance on open-source libraries (e.g., LightGBM) without thorough internal vetting could introduce security vulnerabilities or unpatched bugs, violating Security.")
        add_risk_to_register(dimension="System", category="Scalability & Performance",
                             description="The current deployment infrastructure may not handle peak load volumes for real-time predictions, leading to system outages or degraded service, violating Reliability.")
        add_risk_to_register(dimension="Human", category="Misuse & Misinterpretation",
                             description="Loan officers might misinterpret model outputs or explanations, leading to incorrect manual overrides or decisions, violating Transparency and Accountability.")
        add_risk_to_register(dimension="Human", category="Over-Reliance & Autonomy Creep",
                             description="Over-reliance on automated 'Approve' decisions could lead to a decline in human critical judgment, increasing undetected errors or biases, violating Accountability.")
        add_risk_to_register(dimension="Human", category="Loss of Human Oversight",
                             description="Lack of a clear 'human-in-the-loop' process for edge cases or flagged applications could lead to the model making autonomous, unreviewed decisions with adverse outcomes, violating Safety and Accountability.")
        add_risk_to_register(dimension="Organizational", category="Robust Governance & Oversight",
                             description="Absence of a dedicated AI Ethics Committee or clear roles for AI risk oversight beyond traditional MRM could lead to unaddressed ethical concerns, violating Accountability.")
        add_risk_to_register(dimension="Organizational", category="Policy & Ethical Guidelines",
                             description="Lack of a comprehensive incident response plan for AI model failures (e.g., severe drift, bias detection) could delay remediation and amplify negative impact, violating Safety and Accountability.")
        add_risk_to_register(dimension="Organizational", category="Responsible AI Culture",
                             description="Insufficient training or awareness programs for employees on responsible AI use and emergent risks could lead to poor operational practices, violating Accountability.")
        st.success(
            "Initial risks have been pre-populated into the AI Risk Register.")

    st.subheader("Current AI Risk Register")
    if not st.session_state.risk_register_df.empty:
        st.dataframe(st.session_state.risk_register_df.sort_values(
            by="Risk ID"), use_container_width=True)
    else:
        st.info("No risks identified yet. Use the 'Pre-populate Initial Risks' button or 'Manually Add a New Risk' section below.")

    with st.expander("Manually Add a New Risk"):
        st.markdown(
            "As a Risk Manager, you identify a unique risk based on your expert judgment.")
        new_dimension = st.selectbox("Dimension", options=[
                                     "Data", "Model", "System", "Human", "Organizational"], key="new_risk_dim")
        new_category = st.text_input(
            "Category", help="e.g., Data Quality, Algorithmic Bias", key="new_risk_cat")
        new_description = st.text_area(
            "Description", help="Detailed description of the risk, including how it might impact the model or business.", key="new_risk_desc")
        new_impact = st.selectbox("Potential Impact", options=[
                                  "Low", "Medium", "High"], index=1, key="new_risk_impact")
        new_likelihood = st.selectbox("Likelihood", options=[
                                      "Low", "Medium", "High"], index=1, key="new_risk_likelihood")
        if st.button("Add Risk", key="add_new_risk_btn"):
            if new_description:
                add_risk_to_register(
                    new_dimension, new_category, new_description, new_impact, new_likelihood)
                st.rerun()
            else:
                st.warning("Please provide a description for the new risk.")

    st.markdown("---")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Previous Step", key="page5_prev_btn", use_container_width=True):
            go_to_page(3)  # Navigate to "AI Risk Frameworks"
    with col2:
        if st.button("Next: Assess Risk Severity", key="page5_next_btn", use_container_width=True):
            # Navigate to "AI Risk Register: Assess Risk Severity"
            go_to_page(5)


import streamlit as st
from utils import assess_risk_severity, go_to_page  # Import the navigation helper


def main():
    st.header("6. AI Risk Register: Severity Assessment")
    st.markdown("""
        With all risks identified, your next step as a Risk Manager is to assess their severity. You'll use a qualitative scoring system for "Potential Impact" and "Likelihood," typically rated as Low, Medium, or High. This allows you to prioritize risks, focusing mitigation efforts on those with the highest scores. This process directly applies the fundamental risk formula (R"$Risk = Impact \times Likelihood$") and prepares for detailed discussion with stakeholders on critical risks.
    """)

    if st.button("Auto-Assess Key Risks", key="auto_assess_btn"):
        assess_risk_severity("R002", "High", "Medium")  # Historical data bias
        assess_risk_severity("R003", "Medium", "High")  # CreditScore Lag
        assess_risk_severity("R004", "Medium", "Medium")  # Data Privacy
        assess_risk_severity("R005", "High", "Medium")  # Algorithmic Bias
        # Accuracy & Reliability
        assess_risk_severity("R006", "Medium", "Low")
        # Model Robustness (concept drift)
        assess_risk_severity("R007", "High", "High")
        assess_risk_severity("R008", "Medium", "High")  # Interpretability
        assess_risk_severity("R009", "Medium", "Medium")  # Integration Flaws
        # AI Supply Chain Vulnerabilities
        assess_risk_severity("R010", "High", "Low")
        # Scalability & Performance
        assess_risk_severity("R011", "Medium", "Medium")
        # Misuse & Misinterpretation
        assess_risk_severity("R012", "Medium", "High")
        # Over-Reliance & Autonomy Creep
        assess_risk_severity("R013", "High", "Medium")
        assess_risk_severity("R014", "High", "High")  # Loss of Human Oversight
        # Absence of AI Ethics Committee
        assess_risk_severity("R015", "High", "Medium")
        # Lack of Incident Response Plan
        assess_risk_severity("R016", "High", "High")
        # Insufficient training
        assess_risk_severity("R017", "Medium", "Medium")
        st.rerun()

    st.subheader("AI Risk Register with Assessed Risks (Sorted by Score)")
    if not st.session_state.risk_register_df.empty:
        st.dataframe(st.session_state.risk_register_df.sort_values(
            by="Risk Score", ascending=False), use_container_width=True)
    else:
        st.info("No risks to assess yet. Please identify some risks first.")

    st.markdown("""
    ---
    As a Risk Manager, you can refine the impact and likelihood for any risk based on your deeper analysis.
    """)
    if not st.session_state.risk_register_df.empty:
        risk_ids = st.session_state.risk_register_df['Risk ID'].tolist()
        selected_risk_id = st.selectbox(
            "Select Risk ID to Assess/Update", options=risk_ids, key="select_risk_id_assess")

        # Pre-fill current impact/likelihood if a risk is selected
        if selected_risk_id:
            current_risk = st.session_state.risk_register_df[
                st.session_state.risk_register_df['Risk ID'] == selected_risk_id].iloc[0]
            current_impact_idx = ["Low", "Medium", "High"].index(
                current_risk['Potential Impact'])
            current_likelihood_idx = ["Low", "Medium", "High"].index(
                current_risk['Likelihood'])

            new_impact = st.selectbox("Update Potential Impact", options=[
                                      "Low", "Medium", "High"], index=current_impact_idx, key="update_impact")
            new_likelihood = st.selectbox("Update Likelihood", options=[
                                          "Low", "Medium", "High"], index=current_likelihood_idx, key="update_likelihood")
            if st.button("Update Risk Severity"):
                assess_risk_severity(
                    selected_risk_id, new_impact, new_likelihood)
                st.rerun()
    else:
        st.warning("Please add risks to the register first to enable assessment.")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Previous Step", key="page6_prev_btn", use_container_width=True):
            go_to_page(4)  # Navigate to "AI Risk Register: Identify Risks"
    with col2:
        if st.button("Next: Visualize Risk Landscape", key="page6_next_btn", use_container_width=True):
            go_to_page(6)  # Navigate to "AI Risk Matrix Visualization"

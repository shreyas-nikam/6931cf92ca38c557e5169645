
import streamlit as st
# Import the navigation helper
from utils import add_mitigation_strategy, go_to_page


def main():
    st.header("8. AI Risk Register: Strategic Mitigation")
    st.markdown("""
    Identifying and assessing risks is only half the battle. As a Risk Manager, your next critical step is to propose concrete mitigation strategies and controls for the highest-priority risks. These strategies should align with NIST AI RMF's emphasis on control measures and SR 11-7's requirement for robust validation and governance. For example, for model bias, a mitigation could involve fairness audits and re-training with debiased data. For human oversight, it might involve "human-in-the-loop" mechanisms.
    """)

    if st.button("Auto-Populate Mitigations for Top Risks", key="auto_mitigate_btn"):
        add_mitigation_strategy(
            "R007", "Implement continuous monitoring for concept drift (e.g., population stability index) with quarterly model re-calibration or re-training. Develop a champion-challenger framework.", "Model Monitoring Team")
        add_mitigation_strategy(
            "R014", "Establish clear 'human-in-the-loop' checkpoints for all high-value loan decisions and edge cases. Mandate model explanation training for loan officers.", "Operations & Compliance")
        add_mitigation_strategy(
            "R016", "Develop and socialize a comprehensive AI model incident response plan, including clear communication protocols, rollback procedures, and stakeholder notification processes.", "Risk Management & IT Operations")
        add_mitigation_strategy(
            "R002", "Conduct regular fairness audits across protected groups. Explore data augmentation or re-sampling techniques to debias training data. Implement post-processing bias mitigation techniques.", "Data Science & AI Ethics Committee")
        add_mitigation_strategy(
            "R005", "Implement disparate impact testing during model validation. Use fairness-aware training algorithms or re-weighing techniques. Document fairness metrics in model card.", "Model Validation & Data Science")
        add_mitigation_strategy(
            "R015", "Propose the formation of a cross-functional AI Ethics Committee to guide policy, review high-risk models, and provide an 'effective challenge' on ethical considerations.", "Senior Management & Governance")
        st.rerun()

    st.subheader("AI Risk Register with Proposed Mitigations (Top Risks)")
    if not st.session_state.risk_register_df.empty:
        st.dataframe(st.session_state.risk_register_df.sort_values(
            by="Risk Score", ascending=False), use_container_width=True)
    else:
        st.info(
            "No risks with mitigations yet. Please identify and assess risks first.")

    st.markdown("""
    As a Risk Manager, you can add or update mitigation strategies for individual risks.
    """)
    if not st.session_state.risk_register_df.empty:
        risk_ids = st.session_state.risk_register_df['Risk ID'].tolist()
        selected_risk_id_mitigate = st.selectbox(
            "Select Risk ID to Add/Update Mitigation", options=risk_ids, key="select_risk_id_mitigate")

        # Pre-fill current mitigation/party if a risk is selected
        if selected_risk_id_mitigate:
            current_mitigation = st.session_state.risk_register_df[
                st.session_state.risk_register_df['Risk ID'] == selected_risk_id_mitigate].iloc[0]
            current_strategy = current_mitigation['Mitigation Strategy'] if current_mitigation[
                'Mitigation Strategy'] != "To be determined" else ""
            current_party = current_mitigation['Responsible Party'] if current_mitigation['Responsible Party'] != "TBD" else ""

            new_strategy = st.text_area(
                "Mitigation Strategy Description", value=current_strategy, height=100, key="new_strategy")
            new_party = st.text_input("Responsible Party", value=current_party,
                                      help="e.g., Data Science Team, Compliance Department", key="new_party")
            if st.button("Add/Update Mitigation Strategy"):
                add_mitigation_strategy(
                    selected_risk_id_mitigate, new_strategy, new_party)
                st.rerun()
    else:
        st.warning(
            "Please add risks to the register first to enable mitigation planning.")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Previous Step", key="page8_prev_btn", use_container_width=True):
            go_to_page(6)  # Navigate to "AI Risk Matrix Visualization"
    with col2:
        if st.button("Next: Generate Final Report", key="page8_next_btn", use_container_width=True):
            go_to_page(8)  # Navigate to "Final AI Risk Report"

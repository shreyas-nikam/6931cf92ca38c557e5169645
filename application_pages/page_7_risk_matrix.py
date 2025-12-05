
import streamlit as st
from utils import plot_risk_matrix, go_to_page  # Import the navigation helper


def main():
    st.header("7. Visualizing the Risk Landscape: The AI Risk Matrix")
    st.markdown("""
    To effectively communicate the risk landscape to senior management and other stakeholders, a visual representation is essential. As a Risk Manager, you'll create a Risk Matrix, plotting each identified risk based on its assessed impact and likelihood. This visualization quickly highlights high-priority risks that fall into the "High Impact, High Likelihood" quadrant, enabling a clear and concise presentation for your upcoming 'Effective Challenge' meeting.
    """)
    if not st.session_state.risk_register_df.empty:
        plot_risk_matrix(st.session_state.risk_register_df)
        st.markdown(r"""
        The Risk Matrix visually groups risks, making it immediately clear which ones reside in the high-risk "red" zone (High Impact, High Likelihood). You can quickly point out risks like R007 ("Model Robustness"), R014 ("Loss of Human Oversight"), and R016 ("Lack of Incident Response Plan") as top priorities. This visual summary is an invaluable tool for driving discussions with non-technical stakeholders and securing resources for mitigation.
        """)
    else:
        st.info(
            "No risks in the register to plot yet. Please go back to identify and assess some risks.")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Previous Step", key="page7_prev_btn", use_container_width=True):
            # Navigate to "AI Risk Register: Assess Risk Severity"
            go_to_page(5)
    with col2:
        if st.button("Next: Develop Mitigation Strategies", key="page7_next_btn", use_container_width=True):
            # Navigate to "AI Risk Register: Mitigation Strategies"
            go_to_page(7)

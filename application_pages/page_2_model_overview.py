
import streamlit as st
from utils import go_to_page  # Import the navigation helper


def main():
    st.header("2. Understanding the Credit Risk AI Model")
    st.markdown("""As a Quantitative Analyst, before diving into risk identification, you need to thoroughly understand the AI model itself. This involves grasping its fundamental purpose, the algorithm it uses, and its intended operational environment. For the new Credit Risk Scoring Model, you've gathered initial details from the development team. This foundational understanding is the first step in applying frameworks like SR 11-7 and NIST AI RMF, ensuring you assess the right "model" in its specific context.
    """)
    st.subheader("Hypothetical AI Model Scenario Details:")
    for key, value in st.session_state.credit_risk_model_scenario.items():
        st.markdown(f"- **{key}**: {value}")

    st.markdown("""
    The output above provides a clear, concise overview of the AI model. For a Risk Manager, this information is critical for establishing the scope of the assessment and understanding the model's direct impact on business operations and potential regulatory exposure. It immediately highlights that this is a high-stakes model impacting customer finances.
    """)

    st.markdown("""---""")
    st.header("3. Constructing the AI Model Card: Transparency & Key Facts")
    st.markdown("""
    To ensure transparency and facilitate effective challenge, you need to create an 'AI Model Card' for the Credit Risk Scoring Model. This artifact, inspired by best practices in AI assurance, summarizes crucial information about the model, including its purpose, performance metrics, and known limitations. This proactive documentation is vital for internal stakeholders and external auditors, enhancing accountability and reducing information asymmetry, directly supporting SR 11-7's emphasis on validation and governance.
    """)
    st.subheader("AI Model Card: Credit Risk Scoring Model")

    # Display model card with appropriate formatting
    model_card_display = st.session_state.credit_risk_model_card.copy()
    model_card_display["Key Performance Metrics"] = {
        "AUC": f"{st.session_state.hypothetical_auc:.2f}",
        "Precision@90%Recall": f"{st.session_state.hypothetical_precision_at_recall:.2f}",
        "Target Variable": "Defaulted (Binary: 1 for default, 0 for no default)"
    }
    st.json(model_card_display)

    st.markdown(r"""
    The generated Model Card provides a structured summary. As a Risk Manager, you immediately see the model's purpose, algorithm, and crucial performance indicators (AUC: $0.85$, Precision@90%Recall: $0.60$). Importantly, the "Known Limitations" section proactively highlights areas of concern like potential bias and performance degradation, which will be central to your risk identification process. This artifact serves as a single source of truth for the model's core information.
    """)
    st.markdown("---")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Previous Step", key="page2_prev_btn", use_container_width=True):
            go_to_page(0)  # Navigate to "Welcome & Scenario Setup"
    with col2:
        if st.button("Next: Data Card", key="page2_next_btn", use_container_width=True):
            go_to_page(2)  # Navigate to "Data Overview & Card"

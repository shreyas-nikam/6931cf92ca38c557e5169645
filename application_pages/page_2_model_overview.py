
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

    # Interactive Quiz Section
    st.markdown("---")
    st.subheader("🎯 Interactive Knowledge Check: Understanding the Model Card")
    st.markdown("""
    Test your understanding of the AI Model Card by answering the following questions. Select the correct option and see explanations for each choice.
    """)

    # Initialize session state for quiz answers
    if 'model_q1_answer' not in st.session_state:
        st.session_state.model_q1_answer = None
    if 'model_q2_answer' not in st.session_state:
        st.session_state.model_q2_answer = None
    if 'model_q3_answer' not in st.session_state:
        st.session_state.model_q3_answer = None

    # Question 1
    st.markdown(
        "**Question 1:** What is the primary purpose of the Credit Risk Scoring Model?")
    q1_options = [
        "To maximize bank profits by rejecting all risky applicants",
        "To predict the likelihood of loan default for retail loan applicants",
        "To replace all human underwriters in the lending process",
        "To collect demographic data from loan applicants"
    ]
    q1_correct = 1

    st.session_state.model_q1_answer = st.radio(
        "Select your answer:",
        options=range(len(q1_options)),
        format_func=lambda x: q1_options[x],
        key="model_q1",
        index=st.session_state.model_q1_answer
    )

    if st.button("Check Answer - Question 1", key="check_q1_model"):
        if st.session_state.model_q1_answer == q1_correct:
            st.success("✅ Correct!")
            st.info("**Explanation:** The model's purpose is specifically to predict default likelihood, which helps automate approval for low-risk applicants and flag high-risk ones for manual review. This balanced approach supports decision-making rather than replacing human judgment entirely.")
        else:
            st.error("❌ Incorrect. Try again!")
            explanations = {
                0: "While risk management affects profitability, the model's purpose is prediction, not profit maximization. It's designed to assess risk objectively.",
                2: "The model is designed to assist, not replace, human underwriters. High-risk cases are flagged for manual review, maintaining human oversight.",
                3: "Data collection is a means, not the purpose. The model uses data to make predictions about default probability."
            }
            if st.session_state.model_q1_answer in explanations:
                st.info(
                    f"**Explanation:** {explanations[st.session_state.model_q1_answer]}")

    st.markdown("---")

    # Question 2
    st.markdown(
        "**Question 2:** Based on the Model Card, what AUC score did the model achieve, and what does this indicate?")
    q2_options = [
        "AUC = 0.60, indicating poor discrimination ability",
        "AUC = 0.85, indicating good discrimination ability between defaulters and non-defaulters",
        "AUC = 1.00, indicating perfect prediction accuracy",
        "AUC = 0.50, indicating random guessing"
    ]
    q2_correct = 1

    st.session_state.model_q2_answer = st.radio(
        "Select your answer:",
        options=range(len(q2_options)),
        format_func=lambda x: q2_options[x],
        key="model_q2",
        index=st.session_state.model_q2_answer
    )

    if st.button("Check Answer - Question 2", key="check_q2_model"):
        if st.session_state.model_q2_answer == q2_correct:
            st.success("✅ Correct!")
            st.info("**Explanation:** An AUC (Area Under the ROC Curve) of 0.85 is considered good. It means the model correctly distinguishes between defaulters and non-defaulters 85% of the time. AUC ranges from 0.5 (random) to 1.0 (perfect), so 0.85 shows strong predictive capability while acknowledging room for improvement.")
        else:
            st.error("❌ Incorrect. Try again!")
            explanations = {
                0: "0.60 is the Precision@90%Recall metric, not the AUC. AUC is 0.85, which indicates good performance.",
                2: "AUC = 1.00 would be perfect, but this is rarely achieved in real-world scenarios and might indicate overfitting. The model achieved 0.85, which is realistically good.",
                3: "AUC = 0.50 would be random guessing (like flipping a coin). The model performs much better at 0.85."
            }
            if st.session_state.model_q2_answer in explanations:
                st.info(
                    f"**Explanation:** {explanations[st.session_state.model_q2_answer]}")

    st.markdown("---")

    # Question 3
    st.markdown(
        "**Question 3:** Which known limitation is MOST critical from a regulatory compliance perspective (SR 11-7)?")
    q3_options = [
        "Limited interpretability (black-box nature)",
        "Potential for disparate impact on demographic groups due to historical data biases",
        "Performance degradation with economic shifts",
        "Model was developed internally"
    ]
    q3_correct = 1

    st.session_state.model_q3_answer = st.radio(
        "Select your answer:",
        options=range(len(q3_options)),
        format_func=lambda x: q3_options[x],
        key="model_q3",
        index=st.session_state.model_q3_answer
    )

    if st.button("Check Answer - Question 3", key="check_q3_model"):
        if st.session_state.model_q3_answer == q3_correct:
            st.success("✅ Correct!")
            st.info("**Explanation:** Disparate impact (discriminatory outcomes affecting protected demographic groups) is a critical regulatory concern under fair lending laws like the Equal Credit Opportunity Act (ECOA) and SR 11-7. This type of bias can lead to legal consequences, regulatory fines, and reputational damage. While all limitations are important, fairness and non-discrimination are paramount in financial services.")
        else:
            st.error("❌ Incorrect. Try again!")
            explanations = {
                0: "While interpretability is important for SR 11-7's model validation requirements, fairness and non-discrimination are more critical regulatory concerns that can result in severe legal consequences.",
                2: "Model robustness is important, but discriminatory outcomes pose more immediate regulatory and legal risks than performance degradation.",
                3: "Internal development is not a limitation; SR 11-7 applies regardless of whether models are developed internally or by third parties."
            }
            if st.session_state.model_q3_answer in explanations:
                st.info(
                    f"**Explanation:** {explanations[st.session_state.model_q3_answer]}")

    st.markdown("---")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Previous Step", key="page2_prev_btn", use_container_width=True):
            go_to_page(0)  # Navigate to "Welcome & Scenario Setup"
    with col2:
        if st.button("Next: Data Card", key="page2_next_btn", use_container_width=True):
            go_to_page(2)  # Navigate to "Data Overview & Card"

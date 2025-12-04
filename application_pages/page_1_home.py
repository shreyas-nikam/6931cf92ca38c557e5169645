
import streamlit as st
import pandas as pd
from utils import generate_synthetic_risk_data, calculate_risk_priority_score

def main():
    st.title("AI Model Risk Register & Mitigation Planner")
    st.markdown("""
    This lab provides a practical guide for identifying, assessing, and managing risks associated with Artificial Intelligence (AI) models. It's designed for risk managers, data engineers, and compliance officers who need to ensure the responsible deployment and continuous assurance of AI systems in regulated environments, such as financial institutions.

    We will explore key concepts from foundational frameworks like SR 11-7 and the NIST AI Risk Management Framework (AI RMF), apply a structured AI risk taxonomy, and develop a simulated AI Risk Register to track and mitigate potential hazards.
    """)

    st.header("Learning Objectives")
    st.markdown("""
    Upon completing this lab, you will be able to:
    *   Implement an AI Risk Taxonomy to categorize risks into Data, Model, System, Human, and Organizational dimensions.
    *   Facilitate the conceptual assessment of risk likelihood and impact to derive a priority score.
    *   Demonstrate the mapping of mitigation strategies to NIST AI RMF functions and SR 11-7 pillars.
    *   Allow for tracking the status of mitigation efforts over time.
    *   Understand the role of AI assurance artifacts like Model Cards, Data Cards, and comprehensive Risk Reports.
    """)

    st.header("Target Audience")
    st.markdown("""
    This lab is tailored for:
    *   **Risk Managers**: Responsible for overseeing and mitigating AI-related risks.
    *   **Financial Data Engineers**: Involved in the development, deployment, and monitoring of AI models in regulated financial contexts.
    *   **AI Ethicists and Compliance Officers**: Focused on ensuring ethical AI practices and regulatory adherence.
    *   **Model Validators**: Tasked with critically reviewing and testing AI models.
    """)

    st.header("AI Risk Management: Context and Foundational Frameworks")
    st.markdown("""
    The increasing adoption of AI, particularly in high-stakes domains like finance, necessitates robust risk management practices. Traditional model risk management frameworks, such as SR 11-7, provide a strong foundation but must be extended to address the unique complexities and emergent risks introduced by AI systems (e.g., hallucinations in LLMs, autonomy creep in agentic systems).

    The **NIST AI Risk Management Framework (AI RMF 1.0)** offers a complementary and voluntary U.S. framework for managing AI risks across all sectors, emphasizing trustworthiness attributes like validity, reliability, safety, security, transparency, fairness, accountability, and privacy-preservation.

    Key principles we will explore include:
    *   **SR 11-7 (2011)**: Foundational U.S. guidance for model risk management in financial institutions, defining model risk as the potential for adverse outcomes from incorrect or misused models. It emphasizes effective challenge and robust governance.
    *   **NIST AI RMF 1.0 (2023)**: A framework to promote trustworthy AI by improving the ability to incorporate trustworthiness considerations into AI product design, development, use, and evaluation. It outlines four core functions: **Govern, Map, Measure, Manage**.

    These frameworks collectively provide a structured approach to identifying, assessing, mitigating, and monitoring AI-specific risks, ensuring both regulatory compliance and responsible AI deployment.
    """)

    st.header("AI Risk Taxonomy: A Multidimensional Approach")
    st.markdown("""
    A systematic classification of AI risks is crucial for comprehensive risk management. Risks are categorized across five critical dimensions, ensuring a holistic view across the entire AI lifecycle.

    1.  **Data Risks**: Pertain to the quality, provenance, relevance, and privacy of data used in AI systems.
        *   *Examples*: Data drift, poor data quality, biased training data, data privacy breaches, lack of data provenance.
    2.  **Model Risks**: Associated with the AI model itself, including its design, performance, and interpretability.
        *   *Examples*: Algorithmic bias, low accuracy/reliability, lack of robustness, model drift, interpretability challenges, hallucinations (LLMs).
    3.  **System Risks**: Relate to the integration, architecture, and security of the AI system within broader IT infrastructure.
        *   *Examples*: Integration flaws, architectural vulnerabilities, AI supply chain risks, API security issues, scalability problems, error propagation.
    4.  **Human Risks**: Involve human interaction with AI, including misuse, over-reliance, and challenges in oversight.
        *   *Examples*: Misinterpretation of AI outputs, over-reliance on AI, autonomy creep, loss of human oversight, inadequate human-in-the-loop mechanisms.
    5.  **Organizational Risks**: Encompass governance, policy, and cultural factors within the organization that impact AI risk management.
        *   *Examples*: Lack of clear AI governance, insufficient ethical guidelines, absence of a responsible AI culture, inadequate resources for AI risk management.

    Understanding these dimensions allows for targeted identification and mitigation of risks throughout the AI system's lifecycle, from development to ongoing monitoring.
    """)

    st.header("Generating a Synthetic AI Risk Register")
    st.markdown("""
    As a risk manager, you often start by populating a risk register based on initial assessments or available data. To simulate a real-world scenario and kickstart our risk management process, you can generate a synthetic dataset representing an AI Model Risk Register. This data will allow us to demonstrate the principles of AI risk management without needing actual sensitive data.
    """)

    num_risks_input = st.number_input("Number of synthetic risks to generate:", min_value=1, value=30, key="num_risks_input")
    if st.button("Generate Synthetic Data", key="generate_synthetic_data_button"):
        st.session_state.ai_risk_register_df = generate_synthetic_risk_data(num_risks_input)
        st.session_state.ai_risk_register_df["Risk_Priority_Score"] = calculate_risk_priority_score(st.session_state.ai_risk_register_df)
        st.success(f"{num_risks_input} synthetic risks generated and added to the register.")

    st.header("Initial Data Exploration")
    st.markdown("""
    Before diving into risk scoring and detailed analysis, it's crucial to perform an initial exploration of your AI Risk Register. This step helps you, as a risk manager, to quickly understand the structure, data types, and get a preliminary overview of the content. This step ensures that the data is as expected and ready for further assessment.
    """)
    if 'ai_risk_register_df' in st.session_state and not st.session_state.ai_risk_register_df.empty:
        st.dataframe(st.session_state.ai_risk_register_df)
        st.markdown(f"**Current number of risks in register:** {len(st.session_state.ai_risk_register_df)}")
    else:
        st.info("No AI Risk Register data available yet. Please generate synthetic data above.")

    st.header("Calculating Risk Priority Score")
    st.markdown(r"""
    To effectively prioritize risks, you need a quantifiable measure of their severity. As a risk manager, you will calculate a `Risk_Priority_Score` based on the assessed `Likelihood` and `Impact` of each risk. This score helps you focus your attention and resources on the most critical issues.

    We use a simple multiplicative matrix approach, mapping `Low`, `Medium`, `High` to numerical values (1, 2, 3 respectively) for both Likelihood and Impact. The Priority Score ($S$) is then calculated as the product of these numerical values:
    $$
    S = \text{Likelihood}_{\text{numeric}} \times \text{Impact}_{\text{numeric}}
    $$
    The resulting score will range from 1 (Low Likelihood x Low Impact) to 9 (High Likelihood x High Impact).

    The scoring matrix is as follows:
    $$
    \begin{pmatrix}
    \textbf{Likelihood} / \textbf{Impact} & \textbf{Low (1)} & \textbf{Medium (2)} & \textbf{High (3)} \\
    \textbf{Low (1)} & 1 & 2 & 3 \\
    \textbf{Medium (2)} & 2 & 4 & 6 \\
    \textbf{High (3)} & 3 & 6 & 9
    \end{pmatrix}
    $$
    This matrix allows for a quick visual and numerical assessment of risk severity.
    """)
    if 'ai_risk_register_df' in st.session_state and not st.session_state.ai_risk_register_df.empty:
        st.markdown("Your AI Risk Register now includes the calculated `Risk_Priority_Score` for each entry:")
        st.dataframe(st.session_state.ai_risk_register_df[['Risk_ID', 'Risk_Description', 'Likelihood', 'Impact', 'Risk_Priority_Score']])
    else:
        st.info("Generate synthetic data to see the Risk Priority Scores.")



import streamlit as st
from utils import go_to_page  # Import the navigation helper


def main():
    st.header("4. Foundations: SR 11-7 & NIST AI RMF 1.0")
    st.markdown("""
    ## Foundations of Financial Model Risk: SR 11-7 in an AI Context

    As a Quantitative Analyst in a financial institution, SR 11-7 (Supervisory Guidance on Model Risk Management) is your bedrock for model governance. While it predates modern AI, its core principles of Model Risk Management (MRM) remain highly relevant. You must consider how SR 11-7's pillars—model development, implementation, validation, and governance—translate to AI systems. This conceptual mapping ensures that even novel AI models are subject to the same rigor and oversight as traditional financial models, especially concerning "effective challenge" and sound governance.

    The definition of model risk under SR 11-7 is broad and encompasses the potential for adverse consequences from decisions based on incorrect or misused model outputs. This includes financial loss, reputational damage, and flawed decisions. The guidance emphasizes that model risk intensifies with greater model complexity, higher input uncertainty, broader extent of use, and larger potential impact. These considerations are particularly amplified with AI models due to their opacity and emergent behaviors.
    """)
    st.info("As a Quant Analyst, SR 11-7 is your bedrock for model governance. Remember: model risk intensifies with complexity, input uncertainty, and broader use.")

    st.markdown("""
    ## Embracing Trustworthy AI: The NIST AI RMF 1.0 Framework

    Beyond SR 11-7's financial focus, the NIST AI Risk Management Framework (AI RMF 1.0) provides a broader, cross-sector lens for managing AI risks and promoting trustworthy AI. As an AI Risk Manager, you recognize the need to integrate these principles, which encompass attributes like validity, reliability, safety, security, transparency, fairness, accountability, and privacy-preserving. This framework complements SR 11-7 by offering a structured approach to identifying, measuring, and managing the unique risks posed by AI systems across their entire lifecycle. You will leverage its taxonomy and attributes to ensure a comprehensive risk assessment.
    """)
    st.markdown(r"""
    The NIST AI RMF categorizes trustworthiness attributes as follows:
    -   **Validity**: Ensuring the AI system accurately performs its intended function and produces correct outputs for its specified purpose.
    -   **Reliability**: Guarantees consistent and stable performance of the AI system over time and across various operational conditions.
    -   **Safety**: Minimizing the potential for the AI system to cause harm to individuals, society, or the environment.
    -   **Security**: Protecting AI systems from adversarial attacks and ensuring data integrity.
    -   **Transparency**: Understanding how AI systems arrive at outputs, often through interpretability methods.
    -   **Fairness**: Identifying and mitigating biases encoded and amplified by AI to ensure equitable outcomes.
    -   **Accountability**: Establishing clear roles and policies for AI risk oversight to ensure responsibility for AI outcomes and decisions.
    -   **Privacy-Preserving**: Implementing strategies to address data sensitivity and integrating privacy by design.
    """)
    st.info("NIST AI RMF broadens the view beyond financial models, focusing on trustworthy AI attributes like Fairness, Transparency, and Accountability, which are crucial for any AI deployment.")

    # Interactive Quiz Section
    st.markdown("---")
    st.subheader("🎯 Interactive Knowledge Check: Understanding AI Risk Frameworks")
    st.markdown("""
    Test your understanding of SR 11-7 and NIST AI RMF frameworks. Select the correct option and see explanations for each choice.
    """)
    
    # Initialize session state for quiz answers
    if 'framework_q1_answer' not in st.session_state:
        st.session_state.framework_q1_answer = None
    if 'framework_q2_answer' not in st.session_state:
        st.session_state.framework_q2_answer = None
    if 'framework_q3_answer' not in st.session_state:
        st.session_state.framework_q3_answer = None
    if 'framework_q4_answer' not in st.session_state:
        st.session_state.framework_q4_answer = None
    if 'framework_q5_answer' not in st.session_state:
        st.session_state.framework_q5_answer = None
    
    # Question 1 - SR 11-7 Core Principles
    st.markdown("**Question 1:** According to SR 11-7, which factors intensify model risk?")
    q1_options = [
        "Only the model's complexity",
        "Complexity, input uncertainty, extent of use, and potential impact",
        "The number of developers who worked on the model",
        "Whether the model uses open-source libraries"
    ]
    q1_correct = 1
    
    st.session_state.framework_q1_answer = st.radio(
        "Select your answer:",
        options=range(len(q1_options)),
        format_func=lambda x: q1_options[x],
        key="framework_q1",
        index=st.session_state.framework_q1_answer
    )
    
    if st.button("Check Answer - Question 1", key="check_q1_framework"):
        if st.session_state.framework_q1_answer == q1_correct:
            st.success("✅ Correct!")
            st.info("**Explanation:** SR 11-7 explicitly identifies four key factors that intensify model risk: (1) **Greater model complexity** makes validation harder, (2) **Higher input uncertainty** reduces reliability, (3) **Broader extent of use** increases exposure, and (4) **Larger potential impact** magnifies consequences. For our Credit Risk Scoring Model, all four factors apply—it's a complex gradient boosting model, uses potentially uncertain data, will be widely deployed, and directly impacts customer finances and regulatory compliance.")
        else:
            st.error("❌ Incorrect. Try again!")
            explanations = {
                0: "Complexity alone isn't sufficient. SR 11-7 considers multiple dimensions including how uncertain inputs are, how broadly the model is used, and what impact it has.",
                2: "Team size is not a risk factor identified by SR 11-7. The focus is on inherent model characteristics and deployment context.",
                3: "Open-source vs. proprietary is not a risk factor in SR 11-7. The focus is on complexity, uncertainty, usage extent, and potential impact."
            }
            if st.session_state.framework_q1_answer in explanations:
                st.info(f"**Explanation:** {explanations[st.session_state.framework_q1_answer]}")
    
    st.markdown("---")
    
    # Question 2 - SR 11-7 Pillars
    st.markdown("**Question 2:** What are the core pillars of Model Risk Management under SR 11-7?")
    q2_options = [
        "Development, Testing, Deployment, Retirement",
        "Model Development, Implementation, Validation, and Governance",
        "Planning, Building, Monitoring, Reporting",
        "Design, Code, Test, Release"
    ]
    q2_correct = 1
    
    st.session_state.framework_q2_answer = st.radio(
        "Select your answer:",
        options=range(len(q2_options)),
        format_func=lambda x: q2_options[x],
        key="framework_q2",
        index=st.session_state.framework_q2_answer
    )
    
    if st.button("Check Answer - Question 2", key="check_q2_framework"):
        if st.session_state.framework_q2_answer == q2_correct:
            st.success("✅ Correct!")
            st.info("**Explanation:** SR 11-7 establishes four fundamental pillars: (1) **Model Development**—rigorous design and testing, (2) **Implementation**—proper integration into business processes, (3) **Validation**—independent review and effective challenge, (4) **Governance**—oversight, policies, and accountability. These pillars ensure comprehensive risk management throughout the model lifecycle. For AI models like our Credit Risk Scoring Model, each pillar must be adapted to address unique challenges like opacity, bias, and emergent behaviors.")
        else:
            st.error("❌ Incorrect. Try again!")
            explanations = {
                0: "While these are general project phases, SR 11-7 specifically emphasizes Development, Implementation, Validation, and Governance as the formal pillars.",
                2: "These are generic project management phases. SR 11-7's pillars specifically address model risk with emphasis on validation and governance.",
                3: "This describes a software development lifecycle, not SR 11-7's model risk management framework which emphasizes validation and governance."
            }
            if st.session_state.framework_q2_answer in explanations:
                st.info(f"**Explanation:** {explanations[st.session_state.framework_q2_answer]}")
    
    st.markdown("---")
    
    # Question 3 - SR 11-7 Model Risk Definition
    st.markdown("**Question 3:** How does SR 11-7 define model risk?")
    q3_options = [
        "Only the risk of financial losses from model errors",
        "The risk that models will become outdated over time",
        "Potential for adverse consequences from decisions based on incorrect or misused model outputs",
        "The probability that a model's code contains bugs"
    ]
    q3_correct = 2
    
    st.session_state.framework_q3_answer = st.radio(
        "Select your answer:",
        options=range(len(q3_options)),
        format_func=lambda x: q3_options[x],
        key="framework_q3",
        index=st.session_state.framework_q3_answer
    )
    
    if st.button("Check Answer - Question 3", key="check_q3_framework"):
        if st.session_state.framework_q3_answer == q3_correct:
            st.success("✅ Correct!")
            st.info("**Explanation:** SR 11-7 defines model risk broadly as the potential for adverse consequences from decisions based on **incorrect** (model errors, poor performance) or **misused** (inappropriate application) model outputs. This encompasses financial loss, poor business decisions, reputational damage, and regulatory violations. For the Credit Risk Scoring Model, this means risks from both technical failures (bias, poor accuracy) and operational misuse (applying it outside its validated scope).")
        else:
            st.error("❌ Incorrect. Try again!")
            explanations = {
                0: "Model risk is broader than just financial losses. It includes reputational damage, flawed business decisions, and regulatory consequences.",
                1: "Model obsolescence is one aspect, but SR 11-7's definition is broader, focusing on adverse consequences from incorrect or misused outputs.",
                3: "Technical bugs are part of model risk, but the definition encompasses broader adverse consequences including misuse, not just coding errors."
            }
            if st.session_state.framework_q3_answer in explanations:
                st.info(f"**Explanation:** {explanations[st.session_state.framework_q3_answer]}")
    
    st.markdown("---")
    
    # Question 4 - NIST AI RMF Trustworthiness Attributes
    st.markdown("**Question 4:** Which NIST AI RMF attribute focuses on identifying and mitigating biases to ensure equitable outcomes?")
    q4_options = [
        "Validity",
        "Transparency",
        "Fairness",
        "Accountability"
    ]
    q4_correct = 2
    
    st.session_state.framework_q4_answer = st.radio(
        "Select your answer:",
        options=range(len(q4_options)),
        format_func=lambda x: q4_options[x],
        key="framework_q4",
        index=st.session_state.framework_q4_answer
    )
    
    if st.button("Check Answer - Question 4", key="check_q4_framework"):
        if st.session_state.framework_q4_answer == q4_correct:
            st.success("✅ Correct!")
            st.info("**Explanation:** **Fairness** is the NIST AI RMF attribute specifically dedicated to identifying and mitigating biases encoded and amplified by AI systems to ensure equitable outcomes across different groups. For the Credit Risk Scoring Model, this means examining whether the model treats different demographic groups fairly, particularly given the identified historical lending biases in the training data. This directly addresses concerns like disparate impact on renters or underrepresented age groups.")
        else:
            st.error("❌ Incorrect. Try again!")
            explanations = {
                0: "Validity focuses on whether the AI performs its intended function accurately, not on equitable treatment across groups.",
                1: "Transparency is about understanding how AI systems arrive at outputs (interpretability), not specifically about bias mitigation and equitable outcomes.",
                3: "Accountability establishes clear roles and oversight for AI decisions, but Fairness specifically addresses bias mitigation and equitable outcomes."
            }
            if st.session_state.framework_q4_answer in explanations:
                st.info(f"**Explanation:** {explanations[st.session_state.framework_q4_answer]}")
    
    st.markdown("---")
    
    # Question 5 - NIST AI RMF Comprehensive Application
    st.markdown("**Question 5:** For the Credit Risk Scoring Model's 'black-box nature' limitation, which NIST AI RMF attribute is MOST directly relevant?")
    q5_options = [
        "Security - protecting the model from attacks",
        "Transparency - understanding how the model arrives at outputs",
        "Privacy-Preserving - protecting applicant data",
        "Reliability - ensuring consistent performance"
    ]
    q5_correct = 1
    
    st.session_state.framework_q5_answer = st.radio(
        "Select your answer:",
        options=range(len(q5_options)),
        format_func=lambda x: q5_options[x],
        key="framework_q5",
        index=st.session_state.framework_q5_answer
    )
    
    if st.button("Check Answer - Question 5", key="check_q5_framework"):
        if st.session_state.framework_q5_answer == q5_correct:
            st.success("✅ Correct!")
            st.info("**Explanation:** **Transparency** directly addresses the black-box nature of complex models like Gradient Boosting Classifiers. It involves understanding how AI systems arrive at their outputs through interpretability methods (e.g., SHAP values, feature importance, partial dependence plots). For SR 11-7's 'effective challenge' requirement and regulatory compliance, stakeholders need to understand why the model makes certain predictions. Limited interpretability hinders validation, debugging, and explaining decisions to applicants or regulators.")
        else:
            st.error("❌ Incorrect. Try again!")
            explanations = {
                0: "Security is about protecting against adversarial attacks and ensuring data integrity, not about understanding internal model logic.",
                2: "Privacy-Preserving addresses data sensitivity and privacy-by-design, not the interpretability of model predictions.",
                3: "Reliability ensures consistent performance over time, but doesn't address the ability to understand and explain individual predictions."
            }
            if st.session_state.framework_q5_answer in explanations:
                st.info(f"**Explanation:** {explanations[st.session_state.framework_q5_answer]}")
    
    st.markdown("---")
    
    # Bonus Scenario-Based Question
    st.markdown("**Bonus Question:** You discover the Credit Risk Scoring Model performs well overall (AUC=0.85) but has significantly lower precision for applicants under 25. Which framework attribute combination should you prioritize?")
    q6_options = [
        "Security and Privacy only",
        "Fairness (equitable outcomes) and Validity (accurate performance for all groups)",
        "Accountability and Governance only",
        "Reliability and Safety only"
    ]
    q6_correct = 1
    
    if 'framework_q6_answer' not in st.session_state:
        st.session_state.framework_q6_answer = None
    
    st.session_state.framework_q6_answer = st.radio(
        "Select your answer:",
        options=range(len(q6_options)),
        format_func=lambda x: q6_options[x],
        key="framework_q6",
        index=st.session_state.framework_q6_answer
    )
    
    if st.button("Check Answer - Bonus Question", key="check_q6_framework"):
        if st.session_state.framework_q6_answer == q6_correct:
            st.success("✅ Correct!")
            st.info("**Explanation:** This scenario requires addressing both **Fairness** and **Validity**. The performance disparity for under-25 applicants represents: (1) A **fairness issue**—differential performance across age groups may lead to discriminatory outcomes and potential age discrimination concerns, (2) A **validity issue**—the model isn't accurately performing its intended function for all population segments. From SR 11-7's perspective, this is a model limitation requiring mitigation (e.g., separate model for this segment, rebalanced training data, age-specific monitoring). The underrepresentation identified in the Data Card explains this performance gap.")
        else:
            st.error("❌ Incorrect. Try again!")
            explanations = {
                0: "While important, security and privacy don't address the core issue of differential model performance across age groups.",
                2: "Accountability and governance are important for oversight, but don't directly address the technical performance disparity that needs fixing.",
                3: "Reliability is about consistency over time. This is about accuracy differences across groups (validity) and equitable treatment (fairness)."
            }
            if st.session_state.framework_q6_answer in explanations:
                st.info(f"**Explanation:** {explanations[st.session_state.framework_q6_answer]}")

    st.markdown("---")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Previous Step", key="page4_prev_btn", use_container_width=True):
            go_to_page(2)  # Navigate to "Data Overview & Card"
    with col2:
        if st.button("Next: Identify AI Risks", key="page4_next_btn", use_container_width=True):
            go_to_page(4)  # Navigate to "AI Risk Register: Identify Risks"

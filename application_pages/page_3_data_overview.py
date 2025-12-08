
import streamlit as st
from utils import go_to_page  # Import the navigation helper


def main():
    st.header("3. Dissecting the Data for the Credit Risk Model")
    st.markdown("""
    The quality and characteristics of the training data are paramount to an AI model's performance and fairness. As a Quantitative Analyst, you understand that "garbage in, garbage out" applies rigorously to AI. You need to document the synthetic dataset used to train the Credit Risk Scoring Model. This 'Data Card' will detail its provenance, features, and crucially, any identified biases or quality issues. This directly addresses the "Data" dimension of AI risk, as highlighted by NIST AI RMF and SR 11-7's emphasis on data quality in model validation.
    """)
    st.subheader("Data Card: Credit Application Data")

    # Display data card with appropriate formatting
    st.json(st.session_state.credit_data_card)

    st.markdown("""
    The Data Card clearly outlines the dataset's characteristics and, critically, highlights potential biases and data quality issues. As a Risk Manager, you note the "Historical lending bias" and "Underrepresentation" as immediate red flags for fairness, while "Missing Data" and "CreditScore Lag" point to accuracy and reliability concerns. This information directly informs the data-related risks you'll formally document in the risk register.
    """)
    
    # Interactive Quiz Section
    st.markdown("---")
    st.subheader("🎯 Interactive Knowledge Check: Understanding the Data Card")
    st.markdown("""
    Test your understanding of the Data Card and its implications for AI risk assessment. Select the correct option and see explanations for each choice.
    """)
    
    # Initialize session state for quiz answers
    if 'data_q1_answer' not in st.session_state:
        st.session_state.data_q1_answer = None
    if 'data_q2_answer' not in st.session_state:
        st.session_state.data_q2_answer = None
    if 'data_q3_answer' not in st.session_state:
        st.session_state.data_q3_answer = None
    
    # Question 1
    st.markdown("**Question 1:** Which data quality issue poses the GREATEST risk for real-time lending decisions?")
    q1_options = [
        "Missing 5% of EmploymentStatus values",
        "CreditScore data updated quarterly (lags real-time creditworthiness)",
        "Categorical features are one-hot encoded",
        "Dataset has 10,000 rows"
    ]
    q1_correct = 1
    
    st.session_state.data_q1_answer = st.radio(
        "Select your answer:",
        options=range(len(q1_options)),
        format_func=lambda x: q1_options[x],
        key="data_q1",
        index=st.session_state.data_q1_answer
    )
    
    if st.button("Check Answer - Question 1", key="check_q1_data"):
        if st.session_state.data_q1_answer == q1_correct:
            st.success("✅ Correct!")
            st.info("**Explanation:** Credit scores that lag by up to three months may not reflect recent financial changes (e.g., new debt, missed payments, or improved payment history). In real-time lending decisions, this could lead to approving applicants whose creditworthiness has deteriorated or rejecting those who have improved, directly impacting prediction accuracy and fairness.")
        else:
            st.error("❌ Incorrect. Try again!")
            explanations = {
                0: "While 5% missing values is notable, it's been addressed through imputation with mode. The CreditScore lag affects all predictions and cannot be easily fixed through preprocessing.",
                2: "One-hot encoding is a standard preprocessing technique, not a risk. It's how the model properly handles categorical variables.",
                3: "Dataset size of 10,000 is reasonable for this use case and not inherently risky. The lag in credit scores is a more pressing concern."
            }
            if st.session_state.data_q1_answer in explanations:
                st.info(f"**Explanation:** {explanations[st.session_state.data_q1_answer]}")
    
    st.markdown("---")
    
    # Question 2
    st.markdown("**Question 2:** The Data Card identifies 'Historical lending bias' showing lower approval rates for 'Renter' status in specific income brackets. What type of AI risk does this primarily represent?")
    q2_options = [
        "Technical/Performance Risk only",
        "Fairness and Bias Risk, potentially leading to discriminatory outcomes",
        "Cybersecurity Risk",
        "Data Privacy Risk"
    ]
    q2_correct = 1
    
    st.session_state.data_q2_answer = st.radio(
        "Select your answer:",
        options=range(len(q2_options)),
        format_func=lambda x: q2_options[x],
        key="data_q2",
        index=st.session_state.data_q2_answer
    )
    
    if st.button("Check Answer - Question 2", key="check_q2_data"):
        if st.session_state.data_q2_answer == q2_correct:
            st.success("✅ Correct!")
            st.info("**Explanation:** Historical lending bias in training data can perpetuate discriminatory patterns. If renters were historically denied loans not due to creditworthiness but due to bias, the model learns this pattern and may continue to unfairly disadvantage renters. This is a classic fairness and bias risk, especially concerning since housing status can correlate with protected characteristics. From NIST AI RMF and SR 11-7 perspectives, this requires immediate attention and mitigation.")
        else:
            st.error("❌ Incorrect. Try again!")
            explanations = {
                0: "While it may affect performance, the primary concern is fairness. The model may perform well statistically while still producing discriminatory outcomes for certain groups.",
                2: "Cybersecurity risks involve unauthorized access, data breaches, or malicious attacks. This is about biased historical data, not security vulnerabilities.",
                3: "Data privacy relates to protecting personal information. While important, the bias issue is about fairness in decision-making, not privacy protection."
            }
            if st.session_state.data_q2_answer in explanations:
                st.info(f"**Explanation:** {explanations[st.session_state.data_q2_answer]}")
    
    st.markdown("---")
    
    # Question 3
    st.markdown("**Question 3:** Why are 'Age', 'Income', and 'ResidentialStatus' identified as 'Sensitive Features'?")
    q3_options = [
        "They are encrypted in the database",
        "They may correlate with protected demographic characteristics and require fairness monitoring",
        "They are the most important features for prediction",
        "They contain personally identifiable information (PII)"
    ]
    q3_correct = 1
    
    st.session_state.data_q3_answer = st.radio(
        "Select your answer:",
        options=range(len(q3_options)),
        format_func=lambda x: q3_options[x],
        key="data_q3",
        index=st.session_state.data_q3_answer
    )
    
    if st.button("Check Answer - Question 3", key="check_q3_data"):
        if st.session_state.data_q3_answer == q3_correct:
            st.success("✅ Correct!")
            st.info("**Explanation:** These features are 'sensitive' because they can serve as proxies for protected characteristics (e.g., Age can proxy for age discrimination, ResidentialStatus might correlate with race or socioeconomic status). Even if protected attributes like race or gender aren't directly used, the model could still produce disparate impacts through these correlated features. Under SR 11-7 and fair lending regulations, these features require special monitoring to ensure they don't lead to discriminatory outcomes.")
        else:
            st.error("❌ Incorrect. Try again!")
            explanations = {
                0: "Encryption is a security control, not what makes features 'sensitive' in the AI risk context. The term refers to potential for bias and discrimination.",
                2: "Feature importance is about predictive power, not sensitivity. A feature can be highly predictive but not sensitive, or sensitive but not the most important predictor.",
                3: "While these may be PII, 'sensitive features' in AI risk assessment specifically refers to features that could lead to unfair or discriminatory outcomes, not just data privacy concerns."
            }
            if st.session_state.data_q3_answer in explanations:
                st.info(f"**Explanation:** {explanations[st.session_state.data_q3_answer]}")
    
    st.markdown("---")
    
    # Bonus Question
    st.markdown("**Bonus Question:** What is the significance of documenting 'Underrepresentation' of applicants under 25 or over 65?")
    q4_options = [
        "It's just a statistical observation with no practical implications",
        "The model may perform poorly or unfairly for these age groups due to insufficient training examples",
        "These age groups should be excluded from using the model",
        "It means the bank doesn't want these customers"
    ]
    q4_correct = 1
    
    if 'data_q4_answer' not in st.session_state:
        st.session_state.data_q4_answer = None
    
    st.session_state.data_q4_answer = st.radio(
        "Select your answer:",
        options=range(len(q4_options)),
        format_func=lambda x: q4_options[x],
        key="data_q4",
        index=st.session_state.data_q4_answer
    )
    
    if st.button("Check Answer - Bonus Question", key="check_q4_data"):
        if st.session_state.data_q4_answer == q4_correct:
            st.success("✅ Correct!")
            st.info("**Explanation:** Underrepresentation means the model has fewer examples to learn from for these age groups, potentially leading to: (1) Higher prediction errors for these groups, (2) Unfair treatment due to the model's uncertainty, (3) Compliance risks under age discrimination laws. This is a data quality and fairness concern requiring mitigation strategies such as collecting more data, using stratified sampling, or implementing age-specific model monitoring. The model's applicability to these segments must be carefully evaluated per SR 11-7.")
        else:
            st.error("❌ Incorrect. Try again!")
            explanations = {
                0: "Underrepresentation has serious practical implications for model performance and fairness. It's a key risk factor that must be addressed.",
                2: "Exclusion would be discriminatory and illegal under age discrimination laws. Instead, the model needs mitigation strategies to handle these groups fairly despite limited training data.",
                3: "This is about data collection and historical patterns, not business preference. The concern is ensuring fair treatment despite limited training data."
            }
            if st.session_state.data_q4_answer in explanations:
                st.info(f"**Explanation:** {explanations[st.session_state.data_q4_answer]}")
    
    st.markdown("---")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Previous Step", key="page3_prev_btn", use_container_width=True):
            go_to_page(1)  # Navigate to "Model Overview & Card"
    with col2:
        if st.button("Next: AI Risk Frameworks", key="page3_next_btn", use_container_width=True):
            go_to_page(3)  # Navigate to "AI Risk Frameworks"

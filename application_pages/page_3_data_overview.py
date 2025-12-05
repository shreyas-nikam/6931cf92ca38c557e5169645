
import streamlit as st
from utils import go_to_page # Import the navigation helper

def main():
    st.header("3. Dissecting the Data for the Credit Risk Model")
    st.markdown("---
    The quality and characteristics of the training data are paramount to an AI model's performance and fairness. As a Quantitative Analyst, you understand that "garbage in, garbage out" applies rigorously to AI. You need to document the synthetic dataset used to train the Credit Risk Scoring Model. This 'Data Card' will detail its provenance, features, and crucially, any identified biases or quality issues. This directly addresses the "Data" dimension of AI risk, as highlighted by NIST AI RMF and SR 11-7's emphasis on data quality in model validation.
    ")
    st.subheader("Data Card: Credit Application Data")
    
    # Display data card with appropriate formatting
    st.json(st.session_state.credit_data_card)

    st.markdown("""
    The Data Card clearly outlines the dataset's characteristics and, critically, highlights potential biases and data quality issues. As a Risk Manager, you note the "Historical lending bias" and "Underrepresentation" as immediate red flags for fairness, while "Missing Data" and "CreditScore Lag" point to accuracy and reliability concerns. This information directly informs the data-related risks you'll formally document in the risk register.
    """)
    st.markdown("---")
    
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("Previous Step", key="page3_prev_btn"):
            go_to_page(1) # Navigate to "Model Overview & Card"
    with col2:
        if st.button("Next: AI Risk Frameworks", key="page3_next_btn"):
            go_to_page(3) # Navigate to "AI Risk Frameworks"

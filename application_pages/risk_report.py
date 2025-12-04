import streamlit as st
import pandas as pd

def main():
    st.header("Risk Report")
    st.markdown("Generate a comprehensive report summarizing the current state of the AI Risk Register.")

    if st.session_state.ai_risk_register_df.empty:
        st.warning("The AI Risk Register is empty. Please generate some synthetic data or add risks in the 'AI Risk Register' section before generating a report.")
        return

    if st.button("Generate Comprehensive Risk Report"):
        from app import generate_risk_report # Assuming app.py makes it available
        report_markdown = generate_risk_report(st.session_state.ai_risk_register_df)
        st.markdown(report_markdown)

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker
import random
import plotly.express as px # For enhanced interactive visualizations

st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()

# Explain the business logic here
st.markdown("""
In this lab, we develop a Streamlit application for the lab "Lab 1: Principles of AI Risk and Assurance - Clone".
This application serves as an interactive tool for managing AI model risks, encompassing identification, assessment, mitigation planning, and continuous monitoring.
It integrates foundational frameworks like SR 11-7 and the NIST AI Risk Management Framework (AI RMF 1.0) to provide a structured approach to AI assurance in regulated environments.
""")

# Initialize session state for the DataFrame if it doesn't exist
if 'ai_risk_register_df' not in st.session_state:
    st.session_state.ai_risk_register_df = pd.DataFrame(columns=[
        "Risk_ID", "Risk_Description", "Risk_Category", "Likelihood", "Impact",
        "Mitigation_Controls", "Response_Plan", "NIST_AI_RMF_Function",
        "SR_11_7_Pillar", "Responsible_Party", "Status", "Risk_Priority_Score"
    ]) # Start with an empty DataFrame with all columns

# --- Code from Notebook: generate_synthetic_risk_data ---
def generate_synthetic_risk_data(num_risks):
    """
    Generates a synthetic AI Model Risk Register DataFrame.

    Args:
        num_risks (int): The number of synthetic risk entries to generate.

    Returns:
        pd.DataFrame: A DataFrame containing the synthetic AI risk register.
    """
    fake = Faker()

    risk_categories = ["Data", "Model", "System", "Human", "Organizational"]
    likelihood_options = ["Low", "Medium", "High"]
    impact_options = ["Low", "Medium", "High"]
    nist_rmf_functions = ["Govern", "Map", "Measure", "Manage"]
    sr_11_7_pillars = ["Development/Implementation", "Validation", "Governance", "Ongoing Monitoring"]
    status_options = ["Identified", "In Progress", "Mitigated", "Monitored"]

    data = []
    # Ensure Risk_ID starts from 1, or from max_id + 1 if df is not empty
    current_max_id = st.session_state.ai_risk_register_df["Risk_ID"].max() if not st.session_state.ai_risk_register_df.empty else 0
    for i in range(1, num_risks + 1):
        risk_category = random.choice(risk_categories)
        likelihood = random.choice(likelihood_options)
        impact = random.choice(impact_options)
        nist_function = random.choice(nist_rmf_functions)
        sr_pillar = random.choice(sr_11_7_pillars)
        status = random.choice(status_options)

        risk_description_template = {
            "Data": f"Potential data drift in the {fake.word()} dataset affecting model fairness.",
            "Model": f"Risk of {fake.word()} model hallucinating during automated report generation.",
            "System": f"Integration flaw in the {fake.company()} API leading to data corruption.",
            "Human": f"Over-reliance on AI recommendations leading to incorrect {fake.job()} decisions.",
            "Organizational": f"Lack of clear governance for AI model {fake.currency_name()} deployment."
        }
        mitigation_template = {
            "Data": f"Implement {fake.word()} data quality checks and monitoring.",
            "Model": f"Enhance model explainability and add human-in-the-loop review.",
            "System": f"Conduct security audits for AI system integration points.",
            "Human": f"Develop clear operational guidelines for AI interaction.",
            "Organizational": f"Establish an AI Risk Committee and define clear roles."
        }
        response_plan_template = {
            "Data": f"Retrain model with updated {fake.word()} and re-validate.",
            "Model": f"Investigate root cause of {fake.word()} errors and recalibrate.",
            "System": f"Rollback system and patch security vulnerabilities.",
            "Human": f"Provide additional training on AI limitations and best practices.",
            "Organizational": f"Revise AI governance policies and communication strategy."
        }

        data.append({
            "Risk_ID": current_max_id + i,
            "Risk_Description": risk_description_template[risk_category],
            "Risk_Category": risk_category,
            "Likelihood": likelihood,
            "Impact": impact,
            "Mitigation_Controls": mitigation_template[risk_category],
            "Response_Plan": response_plan_template[risk_category],
            "NIST_AI_RMF_Function": nist_function,
            "SR_11_7_Pillar": sr_pillar,
            "Responsible_Party": fake.name(),
            "Status": status
        })

    df = pd.DataFrame(data)
    return df


# --- Code from Notebook: calculate_risk_priority_score ---
def calculate_risk_priority_score(df_register):
    """
    Calculates the Risk_Priority_Score for each risk in the DataFrame.

    Args:
        df_register (pd.DataFrame): The AI Risk Register DataFrame.

    Returns:
        pd.Series: A Series containing the calculated Risk_Priority_Score.
    """
    likelihood_map = {"Low": 1, "Medium": 2, "High": 3}
    impact_map = {"Low": 1, "Medium": 2, "High": 3}

    # Ensure the columns exist before mapping
    if "Likelihood" in df_register.columns and "Impact" in df_register.columns:
        numeric_likelihood = df_register["Likelihood"].map(likelihood_map)
        numeric_impact = df_register["Impact"].map(impact_map)
        return numeric_likelihood * numeric_impact
    else:
        return pd.Series([None] * len(df_register)) # Return NaNs if columns are missing


# --- Code from Notebook: update_risk_status ---
def update_risk_status(df_register, risk_id, new_status):
    """
    Updates the 'Status' of a specific risk in the AI Risk Register.

    Args:
        df_register (pd.DataFrame): The AI Risk Register DataFrame.
        risk_id (int): The Risk_ID of the risk to update.
        new_status (str): The new status for the risk (must be a valid status).

    Returns:
        pd.DataFrame: The updated DataFrame. Prints a message if the risk_id is not found or status is invalid.
    """
    valid_statuses = ["Identified", "In Progress", "Mitigated", "Monitored"]
    if new_status not in valid_statuses:
        st.error(f"Error: Invalid status '{new_status}'. Valid statuses are: {', '.join(valid_statuses)}")
        return df_register

    if risk_id not in df_register["Risk_ID"].values:
        st.error(f"Error: Risk with ID {risk_id} not found.")
        return df_register

    old_status = df_register.loc[df_register["Risk_ID"] == risk_id, "Status"].iloc[0]
    df_register.loc[df_register["Risk_ID"] == risk_id, "Status"] = new_status
    st.success(f"Risk ID {risk_id} status updated from '{old_status}' to '{new_status}'.")
    return df_register


# --- Code from Notebook: generate_risk_report ---
def generate_risk_report(df_register):
    """
    Generates a formatted summary report of the AI Risk Register.

    Args:
        df_register (pd.DataFrame): The AI Risk Register DataFrame.

    Returns:
        str: A Markdown-formatted string containing the risk report.
    """
    if df_register.empty:
        return "No risks in the register to generate a report."

    report = []
    report.append("# AI Model Risk Register Report\n")
    report.append(f"**Date Generated**: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    report.append(f"**Total Number of Risks Identified**: {len(df_register)}\n\n")

    report.append("## 1. Risk Summary by Category\n")
    risk_category_summary = df_register["Risk_Category"].value_counts().to_string()
    report.append(f"```\n{risk_category_summary}\n```\n\n")

    report.append("## 2. Risk Summary by Priority Score\n")
    # Ensure Risk_Priority_Score exists and is numeric before value_counts
    if "Risk_Priority_Score" in df_register.columns and pd.api.types.is_numeric_dtype(df_register["Risk_Priority_Score"]):
        risk_priority_summary = df_register["Risk_Priority_Score"].value_counts().sort_index().to_string()
        report.append(f"```\n{risk_priority_summary}\n```\n\n")
    else:
        report.append("`Risk_Priority_Score` not available or not numeric.\n\n")


    report.append("## 3. Risk Status Overview\n")
    risk_status_summary = df_register["Status"].value_counts().to_string()
    report.append(f"```\n{risk_status_summary}\n```\n\n")

    report.append("## 4. Top 5 High Priority Risks\n")
    if len(df_register) > 0 and "Risk_Priority_Score" in df_register.columns:
        top_risks = df_register.sort_values(by="Risk_Priority_Score", ascending=False).head(5)
        report.append(top_risks[['Risk_ID', 'Risk_Description', 'Risk_Category', 'Likelihood', 'Impact', 'Risk_Priority_Score', 'Status']].to_markdown(index=False))
        report.append("\n\n")
    else:
        report.append("No risks available to display top 5 high priority risks or `Risk_Priority_Score` column is missing.\n\n")


    report.append("## 5. Full AI Risk Register (first 10 entries for brevity)\n")
    if len(df_register) > 0:
        report.append(df_register.head(10).to_markdown(index=False))
        report.append("\n\n")
    else:
        report.append("No risks available to display full register.\n\n")


    report.append("## 6. Adherence to Frameworks (NIST AI RMF & SR 11-7)\n")
    report.append("### NIST AI RMF Function Distribution:\n")
    nist_rmf_summary = df_register["NIST_AI_RMF_Function"].value_counts().to_string()
    report.append(f"```\n{nist_rmf_summary}\n```\n\n")

    report.append("### SR 11-7 Pillar Distribution:\n")
    sr_11_7_summary = df_register["SR_11_7_Pillar"].value_counts().to_string()
    report.append(f"```\n{sr_11_7_summary}\n```\n\n")

    return "\n".join(report)


# Navigation
page = st.sidebar.selectbox(label="Navigation", options=["Home", "AI Risk Register", "Risk Dashboard", "Assurance Artifacts", "Risk Report"])

if page == "Home":
    from application_pages.home import main
    main()
elif page == "AI Risk Register":
    from application_pages.ai_risk_register import main
    main()
elif page == "Risk Dashboard":
    from application_pages.risk_dashboard import main
    main()
elif page == "Assurance Artifacts":
    from application_pages.assurance_artifacts import main
    main()
elif page == "Risk Report":
    from application_pages.risk_report import main
    main()


# License
st.caption('''
---
## QuantUniversity License

© QuantUniversity 2025  
This notebook was created for **educational purposes only** and is **not intended for commercial use**.  

- You **may not copy, share, or redistribute** this notebook **without explicit permission** from QuantUniversity.  
- You **may not delete or modify this license cell** without authorization.  
- This notebook was generated using **QuCreate**, an AI-powered assistant.  
- Content generated by AI may contain **hallucinated or incorrect information**. Please **verify before using**.  

All rights reserved. For permissions or commercial licensing, contact: [info@qusandbox.com](mailto:info@qusandbox.com)
''')

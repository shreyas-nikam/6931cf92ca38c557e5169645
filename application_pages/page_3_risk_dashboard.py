
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from utils import update_risk_status # Import for the demonstration part

def main():
    st.title("AI Risk Dashboard")
    st.markdown("""
    As a Risk Manager, this dashboard provides a high-level, interactive overview of the AI risk landscape. These visualizations are designed to help you quickly identify patterns, concentrations of risk, and progress in mitigation efforts, enabling data-driven decisions and effective communication to stakeholders.
    """)

    if 'ai_risk_register_df' not in st.session_state or st.session_state.ai_risk_register_df.empty:
        st.warning("No AI Risk Register data available to display the dashboard. Please go to the 'Home' page to generate synthetic data or add risks via the 'AI Risk Register' page.")
        return

    df = st.session_state.ai_risk_register_df

    st.header("Visualizing Risk Categories")
    st.markdown("""
    Understanding the distribution of risks across different categories is fundamental for targeted risk management. This visualization provides a clear overview of which AI risk dimensions (Data, Model, System, Human, Organizational) are most prevalent in our register, guiding your focus.
    """)
    fig_category = px.bar(
        df["Risk_Category"].value_counts().reset_index(),
        x="index", y="Risk_Category", title="Distribution of Risks by Category",
        labels={"index": "Risk Category", "Risk_Category": "Number of Risks"},
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig_category.update_layout(xaxis_title_text="Risk Category", yaxis_title_text="Number of Risks")
    st.plotly_chart(fig_category, use_container_width=True)

    st.divider()

    st.header("Visualizing Likelihood vs. Impact")
    st.markdown("""
    The Likelihood vs. Impact heatmap is a powerful tool for visualizing the overall risk profile. It shows the concentration of risks based on their assessed probability of occurrence and their potential severity. High-priority risks will typically fall into the "High Likelihood" and "High Impact" quadrants, demanding immediate attention.
    """)
    risk_matrix = pd.crosstab(
        df["Impact"],
        df["Likelihood"],
        dropna=False
    ).reindex(index=["Low", "Medium", "High"], columns=["Low", "Medium", "High"])

    fig_heatmap = px.imshow(
        risk_matrix,
        text_auto=True,
        aspect="auto",
        title="Heatmap of Likelihood vs. Impact",
        labels=dict(x="Likelihood", y="Impact", color="Count"),
        x=["Low", "Medium", "High"],
        y=["High", "Medium", "Low"], # Reverse y-axis for intuitive display
        color_continuous_scale="YlGnBu"
    )
    fig_heatmap.update_xaxes(side="top")
    st.plotly_chart(fig_heatmap, use_container_width=True)

    st.divider()

    st.header("Visualizing Risk Status")
    st.markdown("""
    Tracking the `Status` of identified risks is essential for monitoring mitigation progress and overall risk management effectiveness. This visualization provides a snapshot of where the organization stands in addressing its AI risks, allowing you to quickly see what's "Identified," "In Progress," "Mitigated," or "Monitored."
    """)
    fig_pie = px.pie(
        df,
        names="Status", title="Current Status of AI Risks",
        hole=0.3,
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig_pie, use_container_width=True)

    st.divider()

    st.header("Mapping Risks to NIST AI RMF Functions")
    st.markdown("""
    The NIST AI RMF (Risk Management Framework) provides a structured approach to managing AI risks through four core functions: Govern, Map, Measure, and Manage. Understanding how identified risks align with these functions helps you, as a Risk Manager, in strategizing mitigation actions within the framework and ensuring comprehensive coverage.

    *   **Govern**: Fostering a culture of risk management.
    *   **Map**: Identifying risks.
    *   **Measure**: Evaluating and analyzing risks.
    *   **Manage**: Acting to address risks.
    """)
    fig_nist = px.histogram(
        df,
        x="NIST_AI_RMF_Function", color="Risk_Category", barmode="group",
        title="Distribution of Risks Across NIST AI RMF Functions by Category",
        labels={"NIST_AI_RMF_Function": "NIST AI RMF Function", "count": "Number of Risks"},
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    fig_nist.update_layout(xaxis_title_text="NIST AI RMF Function", yaxis_title_text="Number of Risks")
    st.plotly_chart(fig_nist, use_container_width=True)

    st.divider()

    st.header("Mapping Risks to SR 11-7 Pillars")
    st.markdown("""
    For financial institutions, SR 11-7 provides essential guidance on model risk management, structured around key pillars: Development/Implementation, Validation, Governance, and Ongoing Monitoring. Mapping AI risks to these pillars ensures that your AI risk management integrates seamlessly with existing regulatory compliance requirements.
    """)
    fig_sr11_7 = px.histogram(
        df,
        x="SR_11_7_Pillar", color="Risk_Category", barmode="group",
        title="Distribution of Risks Across SR 11-7 Pillars by Category",
        labels={"SR_11_7_Pillar": "SR 11-7 Pillar", "count": "Number of Risks"},
        color_discrete_sequence=px.colors.qualitative.Dark24
    )
    fig_sr11_7.update_layout(xaxis_title_text="SR 11-7 Pillar", yaxis_title_text="Number of Risks")
    st.plotly_chart(fig_sr11_7, use_container_width=True)

    st.divider()

    st.header("Updating Risk Status (from Notebook Content)")
    st.markdown("""
    The AI Risk Register is a living document that requires continuous updates as mitigation efforts progress. This section demonstrates how you can programmatically update the `Status` of a specific risk once actions have been taken or new information becomes available, ensuring the dashboard reflects the most current state. (This functionality is also available directly on the 'AI Risk Register' page for direct interaction).
    """)
    if not df.empty:
        risk_ids_for_status_update = df["Risk_ID"].unique().tolist()
        selected_risk_id_status = st.selectbox("Select Risk ID to update status (for demonstration)", risk_ids_for_status_update, key="dash_update_risk_id_status")
        new_status_input = st.selectbox("New Status (for demonstration)", ["Identified", "In Progress", "Mitigated", "Monitored"], key="dash_new_status_input")

        if st.button("Update Risk Status (Demonstration)", key="dash_update_status_button"):
            # Call the utility function to update status
            st.session_state.ai_risk_register_df = update_risk_status(st.session_state.ai_risk_register_df, selected_risk_id_status, new_status_input)
            st.rerun() # Rerun to update the dashboard visualizations
    else:
        st.info("No risks in the register to update status for demonstration purposes.")

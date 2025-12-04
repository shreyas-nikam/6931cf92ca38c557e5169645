import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.header("Risk Dashboard")
    st.markdown("This dashboard provides interactive visualizations of the AI Risk Register, offering insights into the distribution and characteristics of identified risks.")

    if st.session_state.ai_risk_register_df.empty:
        st.warning("The AI Risk Register is empty. Please generate some synthetic data or add risks in the 'AI Risk Register' section to view the dashboard.")
        return

    df = st.session_state.ai_risk_register_df

    st.subheader("1. Distribution of Risks by Category")
    category_counts = df["Risk_Category"].value_counts().reset_index()
    category_counts.columns = ["Risk Category", "Number of Risks"]
    fig_category = px.bar(
        category_counts,
        x="Risk Category", y="Number of Risks", title="Distribution of Risks by Category",
        labels={"Risk Category": "Risk Category", "Number of Risks": "Number of Risks"},
        color="Risk Category"
    )
    fig_category.update_layout(xaxis_title_text="Risk Category", yaxis_title_text="Number of Risks")
    st.plotly_chart(fig_category, use_container_width=True)

    st.subheader("2. Likelihood vs. Impact Heatmap")
    risk_matrix = pd.crosstab(
        df["Impact"],
        df["Likelihood"],
        dropna=False
    ).reindex(index=["Low", "Medium", "High"], columns=["Low", "Medium", "High"])

    # Reverse y-axis for intuitive display where "High Impact" is at the top
    risk_matrix = risk_matrix.reindex(index=["High", "Medium", "Low"])
    
    fig_heatmap = px.imshow(
        risk_matrix,
        text_auto=True,
        aspect="auto",
        title="Heatmap of Likelihood vs. Impact",
        labels=dict(x="Likelihood", y="Impact", color="Count"),
        x=["Low", "Medium", "High"],
        y=["High", "Medium", "Low"], # Ensure the labels match the reindexed order
        color_continuous_scale="YlGnBu"
    )
    fig_heatmap.update_xaxes(side="top")
    st.plotly_chart(fig_heatmap, use_container_width=True)

    st.subheader("3. Current Status of AI Risks")
    status_counts = df["Status"].value_counts().reset_index()
    status_counts.columns = ["Status", "Count"]
    fig_pie = px.pie(
        status_counts,
        names="Status", values="Count", title="Current Status of AI Risks",
        hole=0.3
    )
    st.plotly_chart(fig_pie, use_container_width=True)

    st.subheader("4. Distribution of Risks Across NIST AI RMF Functions by Category")
    fig_nist = px.histogram(
        df,
        x="NIST_AI_RMF_Function", color="Risk_Category", barmode="group",
        title="Distribution of Risks Across NIST AI RMF Functions by Category",
        labels={"NIST_AI_RMF_Function": "NIST AI RMF Function", "count": "Number of Risks"}
    )
    st.plotly_chart(fig_nist, use_container_width=True)

    st.subheader("5. Distribution of Risks Across SR 11-7 Pillars by Category")
    fig_sr11_7 = px.histogram(
        df,
        x="SR_11_7_Pillar", color="Risk_Category", barmode="group",
        title="Distribution of Risks Across SR 11-7 Pillars by Category",
        labels={"SR_11_7_Pillar": "SR 11-7 Pillar", "count": "Number of Risks"}
    )
    st.plotly_chart(fig_sr11_7, use_container_width=True)

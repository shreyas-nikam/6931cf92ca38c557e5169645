
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


def initialize_app_state():
    """Initialize session state variables for the app."""
    # Initialize session state variables if they don't exist
    if 'current_sidebar_page_index' not in st.session_state:
        # Corresponds to the index in the sidebar selectbox
        st.session_state.current_sidebar_page_index = 0
    if 'risk_register_df' not in st.session_state:
        st.session_state.risk_register_df = pd.DataFrame(columns=[
            "Risk ID", "Dimension", "Category", "Description",
            "Potential Impact", "Likelihood", "Risk Score",
            "Mitigation Strategy", "Responsible Party", "Status"
        ])
    if 'next_risk_id' not in st.session_state:
        st.session_state.next_risk_id = 1

    # --- Model Scenario and Card Initializations ---
    # These should ideally be initialized only once, so placing them in utils and checking session state is correct.
    if 'credit_risk_model_scenario' not in st.session_state:
        def initialize_model_scenario_metadata():
            model_metadata = {
                "Name": "Credit Risk Scoring Model v1.0",
                "Type": "Supervised Learning, Classification",
                "Algorithm": "Gradient Boosting Classifier (e.g., LightGBM)",
                "Purpose": "To predict the likelihood of loan default for retail loan applicants.",
                "Intended_Use": "Automate approval for low-risk applicants and flag high-risk applicants for manual underwriting review.",
                "Key_Inputs": ["Age", "Income", "LoanAmount", "CreditScore", "EmploymentStatus", "ResidentialStatus"],
                "Output": "Probability of Default (0-1), Binary Decision (Approve/Reject)",
                "Development_Team": "QuantBank Data Science Department",
                "Deployment_Environment": "API integrated into legacy Loan Origination System",
                "Regulatory_Context": "SR 11-7, potential for future AI-specific regulations"
            }
            return model_metadata
        st.session_state.credit_risk_model_scenario = initialize_model_scenario_metadata()

    if 'hypothetical_auc' not in st.session_state:
        st.session_state.hypothetical_auc = 0.85
    if 'hypothetical_precision_at_recall' not in st.session_state:
        st.session_state.hypothetical_precision_at_recall = 0.60

    if 'credit_risk_model_card' not in st.session_state:
        model_card_template = {
            "Model Name": None,
            "Version": None,
            "Purpose": None,
            "Intended Use": None,
            "Algorithm": None,
            "Key Performance Metrics": {},
            "Known Limitations": [],
            "Developer": None,
            "Last Review Date": None
        }

        def populate_model_card(model_metadata, auc_score, precision_at_recall_90):
            model_card = model_card_template.copy()
            model_card["Model Name"] = model_metadata["Name"]
            model_card["Version"] = "1.0"
            model_card["Purpose"] = model_metadata["Purpose"]
            model_card["Intended Use"] = model_metadata["Intended_Use"]
            model_card["Algorithm"] = model_metadata["Algorithm"]
            model_card["Key Performance Metrics"] = {
                "AUC": auc_score,
                "Precision@90%Recall": precision_at_recall_90,
                "Target Variable": "Defaulted (Binary: 1 for default, 0 for no default)"
            }
            model_card["Known Limitations"] = [
                "Potential for disparate impact on certain demographic groups due to historical data biases.",
                "Performance may degrade with significant shifts in economic conditions not present in training data.",
                "Limited interpretability for individual predictions (black-box nature of Gradient Boosting)."
            ]
            model_card["Developer"] = model_metadata["Development_Team"]
            model_card["Last Review Date"] = "2024-03-15"
            return model_card
        st.session_state.credit_risk_model_card = populate_model_card(
            st.session_state.credit_risk_model_scenario,
            st.session_state.hypothetical_auc,
            st.session_state.hypothetical_precision_at_recall
        )

    if 'synthetic_dataset_details' not in st.session_state:
        st.session_state.synthetic_dataset_details = {
            "dataset_name": "Credit_Application_Data",
            "source": "Internal CRM and historical loan records (synthetic generation)",
            "collection_method": "Aggregated transactional and demographic data, anonymized",
            "size": (10000, 7),
            "features_desc": {
                "Age": "Applicant's age (years)",
                "Income": "Annual income (USD)",
                "LoanAmount": "Requested loan amount (USD)",
                "CreditScore": "Credit score from a third-party bureau",
                "EmploymentStatus": "Categorical: Employed, Unemployed, Student, Retired",
                "ResidentialStatus": "Categorical: Owner, Renter, Other",
                "Defaulted": "Binary target: 1 if loan defaulted, 0 otherwise"
            },
            "sensitive_features": ["Age", "Income", "ResidentialStatus"],
            "potential_biases": [
                "Historical lending bias: Dataset shows lower approval rates for 'Renter' in specific income brackets.",
                "Underrepresentation: Limited data for applicants under 25 or over 65.",
                "Missing Data: Approximately 5% missing values in 'EmploymentStatus', imputed with mode.",
                "CreditScore Lag: CreditScore data updated quarterly, may not reflect real-time creditworthiness."
            ],
            "preprocessing_steps": [
                "Missing 'EmploymentStatus' values imputed using mode strategy.",
                "Categorical features one-hot encoded.",
                "Numerical features scaled using StandardScaler."
            ]
        }
    if 'credit_data_card' not in st.session_state:
        data_card_template = {
            "Dataset Name": None,
            "Source": None,
            "Collection Method": None,
            "Size (rows, features)": None,
            "Features Description": {},
            "Sensitive Features": [],
            "Potential Biases": [],
            "Preprocessing Steps": [],
            "Last Update Date": None
        }

        def populate_data_card(dataset_name, source, collection_method, size, features_desc, sensitive_features, potential_biases, preprocessing_steps):
            data_card = data_card_template.copy()
            data_card["Dataset Name"] = dataset_name
            data_card["Source"] = source
            data_card["Collection Method"] = collection_method
            data_card["Size (rows, features)"] = size
            data_card["Features Description"] = features_desc
            data_card["Sensitive Features"] = sensitive_features
            data_card["Potential Biases"] = potential_biases
            data_card["Preprocessing Steps"] = preprocessing_steps
            data_card["Last Update Date"] = "2024-03-10"
            return data_card
        st.session_state.credit_data_card = populate_data_card(
            **st.session_state.synthetic_dataset_details)


# --- Helper functions for navigation (to be called from pages) ---
def go_to_page(page_index):
    st.session_state.current_sidebar_page_index = page_index
    st.rerun()

# --- Core Functions from Notebook ---


def add_risk_to_register(dimension, category, description, potential_impact="Medium", likelihood="Medium"):
    impact_map = {"Low": 1, "Medium": 2, "High": 3}
    likelihood_map = {"Low": 1, "Medium": 2, "High": 3}

    impact_score = impact_map.get(potential_impact, 0)
    likelihood_score = likelihood_map.get(likelihood, 0)
    risk_score = impact_score * likelihood_score

    new_risk = {
        "Risk ID": f"R{st.session_state.next_risk_id:03d}",
        "Dimension": dimension,
        "Category": category,
        "Description": description,
        "Potential Impact": potential_impact,
        "Likelihood": likelihood,
        "Risk Score": risk_score,
        "Mitigation Strategy": "To be determined",
        "Responsible Party": "TBD",
        "Status": "Identified"
    }
    st.session_state.risk_register_df = pd.concat(
        [st.session_state.risk_register_df, pd.DataFrame([new_risk])], ignore_index=True)
    st.session_state.next_risk_id += 1


def assess_risk_severity(risk_id, potential_impact, likelihood):
    impact_map = {"Low": 1, "Medium": 2, "High": 3}
    likelihood_map = {"Low": 1, "Medium": 2, "High": 3}

    idx = st.session_state.risk_register_df[st.session_state.risk_register_df["Risk ID"] == risk_id].index
    if not idx.empty:
        idx = idx[0]
        st.session_state.risk_register_df.loc[idx,
                                              "Potential Impact"] = potential_impact
        st.session_state.risk_register_df.loc[idx, "Likelihood"] = likelihood

        impact_score = impact_map.get(potential_impact, 0)
        likelihood_score = likelihood_map.get(likelihood, 0)
        st.session_state.risk_register_df.loc[idx,
                                              "Risk Score"] = impact_score * likelihood_score
        st.session_state.risk_register_df.loc[idx, "Status"] = "Assessed"
        st.success(
            f"Risk {risk_id} updated with Impact: {potential_impact}, Likelihood: {likelihood}, Score: {impact_score * likelihood_score}")
    else:
        st.error(f"Risk ID {risk_id} not found.")


def plot_risk_matrix(risk_df):
    import numpy as np

    impact_order = ["Low", "Medium", "High"]
    likelihood_order = ["Low", "Medium", "High"]

    risk_df_plot = risk_df.copy()
    # Filter out risks that haven't been assessed (Risk Score 0 if not assessed properly)
    risk_df_plot = risk_df_plot[risk_df_plot['Risk Score'] > 0]

    if risk_df_plot.empty:
        st.info(
            "No assessed risks to display in the matrix yet. Please assess some risks first.")
        return

    # Map qualitative ratings to numerical for plotting
    risk_df_plot["Impact_Num"] = risk_df_plot["Potential Impact"].map(
        lambda x: impact_order.index(x) + 0.5)
    risk_df_plot["Likelihood_Num"] = risk_df_plot["Likelihood"].map(
        lambda x: likelihood_order.index(x) + 0.5)

    # Add uniform spread to prevent overlapping points
    # Initialize offset columns
    risk_df_plot["offset_x"] = 0.0
    risk_df_plot["offset_y"] = 0.0

    # Group by same coordinates and spread them in a circular pattern
    grouped = risk_df_plot.groupby(
        ['Likelihood_Num', 'Impact_Num'], sort=False)

    for (lik, imp), group in grouped:
        n_points = len(group)
        if n_points > 1:
            # Distribute points uniformly in a circle
            radius = 0.2  # Maximum offset from center
            angles = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
            offsets_x = radius * np.cos(angles)
            offsets_y = radius * np.sin(angles)

            # Assign offsets to the correct indices
            for i, idx in enumerate(group.index):
                risk_df_plot.loc[idx, "offset_x"] = offsets_x[i]
                risk_df_plot.loc[idx, "offset_y"] = offsets_y[i]

    # Apply offsets
    risk_df_plot["Likelihood_Num"] = risk_df_plot["Likelihood_Num"] + \
        risk_df_plot["offset_x"]
    risk_df_plot["Impact_Num"] = risk_df_plot["Impact_Num"] + \
        risk_df_plot["offset_y"]

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.scatterplot(
        data=risk_df_plot,
        x="Likelihood_Num",
        y="Impact_Num",
        hue="Risk Score",
        size="Risk Score",
        sizes=(100, 1000),
        palette="viridis",
        legend="full",
        ax=ax
    )

    # Set matrix grid
    ax.axvline(x=1, color='gray', linestyle='--', linewidth=0.8)
    ax.axvline(x=2, color='gray', linestyle='--', linewidth=0.8)
    ax.axhline(y=1, color='gray', linestyle='--', linewidth=0.8)
    ax.axhline(y=2, color='gray', linestyle='--', linewidth=0.8)

    # Add background colors for risk levels
    # High Risk (Red)
    ax.axvspan(2, 3, ymin=2/3, ymax=1, color='red',
               alpha=0.15, label='High Risk')
    # Medium-High Risk (Orange)
    ax.axvspan(2, 3, ymin=1/3, ymax=2/3, color='orange', alpha=0.15)
    ax.axvspan(1, 2, ymin=2/3, ymax=1, color='orange', alpha=0.15)
    # Medium Risk (Yellow)
    ax.axvspan(2, 3, ymin=0, ymax=1/3, color='yellow', alpha=0.15)
    ax.axvspan(1, 2, ymin=1/3, ymax=2/3, color='yellow', alpha=0.15)
    ax.axvspan(0, 1, ymin=2/3, ymax=1, color='yellow', alpha=0.15)
    # Low-Medium Risk (Green)
    ax.axvspan(1, 2, ymin=0, ymax=1/3, color='green', alpha=0.15)
    ax.axvspan(0, 1, ymin=1/3, ymax=2/3, color='green', alpha=0.15)
    # Low Risk (Light Green)
    ax.axvspan(0, 1, ymin=0, ymax=1/3, color='lightgreen',
               alpha=0.15, label='Low Risk')

    ax.set_xticks([0.5, 1.5, 2.5])
    ax.set_xticklabels(likelihood_order)
    ax.set_yticks([0.5, 1.5, 2.5])
    ax.set_yticklabels(impact_order)
    ax.set_xlabel("Likelihood")
    ax.set_ylabel("Potential Impact")
    ax.set_title("AI Model Risk Matrix: Credit Risk Scoring Model")

    # Annotate points with Risk ID
    for i, row in risk_df_plot.iterrows():
        ax.annotate(row["Risk ID"], (row["Likelihood_Num"] +
                    0.1, row["Impact_Num"] + 0.1), fontsize=8)

    ax.grid(False)  # Remove default grid to avoid overlap with custom lines
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    st.pyplot(fig)


def add_mitigation_strategy(risk_id, strategy_description, responsible_party):
    idx = st.session_state.risk_register_df[st.session_state.risk_register_df["Risk ID"] == risk_id].index
    if not idx.empty:
        idx = idx[0]
        st.session_state.risk_register_df.loc[idx,
                                              "Mitigation Strategy"] = strategy_description
        st.session_state.risk_register_df.loc[idx,
                                              "Responsible Party"] = responsible_party
        st.session_state.risk_register_df.loc[idx,
                                              "Status"] = "Mitigation Proposed"
        st.success(f"Mitigation strategy added for Risk {risk_id}.")
    else:
        st.error(f"Risk ID {risk_id} not found.")


def generate_risk_register_report(risk_df):
    final_columns = [
        "Risk ID", "Dimension", "Category", "Description",
        "Potential Impact", "Likelihood", "Risk Score",
        "Mitigation Strategy", "Responsible Party", "Status"
    ]

    report_df = risk_df[final_columns].copy()
    report_df = report_df.sort_values(by="Risk Score", ascending=False)
    report_df.reset_index(drop=True, inplace=True)
    return report_df


def plot_risk_distribution(risk_df):
    if risk_df.empty:
        st.info("No risks identified yet for distribution plot.")
        return

    risk_counts_by_dimension = risk_df['Dimension'].value_counts()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=risk_counts_by_dimension.index,
                y=risk_counts_by_dimension.values, palette='viridis', ax=ax)
    ax.set_title('Distribution of Identified Risks Across AI Dimensions')
    ax.set_xlabel('AI Risk Dimension')
    ax.set_ylabel('Number of Risks')
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

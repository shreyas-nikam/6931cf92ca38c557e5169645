
## Streamlit Application Requirements Specification: AI Model Risk Assessment for Credit Decisions

### 1. Application Overview

**Narrative Alignment:**
As a Quantitative Analyst at QuantBank, the user will embark on a critical mission: to conduct a formal risk assessment of a new AI-powered Credit Risk Scoring Model. This model is poised to automate loan approvals and flag high-risk applicants, making its integrity and compliance paramount. The application will guide the user through a systematic process, from understanding the model and its data to identifying, assessing, mitigating, and reporting AI risks, all within the context of stringent financial regulations (SR 11-7) and best practices for trustworthy AI (NIST AI RMF 1.0). Each interactive step in the application reflects a real-world task the persona would perform, moving them closer to ensuring responsible AI deployment.

**Real-World Problem:**
The core problem is to ensure the newly developed Credit Risk Scoring Model adheres to regulatory standards (SR 11-7) and promotes trustworthy AI principles (NIST AI RMF 1.0) before deployment. Failure to identify and mitigate risks could lead to significant financial losses, reputational damage, regulatory penalties, and unfair outcomes for loan applicants. The persona needs a structured, auditable way to manage these complex AI risks.

**How the Streamlit App Helps:**
The Streamlit application serves as an interactive workbench for the Quantitative Analyst. It simplifies the complex task of AI risk management by:
1.  **Providing structured documentation:** Automatically generating and displaying a Model Card and Data Card based on predefined scenarios.
2.  **Guiding risk identification:** Systematically prompting the user to consider risks across five key AI dimensions (Data, Model, System, Human, Organizational) and pre-populating a Risk Register with common risks.
3.  **Facilitating quantitative assessment:** Allowing the user to qualitatively assess the "Potential Impact" and "Likelihood" of risks, automatically calculating a $Risk = Impact \times Likelihood$ score.
4.  **Visualizing the risk landscape:** Generating an interactive Risk Matrix to highlight high-priority risks for stakeholders.
5.  **Enabling mitigation planning:** Providing tools to document mitigation strategies and assign responsible parties for each risk.
6.  **Consolidating findings:** Producing a comprehensive, sortable AI Risk Register and a risk distribution overview, ready for "Effective Challenge" and reporting.

The application allows the persona to directly engage with AI risk management principles, making abstract concepts concrete through scenario-based decision-making.

**Learning Goals (Applied Skills for the Persona):**
By interacting with the app, the persona will gain applied skills in:
*   **Applying AI Governance Frameworks:** Understanding how SR 11-7 and NIST AI RMF 1.0 principles translate into practical risk identification and management for AI models.
*   **Developing AI Assurance Artifacts:** Generating and interpreting Model Cards and Data Cards as foundational documentation for AI transparency and auditability.
*   **Systematic AI Risk Identification:** Identifying specific risks across the five dimensions (Data, Model, System, Human, Organizational) relevant to a financial AI model.
*   **Qualitative Risk Assessment:** Assigning "Potential Impact" and "Likelihood" scores to risks and understanding their implication for prioritization ($Risk = Impact \times Likelihood$).
*   **Risk Visualization and Communication:** Using a Risk Matrix to visually represent the risk landscape and communicate priorities to diverse stakeholders.
*   **Proposing Mitigation Strategies:** Formulating concrete, actionable mitigation strategies for identified high-priority risks and assigning accountability.
*   **Maintaining an AI Risk Register:** Dynamically updating and managing a comprehensive risk register as a living document for ongoing AI risk management and compliance.

### 2. User Interface Requirements

The UI will guide the persona through a linear, multi-step story, presenting information and interactive elements chronologically.

#### Layout & Navigation Structure

The application will be structured as a single-page Streamlit app, using `st.session_state` to manage the `current_page` and display content dynamically. A main content area will display the current step, with clear "Next Step" and "Previous Step" buttons (where applicable) to drive the narrative flow.

**Page Flow:**

1.  **Welcome & Scenario Setup (Page 1)**
    *   **Header:** "AI Model Risk Assessment: Credit Risk Scoring Model"
    *   **Content:** Markdown introducing the persona's role and the Credit Risk Model scenario. Explanation of $Risk = Impact \times Likelihood$.
    *   **Navigation:** "Start Assessment" button.

2.  **Model Overview & Card (Page 2)**
    *   **Header:** "2. Understanding the Credit Risk AI Model"
    *   **Content:** Markdown for "Introducing the Model Under Scrutiny" and "Constructing the AI Model Card".
    *   **Navigation:** "Previous Step" and "Next: Data Card" buttons.

3.  **Data Overview & Card (Page 3)**
    *   **Header:** "3. Dissecting the Data for the Credit Risk Model"
    *   **Content:** Markdown for "Dissecting the Data: Creating a Data Card".
    *   **Navigation:** "Previous Step" and "Next: AI Risk Frameworks" buttons.

4.  **AI Risk Frameworks (Page 4)**
    *   **Header:** "4. Foundations: SR 11-7 & NIST AI RMF 1.0"
    *   **Content:** Markdown for "Foundations of Financial Model Risk: SR 11-7 in an AI Context" and "Embracing Trustworthy AI: The NIST AI RMF 1.0 Framework".
    *   **Navigation:** "Previous Step" and "Next: Identify AI Risks" buttons.

5.  **AI Risk Register: Identify Risks (Page 5)**
    *   **Header:** "5. AI Risk Register: Systematic Identification"
    *   **Content:** Markdown for all "Identifying X-Related Risks" sections.
    *   **Navigation:** "Previous Step" and "Next: Assess Risk Severity" buttons.

6.  **AI Risk Register: Assess Risk Severity (Page 6)**
    *   **Header:** "6. AI Risk Register: Severity Assessment"
    *   **Content:** Markdown for "Assessing Risk Severity: Impact and Likelihood Scoring".
    *   **Navigation:** "Previous Step" and "Next: Visualize Risk Landscape" buttons.

7.  **AI Risk Matrix Visualization (Page 7)**
    *   **Header:** "7. Visualizing the Risk Landscape: The AI Risk Matrix"
    *   **Content:** Markdown for "Visualizing the Risk Landscape: The AI Risk Matrix".
    *   **Navigation:** "Previous Step" and "Next: Develop Mitigation Strategies" buttons.

8.  **AI Risk Register: Mitigation Strategies (Page 8)**
    *   **Header:** "8. AI Risk Register: Strategic Mitigation"
    *   **Content:** Markdown for "Strategic Risk Mitigation: Developing Controls".
    *   **Navigation:** "Previous Step" and "Next: Generate Final Report" buttons.

9.  **Final AI Risk Report (Page 9)**
    *   **Header:** "9. Comprehensive AI Risk Report"
    *   **Content:** Markdown for "Consolidating Findings: Populating the AI Risk Register" and "Concluding the Assessment: Preparing for Effective Challenge".
    *   **Navigation:** "Restart Assessment" button.

#### Input Widgets and Controls

All inputs will be dynamically displayed based on the `st.session_state.current_page`.

**Page 5: AI Risk Register - Identify Risks**

*   **Widget:** `st.button("Pre-populate Initial Risks")`
    *   **Purpose in Story:** Persona chooses to load a set of common initial risks to jumpstart the assessment, reflecting a common starting point in risk management.
    *   **Action:** Triggers the `add_risk_to_register` calls from notebook cells 7-11.
*   **Widget:** `st.expander("Manually Add a New Risk")`
    *   **Purpose in Story:** Persona identifies a unique risk not covered by the pre-populated list, demonstrating their critical thinking beyond predefined scenarios.
    *   **Input Controls within expander:**
        *   `st.selectbox("Dimension", options=["Data", "Model", "System", "Human", "Organizational"])`
            *   **Purpose:** Categorizing the risk according to the AI Risk Taxonomy.
        *   `st.text_input("Category", help="e.g., Data Quality, Algorithmic Bias")`
            *   **Purpose:** Providing a specific sub-category for the risk.
        *   `st.text_area("Description", help="Detailed description of the risk, including how it might impact the model or business.")`
            *   **Purpose:** Articulating the nature of the risk.
        *   `st.selectbox("Potential Impact", options=["Low", "Medium", "High"], index=1)` (Default: Medium)
            *   **Purpose:** Initial qualitative assessment of the severity if the risk materializes.
        *   `st.selectbox("Likelihood", options=["Low", "Medium", "High"], index=1)` (Default: Medium)
            *   **Purpose:** Initial qualitative assessment of the probability of the risk occurring.
        *   `st.button("Add Risk", key="add_new_risk_btn")`
            *   **Purpose:** Committing the new risk to the register.

**Page 6: AI Risk Register - Assess Risk Severity**

*   **Widget:** `st.button("Auto-Assess Key Risks")`
    *   **Purpose in Story:** Persona leverages predefined assessments for critical risks to quickly prioritize. This reflects realistic scenario where some risks have known impact/likelihood.
    *   **Action:** Triggers the `assess_risk_severity` calls from notebook cell 12.
*   **Widget:** `st.selectbox("Select Risk ID to Assess", options=risk_register_df['Risk ID'].tolist())`
    *   **Purpose in Story:** Persona selects a specific risk from the comprehensive register to re-evaluate its severity based on new information or deeper analysis.
    *   **Parameters:** Options populated from current `st.session_state.risk_register_df`.
*   **Widget:** `st.selectbox("Update Potential Impact", options=["Low", "Medium", "High"])`
    *   **Purpose:** Revising the impact assessment for the selected risk.
*   **Widget:** `st.selectbox("Update Likelihood", options=["Low", "Medium", "High"])`
    *   **Purpose:** Revising the likelihood assessment for the selected risk.
*   **Widget:** `st.button("Update Risk Severity")`
    *   **Purpose:** Applies the new impact and likelihood to the selected risk and recalculates its score.

**Page 8: AI Risk Register - Mitigation Strategies**

*   **Widget:** `st.button("Auto-Populate Mitigations for Top Risks")`
    *   **Purpose in Story:** Persona starts with established best-practice mitigation strategies for the most critical risks, demonstrating efficiency.
    *   **Action:** Triggers the `add_mitigation_strategy` calls from notebook cell 14.
*   **Widget:** `st.selectbox("Select Risk ID to Add Mitigation", options=risk_register_df['Risk ID'].tolist())`
    *   **Purpose in Story:** Persona selects a specific risk to define or refine its mitigation strategy.
*   **Widget:** `st.text_area("Mitigation Strategy Description", height=100)`
    *   **Purpose:** Detailing the plan to reduce or control the selected risk.
*   **Widget:** `st.text_input("Responsible Party", help="e.g., Data Science Team, Compliance Department")`
    *   **Purpose:** Assigning ownership for the mitigation implementation.
*   **Widget:** `st.button("Add/Update Mitigation Strategy")`
    *   **Purpose:** Commits the mitigation details to the selected risk.

#### Visualization Components

All visualizations will be rendered using `st.pyplot` from `matplotlib` and `seaborn`.

**Page 2: Model Overview & Card**

*   **Output:** Formatted display of `model_metadata` and `credit_risk_model_card` dictionaries.
    *   **Format:** `st.json` for raw data, or `st.markdown` with bullet points for readability.
    *   **Purpose in Story:** Allows the persona to review critical model details and performance metrics (e.g., AUC = 0.85, Precision@90%Recall = 0.60) at a glance, forming the basis for initial risk intuition.

**Page 3: Data Overview & Card**

*   **Output:** Formatted display of `synthetic_dataset_details` and `credit_data_card` dictionaries.
    *   **Format:** `st.json` or `st.markdown` with bullet points.
    *   **Purpose in Story:** Provides the persona with a clear overview of the data's characteristics, potential biases, and preprocessing steps, enabling them to identify data-centric risks.

**Page 5, 6, 8: AI Risk Register Table**

*   **Output:** `st.dataframe(risk_register_df)`
    *   **Format:** Interactive table with columns: 'Risk ID', 'Dimension', 'Category', 'Description', 'Potential Impact', 'Likelihood', 'Risk Score', 'Mitigation Strategy', 'Responsible Party', 'Status'.
    *   **Purpose in Story:** This table is the central "living document" for the persona. It dynamically updates as risks are identified, assessed, and mitigated, providing a real-time view of the AI model's risk profile. It will be sortable by 'Risk Score' descending to show highest priority risks first.

**Page 7: AI Risk Matrix**

*   **Output:** Scatter plot generated by `plot_risk_matrix(risk_register_df)`.
    *   **Libraries:** `matplotlib.pyplot` and `seaborn`.
    *   **Format:** X-axis: "Likelihood", Y-axis: "Potential Impact". Points colored and sized by "Risk Score". Annotated with "Risk ID". Grid lines representing Low/Medium/High boundaries, with background colors indicating risk zones (e.g., green for low, yellow for medium, red for high).
    *   **Purpose in Story:** Enables the persona to visually communicate the entire risk landscape to stakeholders, quickly highlighting critical risks (High Impact, High Likelihood) for strategic discussion and resource allocation.

**Page 9: Distribution of Identified Risks Across AI Dimensions**

*   **Output:** Bar chart showing `risk_counts_by_dimension`.
    *   **Libraries:** `matplotlib.pyplot` and `seaborn`.
    *   **Format:** X-axis: 'AI Risk Dimension' (Data, Model, System, Human, Organizational), Y-axis: 'Number of Risks'.
    *   **Purpose in Story:** Provides the persona with a high-level summary of where the majority of identified risks lie, informing broader organizational focus areas for AI risk management and resource allocation.

#### Interactive Elements & Feedback Mechanisms

*   **Navigation Buttons:** `st.button("Next Step")` and `st.button("Previous Step")` will control `st.session_state.current_page` to move through the linear story.
*   **"Add Risk", "Update Risk Severity", "Add/Update Mitigation Strategy" buttons:** These trigger the corresponding backend functions and update `st.session_state.risk_register_df`.
*   **Dynamic Dataframe Updates:** The `risk_register_df` will automatically re-render after any addition or update, providing immediate visual feedback.
*   **Success Messages:** After adding/updating a risk or mitigation, a brief `st.success` message will confirm the action (e.g., "Risk R001 updated successfully!").
*   **Error Handling:** Basic validation (e.g., ensuring a Risk ID exists before updating) will display `st.error` if an operation fails.

### 3. Additional Requirements

#### Annotations & Tooltips

*   **Framework Explanations:**
    *   On Page 4 ("AI Risk Frameworks"), use `st.expander` components for SR 11-7 and NIST AI RMF 1.0. Inside each expander, detailed markdown explanations from the notebook content will be provided, contextualized for how the persona applies them.
    *   For example, for SR 11-7: `st.info("As a Quant Analyst, SR 11-7 is your bedrock for model governance. Remember: model risk intensifies with complexity, input uncertainty, and broader use.")`
    *   For NIST AI RMF: `st.info("NIST AI RMF broadens the view beyond financial models, focusing on trustworthy AI attributes like Fairness, Transparency, and Accountability.")`
*   **AI Risk Taxonomy Dimensions:** On Page 5 ("Identify Risks"), use `st.expander` or `st.info` sections to briefly describe each of the five dimensions (Data, Model, System, Human, Organizational) as the persona encounters them, reinforcing their understanding of the taxonomy's application.
*   **Visualization Context:** For the Risk Matrix and Risk Distribution charts, `st.markdown` will be used to interpret the visualizations from the persona's perspective (e.g., "This matrix clearly shows R007 and R014 are in the high-risk zone, requiring immediate attention.")

#### State Management Requirements

*   **`st.session_state` Usage:** All critical application data and user progress must be preserved using `st.session_state`.
    *   `st.session_state.current_page`: Integer controlling the displayed page in the linear workflow.
    *   `st.session_state.risk_register_df`: A `pandas.DataFrame` storing the entire AI Risk Register, initialized as an empty DataFrame with specified columns. This is central to the application's state.
    *   `st.session_state.next_risk_id`: An integer counter to generate unique `Risk ID`s (e.g., 'R001').
    *   Pre-populated data: `model_metadata`, `synthetic_dataset_details`, `hypothetical_auc`, `hypothetical_precision_at_recall` can be loaded once and stored in `st.session_state` or directly referenced.
*   **Persistence:** `st.session_state` ensures that when the user navigates between steps or triggers updates, their identified risks, assessments, and mitigation strategies are not lost. The application will feel continuous and responsive to user actions.

### 4. Notebook Content and Code Requirements

The Streamlit application will directly integrate the Python functions and logic from the Jupyter Notebook, wrapping them in Streamlit UI components and narrative.

**Initialization & Global State (in `st.session_state`):**

```python
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Initialize session state variables if they don't exist
if 'current_page' not in st.session_state:
    st.session_state.current_page = 1
if 'risk_register_df' not in st.session_state:
    st.session_state.risk_register_df = pd.DataFrame(columns=[
        "Risk ID", "Dimension", "Category", "Description", 
        "Potential Impact", "Likelihood", "Risk Score", 
        "Mitigation Strategy", "Responsible Party", "Status"
    ])
if 'next_risk_id' not in st.session_state:
    st.session_state.next_risk_id = 1

# Helper function to go to next/previous page
def next_page():
    st.session_state.current_page += 1
def prev_page():
    st.session_state.current_page -= 1
def set_page(page_num):
    st.session_state.current_page = page_num

# --- Core Functions from Notebook ---

# Code Cell from "2. Introducing the Model Under Scrutiny: The Credit Risk AI"
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


# Code Cell from "3. Constructing the AI Model Card: Transparency & Key Facts"
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

st.session_state.hypothetical_auc = 0.85
st.session_state.hypothetical_precision_at_recall = 0.60
st.session_state.credit_risk_model_card = populate_model_card(
    st.session_state.credit_risk_model_scenario,
    st.session_state.hypothetical_auc,
    st.session_state.hypothetical_precision_at_recall
)


# Code Cell from "4. Dissecting the Data: Creating a Data Card"
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
st.session_state.credit_data_card = populate_data_card(**st.session_state.synthetic_dataset_details)


# Code Cell from "7. First Pass: Identifying Data-Related Risks"
def add_risk_to_register(dimension, category, description, potential_impact="Medium", likelihood="Medium"):
    # Ensure all maps are defined in the function scope or are accessible globally in Streamlit script
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
    st.session_state.risk_register_df = pd.concat([st.session_state.risk_register_df, pd.DataFrame([new_risk])], ignore_index=True)
    st.session_state.next_risk_id += 1
    st.success(f"Risk {new_risk['Risk ID']} added successfully!")


# Code Cell from "12. Assessing Risk Severity: Impact and Likelihood Scoring"
def assess_risk_severity(risk_id, potential_impact, likelihood):
    impact_map = {"Low": 1, "Medium": 2, "High": 3}
    likelihood_map = {"Low": 1, "Medium": 2, "High": 3}

    idx = st.session_state.risk_register_df[st.session_state.risk_register_df["Risk ID"] == risk_id].index
    if not idx.empty:
        idx = idx[0]
        st.session_state.risk_register_df.loc[idx, "Potential Impact"] = potential_impact
        st.session_state.risk_register_df.loc[idx, "Likelihood"] = likelihood
        
        impact_score = impact_map.get(potential_impact, 0)
        likelihood_score = likelihood_map.get(likelihood, 0)
        st.session_state.risk_register_df.loc[idx, "Risk Score"] = impact_score * likelihood_score
        st.session_state.risk_register_df.loc[idx, "Status"] = "Assessed"
        st.success(f"Risk {risk_id} updated with Impact: {potential_impact}, Likelihood: {likelihood}, Score: {impact_score * likelihood_score}")
    else:
        st.error(f"Risk ID {risk_id} not found.")


# Code Cell from "13. Visualizing the Risk Landscape: The AI Risk Matrix"
def plot_risk_matrix(risk_df):
    impact_order = ["Low", "Medium", "High"]
    likelihood_order = ["Low", "Medium", "High"]
    
    risk_df_plot = risk_df.copy()
    # Filter out risks that haven't been assessed (Risk Score 0 if not assessed properly)
    risk_df_plot = risk_df_plot[risk_df_plot['Risk Score'] > 0] 

    if risk_df_plot.empty:
        st.info("No assessed risks to display in the matrix yet. Please assess some risks first.")
        return

    # Map qualitative ratings to numerical for plotting
    risk_df_plot["Impact_Num"] = risk_df_plot["Potential Impact"].map(lambda x: impact_order.index(x) + 0.5)
    risk_df_plot["Likelihood_Num"] = risk_df_plot["Likelihood"].map(lambda x: likelihood_order.index(x) + 0.5)

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
    ax.axvspan(2, 3, ymin=2/3, ymax=1, color='red', alpha=0.15, label='High Risk')
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
    ax.axvspan(0, 1, ymin=0, ymax=1/3, color='lightgreen', alpha=0.15, label='Low Risk')


    ax.set_xticks([0.5, 1.5, 2.5])
    ax.set_xticklabels(likelihood_order)
    ax.set_yticks([0.5, 1.5, 2.5])
    ax.set_yticklabels(impact_order)
    ax.set_xlabel("Likelihood")
    ax.set_ylabel("Potential Impact")
    ax.set_title("AI Model Risk Matrix: Credit Risk Scoring Model")
    
    # Annotate points with Risk ID
    for i, row in risk_df_plot.iterrows():
        ax.annotate(row["Risk ID"], (row["Likelihood_Num"] + 0.1, row["Impact_Num"] + 0.1), fontsize=8)

    ax.grid(False) # Remove default grid to avoid overlap with custom lines
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    st.pyplot(fig)


# Code Cell from "14. Strategic Risk Mitigation: Developing Controls"
def add_mitigation_strategy(risk_id, strategy_description, responsible_party):
    idx = st.session_state.risk_register_df[st.session_state.risk_register_df["Risk ID"] == risk_id].index
    if not idx.empty:
        idx = idx[0]
        st.session_state.risk_register_df.loc[idx, "Mitigation Strategy"] = strategy_description
        st.session_state.risk_register_df.loc[idx, "Responsible Party"] = responsible_party
        st.session_state.risk_register_df.loc[idx, "Status"] = "Mitigation Proposed"
        st.success(f"Mitigation strategy added for Risk {risk_id}.")
    else:
        st.error(f"Risk ID {risk_id} not found.")


# Code Cell from "15. Consolidating Findings: Populating the AI Risk Register"
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
    sns.barplot(x=risk_counts_by_dimension.index, y=risk_counts_by_dimension.values, palette='viridis', ax=ax)
    ax.set_title('Distribution of Identified Risks Across AI Dimensions')
    ax.set_xlabel('AI Risk Dimension')
    ax.set_ylabel('Number of Risks')
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

```

**Mapping Markdown and Code to Streamlit Pages (Conceptual, within main Streamlit script logic):**

**Page 1: Welcome & Scenario Setup**

```python
if st.session_state.current_page == 1:
    st.title("AI Model Risk Assessment: Credit Risk Scoring Model")
    st.markdown("""
    # 1. Setting the Scene: The Critical Role of an AI Risk Manager

    As a Quantitative Analyst at QuantBank, your primary responsibility is to ensure the integrity and compliance of all models used in critical financial decisions. Today, you've been tasked with a formal risk assessment of a newly developed AI-powered Credit Risk Scoring Model. This model, if deployed, will automate loan approval processes and flag high-risk applicants for manual review. Your assessment is crucial for compliance with regulatory standards like SR 11-7 and internal governance policies.

    The core principle guiding this assessment is the understanding that risk is a function of potential impact and likelihood. In quantitative terms, this can be expressed as:

    $$
    Risk = Impact \\times Likelihood
    $$

    Where *Impact* refers to the severity of adverse outcomes (e.g., financial loss, reputational damage, regulatory penalties), and *Likelihood* refers to the probability of the adverse event occurring. Your job is to systematically identify potential failure points and quantify these two dimensions for the AI model.
    """)
    if st.button("Start Assessment"):
        next_page()
```

**Page 2: Model Overview & Card**

```python
elif st.session_state.current_page == 2:
    st.header("2. Understanding the Credit Risk AI Model")
    st.markdown("---")
    st.markdown("""
    Before diving into risk identification, you need to thoroughly understand the AI model itself. This involves grasping its fundamental purpose, the algorithm it uses, and its intended operational environment. For the new Credit Risk Scoring Model, you've gathered initial details from the development team. This foundational understanding is the first step in applying frameworks like SR 11-7 and NIST AI RMF, ensuring you assess the right "model" in its specific context.
    """)
    st.subheader("Hypothetical AI Model Scenario Details:")
    for key, value in st.session_state.credit_risk_model_scenario.items():
        st.markdown(f"- **{key}**: {value}")

    st.markdown("""
    The output above provides a clear, concise overview of the AI model. For a Risk Manager, this information is critical for establishing the scope of the assessment and understanding the model's direct impact on business operations and potential regulatory exposure. It immediately highlights that this is a high-stakes model impacting customer finances.
    """)

    st.markdown("---")
    st.header("3. Constructing the AI Model Card: Transparency & Key Facts")
    st.markdown("""
    To ensure transparency and facilitate effective challenge, you need to create an 'AI Model Card' for the Credit Risk Scoring Model. This artifact, inspired by best practices in AI assurance, summarizes crucial information about the model, including its purpose, performance metrics, and known limitations. This proactive documentation is vital for internal stakeholders and external auditors, enhancing accountability and reducing information asymmetry, directly supporting SR 11-7's emphasis on validation and governance.
    """)
    st.subheader("AI Model Card: Credit Risk Scoring Model")
    for key, value in st.session_state.credit_risk_model_card.items():
        if isinstance(value, dict) or isinstance(value, list):
            st.markdown(f"- **{key}**:")
            for item in value:
                if isinstance(item, dict):
                    st.markdown(f"  - {item.keys()}: {item.values()}")
                else:
                    st.markdown(f"  - {item}")
        else:
            st.markdown(f"- **{key}**: {value}")
    st.markdown("""
    The generated Model Card provides a structured summary. As a Risk Manager, you immediately see the model's purpose, algorithm, and crucial performance indicators (AUC: 0.85, Precision@90%Recall: 0.60). Importantly, the "Known Limitations" section proactively highlights areas of concern like potential bias and performance degradation, which will be central to your risk identification process. This artifact serves as a single source of truth for the model's core information.
    """)
    st.markdown("---")
    st.columns([1, 1, 1])[1].button("Next: Data Card", on_click=next_page)
    st.columns([1, 1, 1])[0].button("Previous Step", on_click=prev_page)
```

**Page 3: Data Overview & Card**

```python
elif st.session_state.current_page == 3:
    st.header("3. Dissecting the Data for the Credit Risk Model")
    st.markdown("---")
    st.markdown("""
    The quality and characteristics of the training data are paramount to an AI model's performance and fairness. As a Quantitative Analyst, you understand that "garbage in, garbage out" applies rigorously to AI. You need to document the synthetic dataset used to train the Credit Risk Scoring Model. This 'Data Card' will detail its provenance, features, and crucially, any identified biases or quality issues. This directly addresses the "Data" dimension of AI risk, as highlighted by NIST AI RMF and SR 11-7's emphasis on data quality in model validation.
    """)
    st.subheader("Data Card: Credit Application Data")
    for key, value in st.session_state.credit_data_card.items():
        if isinstance(value, dict) or isinstance(value, list):
            st.markdown(f"- **{key}**:")
            for item in value:
                if isinstance(item, dict):
                    st.markdown(f"  - {item.keys()}: {item.values()}")
                else:
                    st.markdown(f"  - {item}")
        else:
            st.markdown(f"- **{key}**: {value}")
    st.markdown("""
    The Data Card clearly outlines the dataset's characteristics and, critically, highlights potential biases and data quality issues. As a Risk Manager, you note the "Historical lending bias" and "Underrepresentation" as immediate red flags for fairness, while "Missing Data" and "CreditScore Lag" point to accuracy and reliability concerns. This information directly informs the data-related risks you'll formally document in the risk register.
    """)
    st.markdown("---")
    st.columns([1, 1, 1])[1].button("Next: AI Risk Frameworks", on_click=next_page)
    st.columns([1, 1, 1])[0].button("Previous Step", on_click=prev_page)
```

**Page 4: AI Risk Frameworks**

```python
elif st.session_state.current_page == 4:
    st.header("4. Foundations: SR 11-7 & NIST AI RMF 1.0")
    st.markdown("---")
    st.markdown("""
    ## 5. Foundations of Financial Model Risk: SR 11-7 in an AI Context

    As a Quantitative Analyst in a financial institution, SR 11-7 (Supervisory Guidance on Model Risk Management) is your bedrock for model governance. While it predates modern AI, its core principles of Model Risk Management (MRM) remain highly relevant. You must consider how SR 11-7's pillars—model development, implementation, validation, and governance—translate to AI systems. This conceptual mapping ensures that even novel AI models are subject to the same rigor and oversight as traditional financial models, especially concerning "effective challenge" and sound governance.

    The definition of model risk under SR 11-7 is broad and encompasses the potential for adverse consequences from decisions based on incorrect or misused model outputs. This includes financial loss, reputational damage, and flawed decisions. The guidance emphasizes that model risk intensifies with greater model complexity, higher input uncertainty, broader extent of use, and larger potential impact. These considerations are particularly amplified with AI models due to their opacity and emergent behaviors.
    """)
    st.info("As a Quant Analyst, SR 11-7 is your bedrock for model governance. Remember: model risk intensifies with complexity, input uncertainty, and broader use.")
    
    st.markdown("---")
    st.markdown("""
    ## 6. Embracing Trustworthy AI: The NIST AI RMF 1.0 Framework

    Beyond SR 11-7's financial focus, the NIST AI Risk Management Framework (AI RMF 1.0) provides a broader, cross-sector lens for managing AI risks and promoting trustworthy AI. As an AI Risk Manager, you recognize the need to integrate these principles, which encompass attributes like validity, reliability, safety, security, transparency, fairness, accountability, and privacy-preserving. This framework complements SR 11-7 by offering a structured approach to identifying, measuring, and managing the unique risks posed by AI systems across their entire lifecycle. You will leverage its taxonomy and attributes to ensure a comprehensive risk assessment.

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
    
    st.markdown("---")
    st.columns([1, 1, 1])[1].button("Next: Identify AI Risks", on_click=next_page)
    st.columns([1, 1, 1])[0].button("Previous Step", on_click=prev_page)
```

**Page 5: AI Risk Register - Identify Risks**

```python
elif st.session_state.current_page == 5:
    st.header("5. AI Risk Register: Systematic Identification")
    st.markdown("---")
    st.markdown("""
    Now equipped with the model and data cards, and frameworks like SR 11-7 and NIST AI RMF, you begin the systematic identification of risks. You'll work through the five dimensions of the AI Risk Taxonomy: Data, Model, System, Human, and Organizational.
    """)

    # Pre-populate button logic
    if st.button("Pre-populate Initial Risks", key="prepopulate_risks_btn"):
        add_risk_to_register(dimension="Data", category="Data Quality", description="Inconsistent or missing data in 'EmploymentStatus' could lead to inaccurate risk assessments, violating Validity.")
        add_risk_to_register(dimension="Data", category="Data Bias", description="Historical bias in income data from specific 'ResidentialStatus' groups could lead to unfair decisions for future applicants, violating Fairness.")
        add_risk_to_register(dimension="Data", category="Data Provenance & Relevance", description="CreditScore data from an older system, updated quarterly, may not reflect real-time creditworthiness, impacting model Reliability and Validity.")
        add_risk_to_register(dimension="Data", category="Data Privacy", description="Potential exposure of sensitive demographic data if access controls are insufficient, violating Privacy-Preserving.")
        add_risk_to_register(dimension="Model", category="Algorithmic Bias & Fairness", description="The Gradient Boosting Classifier's complex decision boundaries might amplify subtle biases present in training data, leading to disparate impact on underrepresented groups, violating Fairness.")
        add_risk_to_register(dimension="Model", category="Accuracy & Reliability", description="Model performance (Precision@90%Recall: 0.60) might be insufficient for high-stakes decisions, leading to higher false negatives (approving defaulters), violating Validity and Reliability.")
        add_risk_to_register(dimension="Model", category="Model Robustness", description="Model performance may degrade significantly with concept drift due to changing economic conditions (e.g., recession), leading to unstable predictions, violating Reliability.")
        add_risk_to_register(dimension="Model", category="Interpretability", description="The black-box nature of Gradient Boosting makes it difficult to explain individual loan decisions to applicants or regulators, impacting Transparency and Accountability.")
        add_risk_to_register(dimension="System", category="Integration Flaws", description="API integration into the legacy Loan Origination System might introduce latency or data corruption, leading to incorrect or delayed decisions, violating Validity and Safety.")
        add_risk_to_register(dimension="System", category="AI Supply Chain Vulnerabilities", description="Reliance on open-source libraries (e.g., LightGBM) without thorough internal vetting could introduce security vulnerabilities or unpatched bugs, violating Security.")
        add_risk_to_register(dimension="System", category="Scalability & Performance", description="The current deployment infrastructure may not handle peak load volumes for real-time predictions, leading to system outages or degraded service, violating Reliability.")
        add_risk_to_register(dimension="Human", category="Misuse & Misinterpretation", description="Loan officers might misinterpret model outputs or explanations, leading to incorrect manual overrides or decisions, violating Transparency and Accountability.")
        add_risk_to_register(dimension="Human", category="Over-Reliance & Autonomy Creep", description="Over-reliance on automated 'Approve' decisions could lead to a decline in human critical judgment, increasing undetected errors or biases, violating Accountability.")
        add_risk_to_register(dimension="Human", category="Loss of Human Oversight", description="Lack of a clear 'human-in-the-loop' process for edge cases or flagged applications could lead to the model making autonomous, unreviewed decisions with adverse outcomes, violating Safety and Accountability.")
        add_risk_to_register(dimension="Organizational", category="Robust Governance & Oversight", description="Absence of a dedicated AI Ethics Committee or clear roles for AI risk oversight beyond traditional MRM could lead to unaddressed ethical concerns, violating Accountability.")
        add_risk_to_register(dimension="Organizational", category="Policy & Ethical Guidelines", description="Lack of a comprehensive incident response plan for AI model failures (e.g., severe drift, bias detection) could delay remediation and amplify negative impact, violating Safety and Accountability.")
        add_risk_to_register(dimension="Organizational", category="Responsible AI Culture", description="Insufficient training or awareness programs for employees on responsible AI use and emergent risks could lead to poor operational practices, violating Accountability.")

    st.subheader("Current AI Risk Register")
    if not st.session_state.risk_register_df.empty:
        st.dataframe(st.session_state.risk_register_df.sort_values(by="Risk ID"))
    else:
        st.info("No risks identified yet. Use the 'Pre-populate Initial Risks' button or 'Manually Add a New Risk' section below.")

    st.markdown("---")
    with st.expander("Manually Add a New Risk"):
        st.markdown("As a Risk Manager, you identify a unique risk based on your expert judgment.")
        new_dimension = st.selectbox("Dimension", options=["Data", "Model", "System", "Human", "Organizational"], key="new_risk_dim")
        new_category = st.text_input("Category", help="e.g., Data Quality, Algorithmic Bias", key="new_risk_cat")
        new_description = st.text_area("Description", help="Detailed description of the risk, including how it might impact the model or business.", key="new_risk_desc")
        new_impact = st.selectbox("Potential Impact", options=["Low", "Medium", "High"], index=1, key="new_risk_impact")
        new_likelihood = st.selectbox("Likelihood", options=["Low", "Medium", "High"], index=1, key="new_risk_likelihood")
        if st.button("Add Risk", key="add_new_risk_btn"):
            if new_description:
                add_risk_to_register(new_dimension, new_category, new_description, new_impact, new_likelihood)
            else:
                st.warning("Please provide a description for the new risk.")
    
    st.markdown("---")
    st.columns([1, 1, 1])[1].button("Next: Assess Risk Severity", on_click=next_page)
    st.columns([1, 1, 1])[0].button("Previous Step", on_click=prev_page)
```

**Page 6: AI Risk Register - Assess Risk Severity**

```python
elif st.session_state.current_page == 6:
    st.header("6. AI Risk Register: Severity Assessment")
    st.markdown("---")
    st.markdown("""
    With all risks identified, your next step as a Risk Manager is to assess their severity. You'll use a qualitative scoring system for "Potential Impact" and "Likelihood," typically rated as Low, Medium, or High. This allows you to prioritize risks, focusing mitigation efforts on those with the highest scores. This process directly applies the fundamental risk formula ($Risk = Impact \\times Likelihood$) and prepares for detailed discussion with stakeholders on critical risks.
    """)

    if st.button("Auto-Assess Key Risks", key="auto_assess_btn"):
        assess_risk_severity("R002", "High", "Medium")  # Historical data bias
        assess_risk_severity("R003", "Medium", "High") # CreditScore Lag
        assess_risk_severity("R004", "Medium", "Medium") # Data Privacy
        assess_risk_severity("R005", "High", "Medium")  # Algorithmic Bias
        assess_risk_severity("R006", "Medium", "Low")   # Accuracy & Reliability
        assess_risk_severity("R007", "High", "High")    # Model Robustness (concept drift)
        assess_risk_severity("R008", "Medium", "High")  # Interpretability
        assess_risk_severity("R009", "Medium", "Medium") # Integration Flaws
        assess_risk_severity("R010", "High", "Low")    # AI Supply Chain Vulnerabilities
        assess_risk_severity("R011", "Medium", "Medium") # Scalability & Performance
        assess_risk_severity("R012", "Medium", "High") # Misuse & Misinterpretation
        assess_risk_severity("R013", "High", "Medium") # Over-Reliance & Autonomy Creep
        assess_risk_severity("R014", "High", "High")  # Loss of Human Oversight
        assess_risk_severity("R015", "High", "Medium") # Absence of AI Ethics Committee
        assess_risk_severity("R016", "High", "High")  # Lack of Incident Response Plan
        assess_risk_severity("R017", "Medium", "Medium") # Insufficient training
    
    st.subheader("AI Risk Register with Assessed Risks (Sorted by Score)")
    if not st.session_state.risk_register_df.empty:
        st.dataframe(st.session_state.risk_register_df.sort_values(by="Risk Score", ascending=False))
    else:
        st.info("No risks to assess yet. Please identify some risks first.")
    
    st.markdown("---")
    st.markdown("As a Risk Manager, you can refine the impact and likelihood for any risk based on your deeper analysis.")
    if not st.session_state.risk_register_df.empty:
        risk_ids = st.session_state.risk_register_df['Risk ID'].tolist()
        selected_risk_id = st.selectbox("Select Risk ID to Assess/Update", options=risk_ids, key="select_risk_id_assess")
        
        # Pre-fill current impact/likelihood if a risk is selected
        if selected_risk_id:
            current_risk = st.session_state.risk_register_df[st.session_state.risk_register_df['Risk ID'] == selected_risk_id].iloc[0]
            current_impact_idx = ["Low", "Medium", "High"].index(current_risk['Potential Impact'])
            current_likelihood_idx = ["Low", "Medium", "High"].index(current_risk['Likelihood'])

            new_impact = st.selectbox("Update Potential Impact", options=["Low", "Medium", "High"], index=current_impact_idx, key="update_impact")
            new_likelihood = st.selectbox("Update Likelihood", options=["Low", "Medium", "High"], index=current_likelihood_idx, key="update_likelihood")
            if st.button("Update Risk Severity"):
                assess_risk_severity(selected_risk_id, new_impact, new_likelihood)
    else:
        st.warning("Please add risks to the register first to enable assessment.")

    st.markdown("---")
    st.columns([1, 1, 1])[1].button("Next: Visualize Risk Landscape", on_click=next_page)
    st.columns([1, 1, 1])[0].button("Previous Step", on_click=prev_page)
```

**Page 7: AI Risk Matrix Visualization**

```python
elif st.session_state.current_page == 7:
    st.header("7. Visualizing the Risk Landscape: The AI Risk Matrix")
    st.markdown("---")
    st.markdown("""
    To effectively communicate the risk landscape to senior management and other stakeholders, a visual representation is essential. As a Risk Manager, you'll create a Risk Matrix, plotting each identified risk based on its assessed impact and likelihood. This visualization quickly highlights high-priority risks that fall into the "High Impact, High Likelihood" quadrant, enabling a clear and concise presentation for your upcoming 'Effective Challenge' meeting.
    """)
    if not st.session_state.risk_register_df.empty:
        plot_risk_matrix(st.session_state.risk_register_df)
        st.markdown("""
        The Risk Matrix visually groups risks, making it immediately clear which ones reside in the high-risk "red" zone (High Impact, High Likelihood). You can quickly point out risks like R007 ("Model Robustness"), R014 ("Loss of Human Oversight"), and R016 ("Lack of Incident Response Plan") as top priorities. This visual summary is an invaluable tool for driving discussions with non-technical stakeholders and securing resources for mitigation.
        """)
    else:
        st.info("No risks in the register to plot yet. Please go back to identify and assess some risks.")
    st.markdown("---")
    st.columns([1, 1, 1])[1].button("Next: Develop Mitigation Strategies", on_click=next_page)
    st.columns([1, 1, 1])[0].button("Previous Step", on_click=prev_page)
```

**Page 8: AI Risk Register - Mitigation Strategies**

```python
elif st.session_state.current_page == 8:
    st.header("8. AI Risk Register: Strategic Mitigation")
    st.markdown("---")
    st.markdown("""
    Identifying and assessing risks is only half the battle. As a Risk Manager, your next critical step is to propose concrete mitigation strategies and controls for the highest-priority risks. These strategies should align with NIST AI RMF's emphasis on control measures and SR 11-7's requirement for robust validation and governance. For example, for model bias, a mitigation could involve fairness audits and re-training with debiased data. For human oversight, it might involve "human-in-the-loop" mechanisms.
    """)

    if st.button("Auto-Populate Mitigations for Top Risks", key="auto_mitigate_btn"):
        add_mitigation_strategy("R007", "Implement continuous monitoring for concept drift (e.g., population stability index) with quarterly model re-calibration or re-training. Develop a champion-challenger framework.", "Model Monitoring Team")
        add_mitigation_strategy("R014", "Establish clear 'human-in-the-loop' checkpoints for all high-value loan decisions and edge cases. Mandate model explanation training for loan officers.", "Operations & Compliance")
        add_mitigation_strategy("R016", "Develop and socialize a comprehensive AI model incident response plan, including clear communication protocols, rollback procedures, and stakeholder notification processes.", "Risk Management & IT Operations")
        add_mitigation_strategy("R002", "Conduct regular fairness audits across protected groups. Explore data augmentation or re-sampling techniques to debias training data. Implement post-processing bias mitigation techniques.", "Data Science & AI Ethics Committee")
        add_mitigation_strategy("R005", "Implement disparate impact testing during model validation. Use fairness-aware training algorithms or re-weighing techniques. Document fairness metrics in model card.", "Model Validation & Data Science")
        add_mitigation_strategy("R015", "Propose the formation of a cross-functional AI Ethics Committee to guide policy, review high-risk models, and provide an 'effective challenge' on ethical considerations.", "Senior Management & Governance")
    
    st.subheader("AI Risk Register with Proposed Mitigations (Top Risks)")
    if not st.session_state.risk_register_df.empty:
        st.dataframe(st.session_state.risk_register_df.sort_values(by="Risk Score", ascending=False))
    else:
        st.info("No risks with mitigations yet. Please identify and assess risks first.")
    
    st.markdown("---")
    st.markdown("As a Risk Manager, you can add or update mitigation strategies for individual risks.")
    if not st.session_state.risk_register_df.empty:
        risk_ids = st.session_state.risk_register_df['Risk ID'].tolist()
        selected_risk_id_mitigate = st.selectbox("Select Risk ID to Add/Update Mitigation", options=risk_ids, key="select_risk_id_mitigate")
        
        # Pre-fill current mitigation/party if a risk is selected
        if selected_risk_id_mitigate:
            current_mitigation = st.session_state.risk_register_df[st.session_state.risk_register_df['Risk ID'] == selected_risk_id_mitigate].iloc[0]
            current_strategy = current_mitigation['Mitigation Strategy'] if current_mitigation['Mitigation Strategy'] != "To be determined" else ""
            current_party = current_mitigation['Responsible Party'] if current_mitigation['Responsible Party'] != "TBD" else ""

            new_strategy = st.text_area("Mitigation Strategy Description", value=current_strategy, height=100, key="new_strategy")
            new_party = st.text_input("Responsible Party", value=current_party, help="e.g., Data Science Team, Compliance Department", key="new_party")
            if st.button("Add/Update Mitigation Strategy"):
                add_mitigation_strategy(selected_risk_id_mitigate, new_strategy, new_party)
    else:
        st.warning("Please add risks to the register first to enable mitigation planning.")

    st.markdown("---")
    st.columns([1, 1, 1])[1].button("Next: Generate Final Report", on_click=next_page)
    st.columns([1, 1, 1])[0].button("Previous Step", on_click=prev_page)
```

**Page 9: Final AI Risk Report**

```python
elif st.session_state.current_page == 9:
    st.header("9. Comprehensive AI Risk Report")
    st.markdown("---")
    st.markdown("""
    The ultimate deliverable of your assessment is a comprehensive AI Risk Register. This living document consolidates all identified risks, their assessment (impact, likelihood, score), and the proposed mitigation strategies. As a Risk Manager, you understand that this register is crucial for ongoing monitoring, auditability, and demonstrating compliance. It serves as the single source of truth for the AI model's risk profile, empowering the organization to manage it effectively throughout its lifecycle.
    """)
    st.subheader("Comprehensive AI Model Risk Register: Credit Risk Scoring Model")
    final_ai_risk_register = generate_risk_register_report(st.session_state.risk_register_df)
    st.dataframe(final_ai_risk_register)

    st.markdown("---")
    st.subheader("Risk Distribution Across AI Dimensions")
    plot_risk_distribution(final_ai_risk_register)
    st.markdown("""
    The generated table represents the complete AI Risk Register, a critical deliverable. It provides a clear, sortable overview of all identified and assessed risks, along with their proposed mitigation strategies and responsible parties. The bar chart further aids in understanding the overall risk exposure, quickly showing which dimensions (e.g., Model, Data, Human) have the highest number of identified risks. This document is now ready for presentation, audit, and ongoing management, fulfilling a core requirement of both SR 11-7 and NIST AI RMF.
    """)

    st.markdown("---")
    st.markdown("""
    ## 16. Concluding the Assessment: Preparing for Effective Challenge

    As a Quantitative Analyst, your detailed AI Risk Register and associated artifacts (Model Card, Data Card) form the basis for the "Effective Challenge" process. This principle, central to SR 11-7, mandates that objective and informed reviewers critically test models to identify hidden errors, biases, or limitations. By systematically identifying risks, assessing their impact, and proposing mitigations, you've provided the necessary documentation for internal validation teams, auditors, and senior management to rigorously scrutinize the Credit Risk Scoring Model. Your work ensures that QuantBank can deploy AI models with confidence, upholding regulatory compliance and fostering trustworthiness in AI. This iterative process of identification, assessment, mitigation, and challenge is crucial for continuous improvement and adaptive governance in AI risk management.
    """)
    st.markdown("---")
    st.button("Restart Assessment", on_click=lambda: set_page(1))
```


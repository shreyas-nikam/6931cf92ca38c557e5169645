id: 6931cf92ca38c557e5169645_documentation
summary: Lab 1: Principles of AI Risk and Assurance - Clone Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Building an AI Model Risk Management & Assurance Platform with Streamlit

## 1. Introduction to AI Risk Management and Application Overview
Duration: 0:10

<aside class="positive">
This step provides essential context for the application. Understanding the foundational concepts and the application's overall purpose will greatly enhance your learning experience.
</aside>

The rapid adoption of Artificial Intelligence (AI) models, particularly in high-stakes regulated environments like financial institutions, introduces unique and complex risks. Managing these risks is paramount for ensuring responsible AI deployment, maintaining public trust, and complying with evolving regulatory landscapes. This Streamlit application, **"AI Model Risk Register & Mitigation Planner"**, serves as a practical guide and interactive tool for identifying, assessing, mitigating, and monitoring AI-specific risks.

The application integrates key principles from two foundational frameworks:
*   **SR 11-7 (2011)**: The U.S. Federal Reserve's guidance on Model Risk Management, focusing on effective challenge, robust governance, and comprehensive validation for models in financial institutions.
*   **NIST AI Risk Management Framework (AI RMF 1.0, 2023)**: A voluntary framework promoting trustworthy AI by outlining four core functions: **Govern, Map, Measure, and Manage**. It emphasizes attributes like validity, reliability, safety, security, transparency, fairness, accountability, and privacy-preservation.

### Importance and Learning Objectives

This codelab will walk you through an application designed to equip **Risk Managers, Financial Data Engineers, AI Ethicists, and Model Validators** with the tools and understanding necessary for effective AI risk management. Upon completion, you will be able to:
*   Implement a structured **AI Risk Taxonomy** categorizing risks into Data, Model, System, Human, and Organizational dimensions.
*   Perform conceptual assessment of risk likelihood and impact to derive a priority score.
*   Map mitigation strategies to NIST AI RMF functions and SR 11-7 pillars.
*   Track the status of mitigation efforts over time.
*   Understand the role of AI assurance artifacts like Model Cards and Data Cards.
*   Grasp foundational principles of AI risk and assurance relevant to generative AI and agentic systems.

### AI Risk Taxonomy

A systematic classification of AI risks is crucial. Our application utilizes a five-dimensional taxonomy:
1.  **Data Risks**: Quality, provenance, relevance, and privacy of data. (e.g., Data drift, biased training data, privacy breaches).
2.  **Model Risks**: Design, performance, and interpretability of the AI model. (e.g., Algorithmic bias, low accuracy, hallucinations in LLMs).
3.  **System Risks**: Integration, architecture, and security of the AI system within broader IT infrastructure. (e.g., Integration flaws, API security issues).
4.  **Human Risks**: Human interaction with AI, including misuse, over-reliance, and oversight challenges. (e.g., Misinterpretation of AI outputs, autonomy creep).
5.  **Organizational Risks**: Governance, policy, and cultural factors within the organization. (e.g., Lack of clear AI governance, insufficient ethical guidelines).

### Application Architecture

The application is built using Streamlit, providing an interactive web interface. It follows a multi-page structure, managed by `app.py`, which serves as the entry point and orchestrator. Core functionalities are encapsulated in utility functions within `app.py`, while user interface and page-specific logic reside in separate files under the `application_pages/` directory.

The application's architecture can be visualized as:

```
+-+
|     app.py     |
| (Main App Logic|
|  & Orchestrator)|
+-+--+
        |
        |  Loads & Manages
        |  `st.session_state.ai_risk_register_df`
        v
+--+
| Streamlit Session State |
| (DataFrame: AI Risk   |
|  Register)            |
+-+--+
        |
        |  Routes to
        |  (Sidebar Navigation)
        v
+-+
|              application_pages/                             |
| +--+   +--+  ...  +-+ |
| |   home.py       |   | ai_risk_register.py|        | risk_report.py | |
| | (Introduction)  |   | (CRUD Operations)  |        | (Report Gen)   | |
| +--+   +--+  ...  +-+ |
|                                                             |
|   ++   +--+          |
|   | risk_dashboard.py|   | assurance_artifacts.py|          |
|   | (Visualizations) |   | (Conceptual Docs)     |          |
|   ++   +--+-+
```

Data persistence within the application session is handled by Streamlit's `st.session_state`, which stores the main `ai_risk_register_df` DataFrame. This means data will be reset if the application is restarted.

## 2. Setting Up the Development Environment
Duration: 0:05

To run this Streamlit application, you'll need Python installed, along with several libraries.

### Prerequisites

*   Python 3.8+
*   `pip` (Python package installer)

### Installation

1.  **Create a virtual environment (recommended):**
    ```console
    python -m venv ai_risk_env
    source ai_risk_env/bin/activate  # On Windows: ai_risk_env\Scripts\activate
    ```
2.  **Install the required Python packages:**
    The application uses `streamlit`, `pandas`, `numpy`, `matplotlib`, `seaborn`, `faker`, and `plotly`. You can install them using pip:
    ```console
    pip install streamlit pandas numpy matplotlib seaborn Faker plotly
    ```

3.  **Organize the project files:**
    Ensure your files are structured as follows:
    ```
    .
    ├── app.py
    └── application_pages/
        ├── __init__.py  # (Optional, but good practice for packages)
        ├── home.py
        ├── ai_risk_register.py
        ├── risk_dashboard.py
        ├── assurance_artifacts.py
        └── risk_report.py
    ```
    Place the provided code snippets into their respective files.

### Running the Application

Navigate to the root directory of your project (where `app.py` is located) in your terminal and run:

```console
streamlit run app.py
```

This command will open the application in your default web browser, usually at `http://localhost:8501`.

## 3. Core AI Risk Management Logic and Data Model
Duration: 0:15

The heart of this application lies in its data model—the AI Risk Register DataFrame—and the utility functions that interact with it. All core data manipulation and calculation functions are defined in `app.py` and are accessible to the individual pages via `st.session_state` and direct imports.

### The AI Risk Register DataFrame

The central data store for all AI risks is a Pandas DataFrame, initialized in `app.py` and stored in Streamlit's session state to maintain its content across user interactions.

```python
# app.py
# Initialize session state for the DataFrame if it doesn't exist
if 'ai_risk_register_df' not in st.session_state:
    st.session_state.ai_risk_register_df = pd.DataFrame(columns=[
        "Risk_ID", "Risk_Description", "Risk_Category", "Likelihood", "Impact",
        "Mitigation_Controls", "Response_Plan", "NIST_AI_RMF_Function",
        "SR_11_7_Pillar", "Responsible_Party", "Status", "Risk_Priority_Score"
    ]) # Start with an empty DataFrame with all columns
```
This DataFrame holds all the details of each identified AI risk, including its category, assessed likelihood and impact, mitigation strategies, responsible parties, and current status.

### `generate_synthetic_risk_data(num_risks)`

This function creates a DataFrame with `num_risks` randomly generated AI risk entries. It uses the `Faker` library to produce realistic-looking descriptions, names, and scenarios across the defined risk categories and framework mappings. This is crucial for demonstrating the application's functionalities without requiring real-world sensitive data.

```python
# app.py
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
```

### `calculate_risk_priority_score(df_register)`

This function quantifies risk severity by calculating a `Risk_Priority_Score`. It maps qualitative `Likelihood` and `Impact` ratings ("Low", "Medium", "High") to numerical values (1, 2, 3) and then multiplies them. This allows for clear prioritization of risks.

The scoring matrix is as follows:
$$
\begin{pmatrix}
\textbf{Likelihood} / \textbf{Impact} & \textbf{Low (1)} & \textbf{Medium (2)} & \textbf{High (3)} \\
\textbf{Low (1)} & 1 & 2 & 3 \\
\textbf{Medium (2)} & 2 & 4 & 6 \\
\textbf{High (3)} & 3 & 6 & 9
\end{pmatrix}
$$

The formula for the score ($S$) is:
$$
S = \text{Likelihood}_{\text{numeric}} \times \text{Impact}_{\text{numeric}}
$$

```python
# app.py
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
```

### `update_risk_status(df_register, risk_id, new_status)`

This function updates the `Status` of a specific risk identified by its `Risk_ID`. This is a crucial feature for tracking the progress of mitigation efforts.

```python
# app.py
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
```

### `generate_risk_report(df_register)`

This function compiles a comprehensive summary report of the AI Risk Register, formatted in Markdown. It includes summaries by category, priority, status, top risks, and adherence to NIST AI RMF and SR 11-7 frameworks. This is essential for communicating the risk posture to stakeholders.

```python
# app.py
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
```

## 4. Interacting with the AI Risk Register
Duration: 0:20

The `application_pages/ai_risk_register.py` module provides the core CRUD (Create, Read, Update, Delete - though Delete is not implemented) functionality for managing the AI Model Risk Register. This is where users can directly interact with the risk data.

<aside class="negative">
Remember that the data in `st.session_state.ai_risk_register_df` is not persistent across application restarts. Any changes made will be lost if you close and reopen the Streamlit app. For real-world applications, you would integrate a database.
</aside>

### Generating Synthetic Data

To populate the register quickly, you can generate a configurable number of synthetic risks. This uses the `generate_synthetic_risk_data` function from `app.py`.

```python
# application_pages/ai_risk_register.py
def main():
    st.header("AI Risk Register")
    st.markdown("This section allows you to interact with the AI Risk Register. You can generate synthetic data, add new risks, edit existing ones, and update their statuses.")

    # Data Generation Section
    with st.expander("Generate Synthetic Data"):
        num_risks_input = st.number_input("Number of risks to generate", min_value=1, value=30, key="num_risks_gen")
        if st.button("Generate Synthetic Data", key="generate_data_button"):
            # Access functions from the parent scope (app.py)
            from app import generate_synthetic_risk_data, calculate_risk_priority_score
            
            new_synthetic_df = generate_synthetic_risk_data(int(num_risks_input))
            # Concatenate with existing data to avoid overwriting if user generates multiple times
            if not st.session_state.ai_risk_register_df.empty:
                # Ensure new_synthetic_df Risk_IDs don't clash with existing ones
                max_existing_id = st.session_state.ai_risk_register_df["Risk_ID"].max()
                new_synthetic_df["Risk_ID"] = new_synthetic_df["Risk_ID"] + max_existing_id
                
            st.session_state.ai_risk_register_df = pd.concat([st.session_state.ai_risk_register_df, new_synthetic_df], ignore_index=True)
            st.session_state.ai_risk_register_df["Risk_Priority_Score"] = calculate_risk_priority_score(st.session_state.ai_risk_register_df)
            st.success(f"{num_risks_input} synthetic risks generated and added to the register.")
```

### Viewing the Current AI Risk Register

Once data is generated or added, it's displayed in an interactive Streamlit DataFrame.

```python
# application_pages/ai_risk_register.py
    st.subheader("Current AI Risk Register")
    if not st.session_state.ai_risk_register_df.empty:
        st.dataframe(st.session_state.ai_risk_register_df, use_container_width=True)
    else:
        st.info("The AI Risk Register is currently empty. Generate some synthetic data or add a new risk to get started.")
```

### Adding a New Risk Entry

Users can manually add new risks using a form. Each field corresponds to a column in the DataFrame, and the `Risk_Priority_Score` is automatically calculated upon submission.

```python
# application_pages/ai_risk_register.py
    # Add New Risk Entry
    st.subheader("Add New Risk Entry")
    with st.form("add_risk_form"):
        risk_description = st.text_input("Risk Description", key="add_risk_description")
        risk_category = st.selectbox("Risk Category", ["Data", "Model", "System", "Human", "Organizational"], key="add_risk_category_select")
        likelihood = st.selectbox("Likelihood", ["Low", "Medium", "High"], key="add_likelihood_select")
        impact = st.selectbox("Impact", ["Low", "Medium", "High"], key="add_impact_select")
        mitigation_controls = st.text_input("Mitigation Controls", key="add_mitigation_controls")
        response_plan = st.text_input("Response Plan", key="add_response_plan")
        nist_rmf_function = st.selectbox("NIST AI RMF Function", ["Govern", "Map", "Measure", "Manage"], key="add_nist_rmf_select")
        sr_11_7_pillar = st.selectbox("SR 11-7 Pillar", ["Development/Implementation", "Validation", "Governance", "Ongoing Monitoring"], key="add_sr117_pillar_select")
        responsible_party = st.text_input("Responsible Party", key="add_responsible_party")
        status = st.selectbox("Status", ["Identified", "In Progress", "Mitigated", "Monitored"], key="add_status_select")

        add_submitted = st.form_submit_button("Add New Risk")
        if add_submitted:
            if not risk_description or not mitigation_controls or not response_plan or not responsible_party:
                st.error("Please fill in all required fields for adding a new risk.")
            else:
                next_risk_id = (st.session_state.ai_risk_register_df["Risk_ID"].max() if not st.session_state.ai_risk_register_df.empty else 0) + 1
                new_risk = pd.DataFrame([{
                    "Risk_ID": next_risk_id,
                    "Risk_Description": risk_description,
                    "Risk_Category": risk_category,
                    "Likelihood": likelihood,
                    "Impact": impact,
                    "Mitigation_Controls": mitigation_controls,
                    "Response_Plan": response_plan,
                    "NIST_AI_RMF_Function": nist_rmf_function,
                    "SR_11_7_Pillar": sr_11_7_pillar,
                    "Responsible_Party": responsible_party,
                    "Status": status,
                    "Risk_Priority_Score": 0 # Temporary, will be calculated
                }])
                st.session_state.ai_risk_register_df = pd.concat([st.session_state.ai_risk_register_df, new_risk], ignore_index=True)
                # Recalculate score for the entire DataFrame or just the new row
                from app import calculate_risk_priority_score
                st.session_state.ai_risk_register_df["Risk_Priority_Score"] = calculate_risk_priority_score(st.session_state.ai_risk_register_df)
                st.success(f"Risk ID {next_risk_id} added successfully.")
```

### Editing an Existing Risk

Existing risks can be selected by their `Risk_ID` and edited through a pre-filled form. This allows for updating any detail of a risk as new information becomes available or as mitigation strategies evolve.

```python
# application_pages/ai_risk_register.py
    # Edit Existing Risk
    st.subheader("Edit Existing Risk")
    if not st.session_state.ai_risk_register_df.empty:
        risk_ids = st.session_state.ai_risk_register_df["Risk_ID"].unique().tolist()
        selected_risk_id_edit = st.selectbox("Select Risk ID to edit", risk_ids, key="edit_risk_id_select")

        if selected_risk_id_edit:
            selected_risk = st.session_state.ai_risk_register_df[st.session_state.ai_risk_register_df["Risk_ID"] == selected_risk_id_edit].iloc[0]

            with st.form("edit_risk_form"):
                edited_risk_description = st.text_input("Risk Description", value=selected_risk["Risk_Description"], key="edit_risk_description")
                edited_risk_category = st.selectbox("Risk Category", ["Data", "Model", "System", "Human", "Organizational"], index=["Data", "Model", "System", "Human", "Organizational"].index(selected_risk["Risk_Category"]), key="edit_risk_category_select")
                edited_likelihood = st.selectbox("Likelihood", ["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(selected_risk["Likelihood"]), key="edit_likelihood_select")
                edited_impact = st.selectbox("Impact", ["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(selected_risk["Impact"]), key="edit_impact_select")
                edited_mitigation_controls = st.text_input("Mitigation Controls", value=selected_risk["Mitigation_Controls"], key="edit_mitigation_controls")
                edited_response_plan = st.text_input("Response Plan", value=selected_risk["Response_Plan"], key="edit_response_plan")
                edited_nist_rmf_function = st.selectbox("NIST AI RMF Function", ["Govern", "Map", "Measure", "Manage"], index=["Govern", "Map", "Measure", "Manage"].index(selected_risk["NIST_AI_RMF_Function"]), key="edit_nist_rmf_select")
                edited_sr_11_7_pillar = st.selectbox("SR 11-7 Pillar", ["Development/Implementation", "Validation", "Governance", "Ongoing Monitoring"], index=["Development/Implementation", "Validation", "Governance", "Ongoing Monitoring"].index(selected_risk["SR_11_7_Pillar"]), key="edit_sr117_pillar_select")
                edited_responsible_party = st.text_input("Responsible Party", value=selected_risk["Responsible_Party"], key="edit_responsible_party")
                edited_status = st.selectbox("Status", ["Identified", "In Progress", "Mitigated", "Monitored"], index=["Identified", "In Progress", "Mitigated", "Monitored"].index(selected_risk["Status"]), key="edit_status_select")

                edit_submitted = st.form_submit_button("Save Edited Risk")
                if edit_submitted:
                    if not edited_risk_description or not edited_mitigation_controls or not edited_response_plan or not edited_responsible_party:
                        st.error("Please fill in all required fields for editing the risk.")
                    else:
                        idx = st.session_state.ai_risk_register_df[st.session_state.ai_risk_register_df["Risk_ID"] == selected_risk_id_edit].index[0]
                        st.session_state.ai_risk_register_df.loc[idx, "Risk_Description"] = edited_risk_description
                        st.session_state.ai_risk_register_df.loc[idx, "Risk_Category"] = edited_risk_category
                        st.session_state.ai_risk_register_df.loc[idx, "Likelihood"] = edited_likelihood
                        st.session_state.ai_risk_register_df.loc[idx, "Impact"] = edited_impact
                        st.session_state.ai_risk_register_df.loc[idx, "Mitigation_Controls"] = edited_mitigation_controls
                        st.session_state.ai_risk_register_df.loc[idx, "Response_Plan"] = edited_response_plan
                        st.session_state.ai_risk_register_df.loc[idx, "NIST_AI_RMF_Function"] = edited_nist_rmf_function
                        st.session_state.ai_risk_register_df.loc[idx, "SR_11_7_Pillar"] = edited_sr_11_7_pillar
                        st.session_state.ai_risk_register_df.loc[idx, "Responsible_Party"] = edited_responsible_party
                        st.session_state.ai_risk_register_df.loc[idx, "Status"] = edited_status
                        
                        from app import calculate_risk_priority_score
                        st.session_state.ai_risk_register_df["Risk_Priority_Score"] = calculate_risk_priority_score(st.session_state.ai_risk_register_df)
                        st.success(f"Risk ID {selected_risk_id_edit} updated successfully.")
        else:
            st.info("No risk selected for editing.")
    else:
        st.info("No risks available to edit.")
```

### Updating Risk Status

A dedicated section allows for quickly changing the status of a specific risk, leveraging the `update_risk_status` function.

```python
# application_pages/ai_risk_register.py
    # Update Risk Status
    st.subheader("Update Risk Status")
    if not st.session_state.ai_risk_register_df.empty:
        risk_ids_update = st.session_state.ai_risk_register_df["Risk_ID"].unique().tolist()
        selected_risk_id_update = st.selectbox("Select Risk ID to update status", risk_ids_update, key="update_risk_id_select")
        new_status_input = st.selectbox("New Status", ["Identified", "In Progress", "Mitigated", "Monitored"], key="update_status_select")

        if st.button("Update Risk Status", key="update_status_button"):
            if selected_risk_id_update:
                from app import update_risk_status
                st.session_state.ai_risk_register_df = update_risk_status(st.session_state.ai_risk_register_df.copy(), selected_risk_id_update, new_status_input)
            else:
                st.warning("Please select a Risk ID to update.")
    else:
        st.info("No risks available to update status.")
```

## 5. Visualizing Risk Insights with the Dashboard
Duration: 0:15

The `application_pages/risk_dashboard.py` module is dedicated to providing interactive visualizations of the AI Risk Register using `plotly.express`. These dashboards help risk managers quickly understand the distribution, priorities, and status of AI risks.

<aside class="positive">
Interactive dashboards are invaluable for stakeholders to grasp complex risk landscapes at a glance, identify trends, and prioritize actions.
</aside>

```python
# application_pages/risk_dashboard.py
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
```

### 1. Distribution of Risks by Category

This bar chart provides a clear overview of which AI risk dimensions (Data, Model, System, Human, Organizational) are most prevalent in the register.

```python
# application_pages/risk_dashboard.py
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
```

### 2. Likelihood vs. Impact Heatmap

This heatmap is a critical tool for visualizing the overall risk profile. It shows the concentration of risks based on their assessed probability of occurrence and their potential severity. High-priority risks will typically cluster in the "High Likelihood" and "High Impact" quadrant.

```python
# application_pages/risk_dashboard.py
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
```

### 3. Current Status of AI Risks

This pie chart provides a snapshot of where the organization stands in addressing its AI risks, allowing for easy tracking of mitigation progress.

```python
# application_pages/risk_dashboard.py
    st.subheader("3. Current Status of AI Risks")
    status_counts = df["Status"].value_counts().reset_index()
    status_counts.columns = ["Status", "Count"]
    fig_pie = px.pie(
        status_counts,
        names="Status", values="Count", title="Current Status of AI Risks",
        hole=0.3
    )
    st.plotly_chart(fig_pie, use_container_width=True)
```

### 4. Distribution of Risks Across NIST AI RMF Functions by Category

This histogram illustrates how identified risks align with the four core NIST AI RMF functions (Govern, Map, Measure, Manage), broken down by risk category. This helps in strategizing mitigation actions within the framework.

```python
# application_pages/risk_dashboard.py
    st.subheader("4. Distribution of Risks Across NIST AI RMF Functions by Category")
    fig_nist = px.histogram(
        df,
        x="NIST_AI_RMF_Function", color="Risk_Category", barmode="group",
        title="Distribution of Risks Across NIST AI RMF Functions by Category",
        labels={"NIST_AI_RMF_Function": "NIST AI RMF Function", "count": "Number of Risks"}
    )
    st.plotly_chart(fig_nist, use_container_width=True)
```

### 5. Distribution of Risks Across SR 11-7 Pillars by Category

For financial institutions, this histogram shows how AI risks map to the SR 11-7 pillars (Development/Implementation, Validation, Governance, Ongoing Monitoring), ensuring integration with existing regulatory compliance.

```python
# application_pages/risk_dashboard.py
    st.subheader("5. Distribution of Risks Across SR 11-7 Pillars by Category")
    fig_sr11_7 = px.histogram(
        df,
        x="SR_11_7_Pillar", color="Risk_Category", barmode="group",
        title="Distribution of Risks Across SR 11-7 Pillars by Category",
        labels={"SR_11_7_Pillar": "SR 11-7 Pillar", "count": "Number of Risks"}
    )
    st.plotly_chart(fig_sr11_7, use_container_width=True)
```

## 6. Understanding AI Assurance Artifacts (Model & Data Cards)
Duration: 0:10

The `application_pages/assurance_artifacts.py` module focuses on the conceptual importance of AI assurance artifacts, specifically **Model Cards** and **Data Cards**. While the application doesn't generate these dynamically, it emphasizes their critical role in transparency, accountability, and explainability throughout the AI lifecycle.

<aside class="positive">
These artifacts are essential complements to a risk register. They provide detailed, auditable evidence of a model's characteristics and data provenance, which is vital for "effective challenge" and regulatory compliance.
</aside>

```python
# application_pages/assurance_artifacts.py
import streamlit as st

def main():
    st.header("Conceptual AI Assurance Artifacts: Model Cards & Data Cards")
    st.markdown("Beyond the risk register, robust AI assurance relies on comprehensive documentation artifacts that enhance transparency, accountability, and explainability. Two critical examples are **Model Cards** and **Data Cards**. This section outlines their conceptual templates and guidance.\n\n### Model Cards\nModel Cards provide a comprehensive summary of an AI model's key facts, enhancing transparency and accountability. They are intended to document a model's performance, behavior, and intended use for various stakeholders.\n\n**Key Components of a Model Card:**\n*   **Model Details**:\n    *   Model Name, Version, Developer, Date.\n    *   Intended Use Cases and Context.\n    *   Out-of-Scope Use Cases (Limitations).\n*   **Training Data Characteristics**:\n    *   Description of the training dataset(s).\n    *   Data collection process and provenance.\n    *   Potential biases, sensitive attributes, or demographic information within the data.\n*   **Performance Metrics**:\n    *   Quantitative metrics (e.g., accuracy, precision, recall, F1-score) for relevant subgroups.\n    *   Fairness metrics (e.g., demographic parity, equalized odds) if applicable.\n    *   Performance benchmarks against baselines.\n*   **Ethical Considerations**:\n    *   Potential societal impacts, positive and negative.\n    *   Risks identified (linking to Risk Register).\n    *   Mitigation strategies for ethical concerns.\n*   **Usage Guidelines**:\n    *   Instructions for appropriate model deployment and interaction.\n    *   Monitoring and maintenance procedures.\n    *   Responsible party for model oversight.\n\n### Data Cards\nData Cards are essential for documenting the provenance and characteristics of datasets used in AI. They ensure transparency around data collection, processing, and potential biases, which are critical for addressing data-related risks.\n\n**Key Components of a Data Card:**\n*   **Dataset Overview**:\n    *   Dataset Name, Creator, Version, Date.\n    *   Purpose of the dataset.\n    *   Description of data contents (features, labels).\n    *   Statistics (e.g., distribution of features, missing values).\n    *   Demographic or sensitive information present.\n    *   Potential biases, limitations, or under-representation.\n*   **Data Collection Process**:\n    *   How the data was collected (sources, methods).\n    *   Any preprocessing or cleaning steps applied.\n    *   Anonymization or privacy-preserving techniques used.\n*   **Data Provenance and Lineage**:\n    *   Origin of the data (where it came from).\n    *   History of transformations and modifications.\n    *   Data rights and licensing information.\n*   **Maintenance and Updates**:\n    *   Frequency of updates.\n    *   Responsible party for data stewardship.\n\nThese artifacts are crucial for enabling "effective challenge" and supporting regulatory compliance by providing clear, auditable evidence of responsible AI development and deployment. They directly inform the `Data` and `Model` risk categories and are integral to the `Map` and `Measure` functions of the NIST AI RMF.")
```

### Model Cards

Model Cards provide a comprehensive summary of an AI model's key facts, enhancing transparency and accountability. They document a model's performance, behavior, and intended use for various stakeholders. Key components include Model Details, Training Data Characteristics, Performance Metrics, Ethical Considerations, and Usage Guidelines.

### Data Cards

Data Cards are essential for documenting the provenance and characteristics of datasets used in AI. They ensure transparency around data collection, processing, and potential biases, which are critical for addressing data-related risks. Key components include Dataset Overview, Data Collection Process, Data Provenance and Lineage, and Maintenance and Updates.

## 7. Generating and Interpreting the AI Risk Report
Duration: 0:05

The `application_pages/risk_report.py` module allows users to generate a comprehensive markdown-formatted report summarizing the current state of the AI Risk Register. This report is vital for communication with stakeholders, governance committees, and for demonstrating compliance with internal policies and external regulations.

```python
# application_pages/risk_report.py
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
```

Upon clicking the "Generate Comprehensive Risk Report" button, the `generate_risk_report` function from `app.py` is invoked. This function compiles various summaries and extracts from the `ai_risk_register_df` into a structured Markdown string, which is then displayed directly in the Streamlit application.

The report typically includes:
*   General information (date, total risks).
*   Summaries by risk category, priority score, and status.
*   A list of top high-priority risks.
*   A snippet of the full risk register.
*   Distribution summaries across NIST AI RMF functions and SR 11-7 pillars.

This structured report provides a concise yet thorough overview, enabling quick decision-making and efficient risk governance.

## 8. Conclusion and Further Exploration
Duration: 0:05

Congratulations! You have successfully navigated through the functionalities of the "AI Model Risk Register & Mitigation Planner" Streamlit application. This codelab has provided a comprehensive guide to understanding and interacting with an essential tool for responsible AI deployment.

### Key Takeaways

We've covered:
*   **AI Risk Taxonomy**: Categorizing risks across Data, Model, System, Human, and Organizational dimensions.
*   **Risk Quantification**: Calculating `Risk_Priority_Scores` based on `Likelihood` and `Impact`.
*   **Interactive Risk Management**: Generating synthetic data, adding, editing, and updating risks within a dynamic register.
*   **Visualizing Risk Landscapes**: Utilizing various charts (bar, heatmap, pie, histograms) to interpret risk distributions and priorities.
*   **Assurance Artifacts**: Understanding the conceptual importance of Model Cards and Data Cards for transparency and accountability.
*   **Reporting**: Generating comprehensive, actionable reports for stakeholders.
*   **Framework Integration**: Mapping risks and mitigations to NIST AI RMF functions and SR 11-7 pillars.

By applying these structured approaches, you can proactively identify, assess, mitigate, and monitor AI-specific risks, fostering trust, ensuring compliance, and supporting the responsible deployment of AI within your organizations. Continuous adaptation and monitoring are key to navigating the evolving landscape of AI risks.

### Further Exploration

This application provides a solid foundation. Here are some ideas for extending its capabilities:
*   **Data Persistence**: Integrate with a backend database (e.g., SQLite, PostgreSQL) to ensure data is saved across application sessions.
*   **User Authentication**: Add login functionality to control access and manage different roles (e.g., risk manager, validator).
*   **Advanced Analytics**: Incorporate more sophisticated risk analysis techniques, trend analysis over time, or predictive risk modeling.
*   **Real-time Monitoring Integration**: Connect to actual AI model monitoring systems to automatically update risk statuses or trigger new risk identification.
*   **Workflow Integration**: Implement features for assigning tasks, setting deadlines, and tracking mitigation plan completion.
*   **Customizable Reporting**: Allow users to select specific sections or filters for generated reports.
*   **Alerts and Notifications**: Set up email or in-app notifications for high-priority risks or overdue mitigation actions.

Continue to experiment, adapt, and build upon this foundation to create even more robust AI risk management solutions.

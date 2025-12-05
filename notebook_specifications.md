
# AI Model Risk Assessment & Mitigation Workshop: A Credit Risk Case Study

## 1. Setting the Scene: The Critical Role of an AI Risk Manager

### Story + Context + Real-World Relevance

As a Quantitative Analyst at QuantBank, your primary responsibility is to ensure the integrity and compliance of all models used in critical financial decisions. Today, you've been tasked with a formal risk assessment of a newly developed AI-powered Credit Risk Scoring Model. This model, if deployed, will automate loan approval processes and flag high-risk applicants for manual review. Your assessment is crucial for compliance with regulatory standards like SR 11-7 and internal governance policies.

The core principle guiding this assessment is the understanding that risk is a function of potential impact and likelihood. In quantitative terms, this can be expressed as:

$$
Risk = Impact \times Likelihood
$$

Where *Impact* refers to the severity of adverse outcomes (e.g., financial loss, reputational damage, regulatory penalties), and *Likelihood* refers to the probability of the adverse event occurring. Your job is to systematically identify potential failure points and quantify these two dimensions for the AI model.

## 2. Introducing the Model Under Scrutiny: The Credit Risk AI

### Story + Context + Real-World Relevance

Before diving into risk identification, you need to thoroughly understand the AI model itself. This involves grasping its fundamental purpose, the algorithm it uses, and its intended operational environment. For the new Credit Risk Scoring Model, you've gathered initial details from the development team. This foundational understanding is the first step in applying frameworks like SR 11-7 and NIST AI RMF, ensuring you assess the right "model" in its specific context.

### Code cell (function definition)

Define a function to initialize the metadata for our hypothetical AI model scenario. This function will create a dictionary containing key characteristics of the model.

```python
def initialize_model_scenario_metadata():
    """
    Initializes and returns metadata for the hypothetical Credit Risk Scoring AI Model.
    """
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
```

### Code cell (function execution)

Execute the function to populate the model scenario metadata.

```python
credit_risk_model_scenario = initialize_model_scenario_metadata()
print("Hypothetical AI Model Scenario Details:")
for key, value in credit_risk_model_scenario.items():
    print(f"- {key}: {value}")
```

### Markdown cell (explanation of execution only if necessary)

This output provides a clear, concise overview of the AI model. For a Risk Manager, this information is critical for establishing the scope of the assessment and understanding the model's direct impact on business operations and potential regulatory exposure. It immediately highlights that this is a high-stakes model impacting customer finances.

## 3. Constructing the AI Model Card: Transparency & Key Facts

### Story + Context + Real-World Relevance

To ensure transparency and facilitate effective challenge, you need to create an 'AI Model Card' for the Credit Risk Scoring Model. This artifact, inspired by best practices in AI assurance, summarizes crucial information about the model, including its purpose, performance metrics, and known limitations. This proactive documentation is vital for internal stakeholders and external auditors, enhancing accountability and reducing information asymmetry, directly supporting SR 11-7's emphasis on validation and governance.

### Code cell (function definition)

Define a function to populate the model card based on the model scenario and some hypothetical performance metrics.

```python
def populate_model_card(model_metadata, auc_score, precision_at_recall_90):
    """
    Populates an AI Model Card with model metadata and hypothetical performance metrics.

    Parameters:
    model_metadata (dict): Dictionary containing the model's core characteristics.
    auc_score (float): Hypothetical AUC score.
    precision_at_recall_90 (float): Hypothetical Precision at 90% Recall.

    Returns:
    dict: A populated AI Model Card.
    """
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
```

### Code cell (function execution)

Populate the Model Card for the Credit Risk Scoring Model with the specified hypothetical performance metrics.

```python
# Hypothetical performance metrics for the credit risk model
hypothetical_auc = 0.85
hypothetical_precision_at_recall = 0.60

credit_risk_model_card = populate_model_card(
    credit_risk_model_scenario,
    hypothetical_auc,
    hypothetical_precision_at_recall
)
print("--- AI Model Card: Credit Risk Scoring Model ---")
for key, value in credit_risk_model_card.items():
    if isinstance(value, dict) or isinstance(value, list):
        print(f"- {key}:")
        for item in value:
            print(f"  - {item}")
    else:
        print(f"- {key}: {value}")
```

### Markdown cell (explanation of execution only if necessary)

The generated Model Card provides a structured summary. As a Risk Manager, you immediately see the model's purpose, algorithm, and crucial performance indicators (AUC: 0.85, Precision@90%Recall: 0.60). Importantly, the "Known Limitations" section proactively highlights areas of concern like potential bias and performance degradation, which will be central to your risk identification process. This artifact serves as a single source of truth for the model's core information.

## 4. Dissecting the Data: Creating a Data Card

### Story + Context + Real-World Relevance

The quality and characteristics of the training data are paramount to an AI model's performance and fairness. As a Quantitative Analyst, you understand that "garbage in, garbage out" applies rigorously to AI. You need to document the synthetic dataset used to train the Credit Risk Scoring Model. This 'Data Card' will detail its provenance, features, and crucially, any identified biases or quality issues. This directly addresses the "Data" dimension of AI risk, as highlighted by NIST AI RMF and SR 11-7's emphasis on data quality in model validation.

### Code cell (function definition)

Define a function to populate the data card with details about the hypothetical credit dataset.

```python
def populate_data_card(dataset_name, source, collection_method, size, features_desc, sensitive_features, potential_biases, preprocessing_steps):
    """
    Populates a Data Card with details about the hypothetical credit dataset.

    Parameters:
    dataset_name (str): Name of the dataset.
    source (str): Source of the data.
    collection_method (str): How data was collected.
    size (tuple): (rows, features) of the dataset.
    features_desc (dict): Description of each feature.
    sensitive_features (list): List of features considered sensitive.
    potential_biases (list): List of identified potential biases.
    preprocessing_steps (list): Steps taken to preprocess the data.

    Returns:
    dict: A populated Data Card.
    """
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
```

### Code cell (function execution)

Populate the Data Card for the synthetic `credit_data.csv`.

```python
synthetic_dataset_details = {
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

credit_data_card = populate_data_card(**synthetic_dataset_details)

print("\n--- Data Card: Credit Application Data ---")
for key, value in credit_data_card.items():
    if isinstance(value, dict) or isinstance(value, list):
        print(f"- {key}:")
        for item in value:
            print(f"  - {item}")
    else:
        print(f"- {key}: {value}")
```

### Markdown cell (explanation of execution only if necessary)

The Data Card clearly outlines the dataset's characteristics and, critically, highlights potential biases and data quality issues. As a Risk Manager, you note the "Historical lending bias" and "Underrepresentation" as immediate red flags for fairness, while "Missing Data" and "CreditScore Lag" point to accuracy and reliability concerns. This information directly informs the data-related risks you'll formally document in the risk register.

## 5. Foundations of Financial Model Risk: SR 11-7 in an AI Context

### Story + Context + Real-World Relevance

As a Quantitative Analyst in a financial institution, SR 11-7 (Supervisory Guidance on Model Risk Management) is your bedrock for model governance. While it predates modern AI, its core principles of Model Risk Management (MRM) remain highly relevant. You must consider how SR 11-7's pillars—model development, implementation, validation, and governance—translate to AI systems. This conceptual mapping ensures that even novel AI models are subject to the same rigor and oversight as traditional financial models, especially concerning "effective challenge" and sound governance.

The definition of model risk under SR 11-7 is broad and encompasses the potential for adverse consequences from decisions based on incorrect or misused model outputs. This includes financial loss, reputational damage, and flawed decisions. The guidance emphasizes that model risk intensifies with greater model complexity, higher input uncertainty, broader extent of use, and larger potential impact. These considerations are particularly amplified with AI models due to their opacity and emergent behaviors.

## 6. Embracing Trustworthy AI: The NIST AI RMF 1.0 Framework

### Story + Context + Real-World Relevance

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

## 7. First Pass: Identifying Data-Related Risks

### Story + Context + Real-World Relevance

Now equipped with the model and data cards, and frameworks like SR 11-7 and NIST AI RMF, you begin the systematic identification of risks. You'll start with the "Data" dimension of the AI Risk Taxonomy. Based on the Data Card and your general knowledge of credit risk modeling, you need to identify concrete risks related to data quality, provenance, relevance, and privacy that could impact the Credit Risk Scoring Model. Documenting these risks is the first step in populating your AI Risk Register.

### Code cell (function definition)

Define a function to add a new risk entry to the global `risk_register_df`.

```python
def add_risk_to_register(dimension, category, description, potential_impact="Medium", likelihood="Medium"):
    """
    Adds a new risk entry to the global AI Risk Register.

    Parameters:
    dimension (str): The AI risk dimension (Data, Model, System, Human, Organizational).
    category (str): A sub-category of the risk (e.g., Quality, Bias, Integration).
    description (str): Detailed description of the risk.
    potential_impact (str): Assessed impact (Low, Medium, High).
    likelihood (str): Assessed likelihood (Low, Medium, High).
    """
    global risk_register_df, next_risk_id

    impact_map = {"Low": 1, "Medium": 2, "High": 3}
    likelihood_map = {"Low": 1, "Medium": 2, "High": 3}

    impact_score = impact_map.get(potential_impact, 0)
    likelihood_score = likelihood_map.get(likelihood, 0)
    risk_score = impact_score * likelihood_score

    new_risk = {
        "Risk ID": f"R{next_risk_id:03d}",
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
    risk_register_df = pd.concat([risk_register_df, pd.DataFrame([new_risk])], ignore_index=True)
    next_risk_id += 1
```

### Code cell (function execution)

Add several identified data-related risks for the Credit Risk Scoring Model.

```python
print("Identifying Data-Related Risks...")
add_risk_to_register(
    dimension="Data",
    category="Data Quality",
    description="Inconsistent or missing data in 'EmploymentStatus' could lead to inaccurate risk assessments, violating Validity."
)
add_risk_to_register(
    dimension="Data",
    category="Data Bias",
    description="Historical bias in income data from specific 'ResidentialStatus' groups could lead to unfair decisions for future applicants, violating Fairness."
)
add_risk_to_register(
    dimension="Data",
    category="Data Provenance & Relevance",
    description="CreditScore data from an older system, updated quarterly, may not reflect real-time creditworthiness, impacting model Reliability and Validity."
)
add_risk_to_register(
    dimension="Data",
    category="Data Privacy",
    description="Potential exposure of sensitive demographic data if access controls are insufficient, violating Privacy-Preserving."
)

print("\nCurrent AI Risk Register (Data Risks):")
display(risk_register_df)
```

### Markdown cell (explanation of execution only if necessary)

The `risk_register_df` now includes initial data-related risks. For instance, the "Historical bias in income data" (R002) is a critical concern for fairness, directly linking to the NIST AI RMF's 'Fairness' attribute and potentially leading to adverse outcomes under SR 11-7. The 'CreditScore Lag' (R003) highlights a data relevance issue affecting the model's reliability. This structured approach ensures no critical data risk is overlooked.

## 8. Diving Deeper: Identifying Model-Related Risks

### Story + Context + Real-World Relevance

Next, you shift your focus to the "Model" dimension of the AI Risk Taxonomy. This involves scrutinizing the AI model's algorithm, its performance characteristics, and potential vulnerabilities. You'll consider algorithmic bias, accuracy, reliability, and robustness based on the Model Card and the nature of gradient boosting classifiers. Identifying these risks is crucial for understanding how the model itself might fail or produce undesirable outcomes.

### Code cell (function execution)

Add several identified model-related risks for the Credit Risk Scoring Model.

```python
print("\nIdentifying Model-Related Risks...")
add_risk_to_register(
    dimension="Model",
    category="Algorithmic Bias & Fairness",
    description="The Gradient Boosting Classifier's complex decision boundaries might amplify subtle biases present in training data, leading to disparate impact on underrepresented groups, violating Fairness."
)
add_risk_to_register(
    dimension="Model",
    category="Accuracy & Reliability",
    description="Model performance (Precision@90%Recall: 0.60) might be insufficient for high-stakes decisions, leading to higher false negatives (approving defaulters), violating Validity and Reliability."
)
add_risk_to_register(
    dimension="Model",
    category="Model Robustness",
    description="Model performance may degrade significantly with concept drift due to changing economic conditions (e.g., recession), leading to unstable predictions, violating Reliability."
)
add_risk_to_register(
    dimension="Model",
    category="Interpretability",
    description="The black-box nature of Gradient Boosting makes it difficult to explain individual loan decisions to applicants or regulators, impacting Transparency and Accountability."
)

print("\nCurrent AI Risk Register (Data & Model Risks):")
display(risk_register_df)
```

### Markdown cell (explanation of execution only if necessary)

The register now details model-specific concerns. "Algorithmic Bias" (R005) directly relates to the fairness attribute, while "Model Robustness" (R007) highlights the risk of the model's reliability failing under new market conditions. The "Interpretability" risk (R008) is a key challenge for AI models, affecting transparency and accountability, which are vital for regulatory scrutiny and effective challenge.

## 9. Systemic Concerns: Identifying System-Related Risks

### Story + Context + Real-World Relevance

Your next task is to assess the "System" dimension. The Credit Risk Scoring Model doesn't operate in a vacuum; it's integrated into QuantBank's IT infrastructure. You need to identify risks related to how the model is deployed, its architectural dependencies, and potential vulnerabilities in its supply chain. Integration flaws, security weaknesses, or reliance on unvetted third-party components could lead to significant operational disruptions or data breaches, violating NIST's Security attribute.

### Code cell (function execution)

Add several identified system-related risks for the Credit Risk Scoring Model.

```python
print("\nIdentifying System-Related Risks...")
add_risk_to_register(
    dimension="System",
    category="Integration Flaws",
    description="API integration into the legacy Loan Origination System might introduce latency or data corruption, leading to incorrect or delayed decisions, violating Validity and Safety."
)
add_risk_to_register(
    dimension="System",
    category="AI Supply Chain Vulnerabilities",
    description="Reliance on open-source libraries (e.g., LightGBM) without thorough internal vetting could introduce security vulnerabilities or unpatched bugs, violating Security."
)
add_risk_to_register(
    dimension="System",
    category="Scalability & Performance",
    description="The current deployment infrastructure may not handle peak load volumes for real-time predictions, leading to system outages or degraded service, violating Reliability."
)

print("\nCurrent AI Risk Register (Data, Model, & System Risks):")
display(risk_register_df)
```

### Markdown cell (explanation of execution only if necessary)

The system-related risks are now documented. "API integration flaws" (R009) could directly impact the reliability and safety of the loan application process. "AI Supply Chain Vulnerabilities" (R010) are critical, as unvetted components can introduce security risks, a key concern for any financial institution. These risks highlight that AI model risk extends far beyond the algorithm itself.

## 10. The Human Element: Identifying Human-Centric AI Risks

### Story + Context + Real-World Relevance

Even the most sophisticated AI model requires human interaction and oversight. You now turn to the "Human" dimension, considering how loan officers, applicants, and other human stakeholders interact with the Credit Risk Scoring Model. Risks can arise from misuse, over-reliance, misinterpretation of outputs, or insufficient human control. This is critical for maintaining accountability and preventing scenarios where the AI operates outside its intended scope, a key aspect of NIST's Accountability and Safety principles.

### Code cell (function execution)

Add several identified human-centric risks for the Credit Risk Scoring Model.

```python
print("\nIdentifying Human-Centric AI Risks...")
add_risk_to_register(
    dimension="Human",
    category="Misuse & Misinterpretation",
    description="Loan officers might misinterpret model outputs or explanations, leading to incorrect manual overrides or decisions, violating Transparency and Accountability."
)
add_risk_to_register(
    dimension="Human",
    category="Over-Reliance & Autonomy Creep",
    description="Over-reliance on automated 'Approve' decisions could lead to a decline in human critical judgment, increasing undetected errors or biases, violating Accountability."
)
add_risk_to_register(
    dimension="Human",
    category="Loss of Human Oversight",
    description="Lack of a clear 'human-in-the-loop' process for edge cases or flagged applications could lead to the model making autonomous, unreviewed decisions with adverse outcomes, violating Safety and Accountability."
)

print("\nCurrent AI Risk Register (Data, Model, System, & Human Risks):")
display(risk_register_df)
```

### Markdown cell (explanation of execution only if necessary)

The `risk_register_df` now includes risks from human interaction. "Misinterpretation" (R012) underscores the need for clear model explanations, directly linking to Transparency. "Over-Reliance" (R013) highlights a governance challenge where human expertise might atrophy, increasing the impact of model errors. "Loss of Human Oversight" (R014) is a fundamental risk, emphasizing that human control must be maintained, aligning with SR 11-7's effective challenge and NIST's safety principles.

## 11. Organizational Readiness: Identifying Organizational AI Risks

### Story + Context + Real-World Relevance

Finally, you assess the "Organizational" dimension. This encompasses the governance structures, policies, and culture that support the AI model throughout its lifecycle. Weak governance, inadequate policies, or a lack of a responsible AI culture can amplify all other risks. Your task is to identify gaps in these areas that could hinder effective risk management, compliance, and accountability. This is where SR 11-7's governance pillar and NIST's robust accountability framework converge.

### Code cell (function execution)

Add several identified organizational AI risks for the Credit Risk Scoring Model.

```python
print("\nIdentifying Organizational AI Risks...")
add_risk_to_register(
    dimension="Organizational",
    category="Robust Governance & Oversight",
    description="Absence of a dedicated AI Ethics Committee or clear roles for AI risk oversight beyond traditional MRM could lead to unaddressed ethical concerns, violating Accountability."
)
add_risk_to_register(
    dimension="Organizational",
    category="Policy & Ethical Guidelines",
    description="Lack of a comprehensive incident response plan for AI model failures (e.g., severe drift, bias detection) could delay remediation and amplify negative impact, violating Safety and Accountability."
)
add_risk_to_register(
    dimension="Organizational",
    category="Responsible AI Culture",
    description="Insufficient training or awareness programs for employees on responsible AI use and emergent risks could lead to poor operational practices, violating Accountability."
)

print("\nFinal Identified Risks in AI Risk Register:")
display(risk_register_df)
```

### Markdown cell (explanation of execution only if necessary)

The `risk_register_df` now provides a comprehensive list of risks across all five dimensions. The "Absence of a dedicated AI Ethics Committee" (R015) is a significant governance gap. "Lack of a comprehensive incident response plan" (R016) directly relates to operational resilience and accountability. This holistic view helps you understand the interconnected nature of AI risks, where organizational weaknesses can exacerbate technical failures.

## 12. Assessing Risk Severity: Impact and Likelihood Scoring

### Story + Context + Real-World Relevance

With all risks identified, your next step as a Risk Manager is to assess their severity. You'll use a qualitative scoring system for "Potential Impact" and "Likelihood," typically rated as Low, Medium, or High. This allows you to prioritize risks, focusing mitigation efforts on those with the highest scores. This process directly applies the fundamental risk formula ($Risk = Impact \times Likelihood$) and prepares for detailed discussion with stakeholders on critical risks.

### Code cell (function definition)

Define a function to update the impact and likelihood for existing risks in the register and recalculate their scores.

```python
def assess_risk_severity(risk_id, potential_impact, likelihood):
    """
    Updates the potential impact and likelihood for a specific risk,
    then recalculates the risk score.

    Parameters:
    risk_id (str): The ID of the risk to update (e.g., 'R001').
    potential_impact (str): New assessed impact (Low, Medium, High).
    likelihood (str): New assessed likelihood (Low, Medium, High).
    """
    global risk_register_df

    impact_map = {"Low": 1, "Medium": 2, "High": 3}
    likelihood_map = {"Low": 1, "Medium": 2, "High": 3}

    idx = risk_register_df[risk_register_df["Risk ID"] == risk_id].index
    if not idx.empty:
        idx = idx[0]
        risk_register_df.loc[idx, "Potential Impact"] = potential_impact
        risk_register_df.loc[idx, "Likelihood"] = likelihood
        
        impact_score = impact_map.get(potential_impact, 0)
        likelihood_score = likelihood_map.get(likelihood, 0)
        risk_register_df.loc[idx, "Risk Score"] = impact_score * likelihood_score
        risk_register_df.loc[idx, "Status"] = "Assessed"
        print(f"Risk {risk_id} updated with Impact: {potential_impact}, Likelihood: {likelihood}, Score: {impact_score * likelihood_score}")
    else:
        print(f"Risk ID {risk_id} not found.")
```

### Code cell (function execution)

Assign specific impact and likelihood scores to a selection of the identified risks.

```python
print("\nAssessing Severity for Identified Risks:")
# Data Risks
assess_risk_severity("R002", "High", "Medium")  # Historical data bias
assess_risk_severity("R003", "Medium", "High") # CreditScore Lag
assess_risk_severity("R004", "Medium", "Medium") # Data Privacy

# Model Risks
assess_risk_severity("R005", "High", "Medium")  # Algorithmic Bias
assess_risk_severity("R006", "Medium", "Low")   # Accuracy & Reliability
assess_risk_severity("R007", "High", "High")    # Model Robustness (concept drift)
assess_risk_severity("R008", "Medium", "High")  # Interpretability

# System Risks
assess_risk_severity("R009", "Medium", "Medium") # Integration Flaws
assess_risk_severity("R010", "High", "Low")    # AI Supply Chain Vulnerabilities
assess_risk_severity("R011", "Medium", "Medium") # Scalability & Performance

# Human Risks
assess_risk_severity("R012", "Medium", "High") # Misuse & Misinterpretation
assess_risk_severity("R013", "High", "Medium") # Over-Reliance & Autonomy Creep
assess_risk_severity("R014", "High", "High")  # Loss of Human Oversight

# Organizational Risks
assess_risk_severity("R015", "High", "Medium") # Absence of AI Ethics Committee
assess_risk_severity("R016", "High", "High")  # Lack of Incident Response Plan
assess_risk_severity("R017", "Medium", "Medium") # Insufficient training

print("\nAI Risk Register with Assessed Risks:")
display(risk_register_df.sort_values(by="Risk Score", ascending=False))
```

### Markdown cell (explanation of execution only if necessary)

The risk register now shows updated `Potential Impact`, `Likelihood`, and `Risk Score` for each entry. For example, "Model Robustness" (R007) and "Loss of Human Oversight" (R014) now have the highest scores (9), indicating they are critical risks requiring immediate attention. This scoring helps you quickly identify the most pressing concerns for the Credit Risk Scoring Model, allowing for efficient allocation of resources for mitigation.

## 13. Visualizing the Risk Landscape: The AI Risk Matrix

### Story + Context + Real-World Relevance

To effectively communicate the risk landscape to senior management and other stakeholders, a visual representation is essential. As a Risk Manager, you'll create a Risk Matrix, plotting each identified risk based on its assessed impact and likelihood. This visualization quickly highlights high-priority risks that fall into the "High Impact, High Likelihood" quadrant, enabling a clear and concise presentation for your upcoming 'Effective Challenge' meeting.

### Code cell (function definition)

Define a function to plot the identified risks on a 3x3 risk matrix.

```python
def plot_risk_matrix(risk_df):
    """
    Generates a 3x3 risk matrix visualization based on assessed risks.

    Parameters:
    risk_df (pd.DataFrame): DataFrame containing assessed risks with 'Potential Impact' and 'Likelihood'.
    """
    impact_order = ["Low", "Medium", "High"]
    likelihood_order = ["Low", "Medium", "High"]
    
    # Map qualitative ratings to numerical for plotting
    risk_df_plot = risk_df.copy()
    risk_df_plot["Impact_Num"] = risk_df_plot["Potential Impact"].map(lambda x: impact_order.index(x) + 0.5)
    risk_df_plot["Likelihood_Num"] = risk_df_plot["Likelihood"].map(lambda x: likelihood_order.index(x) + 0.5)

    plt.figure(figsize=(10, 8))
    sns.scatterplot(
        data=risk_df_plot,
        x="Likelihood_Num",
        y="Impact_Num",
        hue="Risk Score",
        size="Risk Score",
        sizes=(100, 1000),
        palette="viridis",
        legend="full"
    )

    # Set matrix grid
    plt.axvline(x=1, color='gray', linestyle='--', linewidth=0.8)
    plt.axvline(x=2, color='gray', linestyle='--', linewidth=0.8)
    plt.axhline(y=1, color='gray', linestyle='--', linewidth=0.8)
    plt.axhline(y=2, color='gray', linestyle='--', linewidth=0.8)

    # Add background colors for risk levels
    plt.axvspan(2, 3, ymin=2/3, ymax=1, color='red', alpha=0.15, label='High Risk')
    plt.axvspan(2, 3, ymin=1/3, ymax=2/3, color='orange', alpha=0.15)
    plt.axvspan(1, 2, ymin=2/3, ymax=1, color='orange', alpha=0.15)
    plt.axvspan(2, 3, ymin=0, ymax=1/3, color='yellow', alpha=0.15)
    plt.axvspan(1, 2, ymin=1/3, ymax=2/3, color='yellow', alpha=0.15)
    plt.axvspan(0, 1, ymin=2/3, ymax=1, color='yellow', alpha=0.15)
    plt.axvspan(1, 2, ymin=0, ymax=1/3, color='green', alpha=0.15)
    plt.axvspan(0, 1, ymin=1/3, ymax=2/3, color='green', alpha=0.15)
    plt.axvspan(0, 1, ymin=0, ymax=1/3, color='lightgreen', alpha=0.15, label='Low Risk')


    plt.xticks([0.5, 1.5, 2.5], likelihood_order)
    plt.yticks([0.5, 1.5, 2.5], impact_order)
    plt.xlabel("Likelihood")
    plt.ylabel("Potential Impact")
    plt.title("AI Model Risk Matrix: Credit Risk Scoring Model")
    
    # Annotate points with Risk ID
    for i, row in risk_df_plot.iterrows():
        plt.annotate(row["Risk ID"], (row["Likelihood_Num"] + 0.1, row["Impact_Num"] + 0.1), fontsize=8)

    plt.grid(False) # Remove default grid to avoid overlap with custom lines
    plt.xlim(0, 3)
    plt.ylim(0, 3)
    plt.show()

```

### Code cell (function execution)

Generate the risk matrix for the assessed risks in the register.

```python
plot_risk_matrix(risk_register_df)
```

### Markdown cell (explanation of execution only if necessary)

The Risk Matrix visually groups risks, making it immediately clear which ones reside in the high-risk "red" zone (High Impact, High Likelihood). You can quickly point out risks like R007 ("Model Robustness"), R014 ("Loss of Human Oversight"), and R016 ("Lack of Incident Response Plan") as top priorities. This visual summary is an invaluable tool for driving discussions with non-technical stakeholders and securing resources for mitigation.

## 14. Strategic Risk Mitigation: Developing Controls

### Story + Context + Real-World Relevance

Identifying and assessing risks is only half the battle. As a Risk Manager, your next critical step is to propose concrete mitigation strategies and controls for the highest-priority risks. These strategies should align with NIST AI RMF's emphasis on control measures and SR 11-7's requirement for robust validation and governance. For example, for model bias, a mitigation could involve fairness audits and re-training with debiased data. For human oversight, it might involve "human-in-the-loop" mechanisms.

### Code cell (function definition)

Define a function to update the `Mitigation Strategy` and `Responsible Party` for a specific risk.

```python
def add_mitigation_strategy(risk_id, strategy_description, responsible_party):
    """
    Adds a mitigation strategy and responsible party to a specific risk entry.

    Parameters:
    risk_id (str): The ID of the risk to update.
    strategy_description (str): Detailed description of the mitigation strategy.
    responsible_party (str): The team or individual responsible for implementation.
    """
    global risk_register_df
    idx = risk_register_df[risk_register_df["Risk ID"] == risk_id].index
    if not idx.empty:
        idx = idx[0]
        risk_register_df.loc[idx, "Mitigation Strategy"] = strategy_description
        risk_register_df.loc[idx, "Responsible Party"] = responsible_party
        risk_register_df.loc[idx, "Status"] = "Mitigation Proposed"
        print(f"Mitigation strategy added for Risk {risk_id}.")
    else:
        print(f"Risk ID {risk_id} not found.")
```

### Code cell (function execution)

Propose mitigation strategies for the top-priority risks identified in the risk matrix.

```python
print("\nDeveloping Mitigation Strategies for High-Priority Risks:")

# For R007: Model Robustness (High Impact, High Likelihood)
add_mitigation_strategy(
    "R007",
    "Implement continuous monitoring for concept drift (e.g., population stability index) with quarterly model re-calibration or re-training. Develop a champion-challenger framework.",
    "Model Monitoring Team"
)

# For R014: Loss of Human Oversight (High Impact, High Likelihood)
add_mitigation_strategy(
    "R014",
    "Establish clear 'human-in-the-loop' checkpoints for all high-value loan decisions and edge cases. Mandate model explanation training for loan officers.",
    "Operations & Compliance"
)

# For R016: Lack of Incident Response Plan (High Impact, High Likelihood)
add_mitigation_strategy(
    "R016",
    "Develop and socialize a comprehensive AI model incident response plan, including clear communication protocols, rollback procedures, and stakeholder notification processes.",
    "Risk Management & IT Operations"
)

# For R002: Historical data bias (High Impact, Medium Likelihood)
add_mitigation_strategy(
    "R002",
    "Conduct regular fairness audits across protected groups. Explore data augmentation or re-sampling techniques to debias training data. Implement post-processing bias mitigation techniques.",
    "Data Science & AI Ethics Committee"
)

# For R005: Algorithmic Bias (High Impact, Medium Likelihood)
add_mitigation_strategy(
    "R005",
    "Implement disparate impact testing during model validation. Use fairness-aware training algorithms or re-weighing techniques. Document fairness metrics in model card.",
    "Model Validation & Data Science"
)

# For R015: Absence of AI Ethics Committee (High Impact, Medium Likelihood)
add_mitigation_strategy(
    "R015",
    "Propose the formation of a cross-functional AI Ethics Committee to guide policy, review high-risk models, and provide an 'effective challenge' on ethical considerations.",
    "Senior Management & Governance"
)

print("\nAI Risk Register with Proposed Mitigations (Top Risks):")
display(risk_register_df.sort_values(by="Risk Score", ascending=False))
```

### Markdown cell (explanation of execution only if necessary)

The `risk_register_df` now includes specific `Mitigation Strategy` and `Responsible Party` for the prioritized risks. For instance, for "Model Robustness" (R007), a clear strategy involving continuous monitoring and re-calibration is proposed. This structured approach moves beyond mere identification to actionable plans, directly supporting the "Manage" function of the NIST AI RMF and reinforcing SR 11-7's call for robust controls.

## 15. Consolidating Findings: Populating the AI Risk Register

### Story + Context + Real-World Relevance

The ultimate deliverable of your assessment is a comprehensive AI Risk Register. This living document consolidates all identified risks, their assessment (impact, likelihood, score), and the proposed mitigation strategies. As a Risk Manager, you understand that this register is crucial for ongoing monitoring, auditability, and demonstrating compliance. It serves as the single source of truth for the AI model's risk profile, empowering the organization to manage it effectively throughout its lifecycle.

### Code cell (function definition)

Define a function to generate a final, formatted AI Risk Register report.

```python
def generate_risk_register_report(risk_df):
    """
    Generates a formatted AI Risk Register report.

    Parameters:
    risk_df (pd.DataFrame): The complete DataFrame of AI risks.

    Returns:
    pd.DataFrame: A formatted DataFrame representing the AI Risk Register.
    """
    # Ensure the order of columns for the final report
    final_columns = [
        "Risk ID", "Dimension", "Category", "Description",
        "Potential Impact", "Likelihood", "Risk Score",
        "Mitigation Strategy", "Responsible Party", "Status"
    ]
    
    report_df = risk_df[final_columns].copy()
    report_df = report_df.sort_values(by="Risk Score", ascending=False)
    report_df.reset_index(drop=True, inplace=True)
    return report_df
```

### Code cell (function execution)

Generate and display the complete AI Risk Register.

```python
final_ai_risk_register = generate_risk_register_report(risk_register_df)

print("--- Comprehensive AI Model Risk Register: Credit Risk Scoring Model ---")
display(final_ai_risk_register)

print("\n--- Risk Distribution Across Dimensions ---")
risk_counts_by_dimension = final_ai_risk_register['Dimension'].value_counts()
print(risk_counts_by_dimension)

plt.figure(figsize=(8, 6))
sns.barplot(x=risk_counts_by_dimension.index, y=risk_counts_by_dimension.values, palette='viridis')
plt.title('Distribution of Identified Risks Across AI Dimensions')
plt.xlabel('AI Risk Dimension')
plt.ylabel('Number of Risks')
plt.show()
```

### Markdown cell (explanation of execution only if necessary)

The generated table represents the complete AI Risk Register, a critical deliverable. It provides a clear, sortable overview of all identified and assessed risks, along with their proposed mitigation strategies and responsible parties. The bar chart further aids in understanding the overall risk exposure, quickly showing which dimensions (e.g., Model, Data, Human) have the highest number of identified risks. This document is now ready for presentation, audit, and ongoing management, fulfilling a core requirement of both SR 11-7 and NIST AI RMF.

## 16. Concluding the Assessment: Preparing for Effective Challenge

### Story + Context + Real-World Relevance

As a Quantitative Analyst, your detailed AI Risk Register and associated artifacts (Model Card, Data Card) form the basis for the "Effective Challenge" process. This principle, central to SR 11-7, mandates that objective and informed reviewers critically test models to identify hidden errors, biases, or limitations. By systematically identifying risks, assessing their impact, and proposing mitigations, you've provided the necessary documentation for internal validation teams, auditors, and senior management to rigorously scrutinize the Credit Risk Scoring Model. Your work ensures that QuantBank can deploy AI models with confidence, upholding regulatory compliance and fostering trustworthiness in AI. This iterative process of identification, assessment, mitigation, and challenge is crucial for continuous improvement and adaptive governance in AI risk management.

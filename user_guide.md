id: 6931cf92ca38c557e5169645_user_guide
summary: AI Design and Deployment Lab 1 - Clone User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Navigating AI Risk: A QuantBank Codelab for Responsible AI

## 1. Setting the Scene: Your Role as a Quant Analyst
Duration: 00:05:00

Welcome to QuantBank! In this codelab, you step into the shoes of a Quantitative Analyst with a critical mission: to conduct a formal risk assessment of a new AI-powered Credit Risk Scoring Model. This model is designed to automate loan approvals and flag high-risk applicants, making its integrity and compliance paramount for the bank.

<aside class="positive">
<b>The Importance of AI Risk Management in Finance:</b> In the financial sector, AI models wield significant power over critical decisions. Ensuring these models are fair, accurate, and transparent is not just good practice; it's a regulatory imperative. Mismanaging AI risks can lead to financial losses, reputational damage, and severe regulatory penalties. This codelab will equip you with a systematic approach to identify and mitigate such risks.
</aside>

At the core of risk management lies a fundamental principle:

$$ Risk = Impact \times Likelihood $$

Where *Impact* refers to the severity of adverse outcomes (e.g., financial loss, reputational damage), and *Likelihood* refers to the probability of that adverse event occurring. Your task is to systematically identify potential failure points in the AI model and quantify these two dimensions.

To begin your assessment, click the **Start Assessment** button. This will guide you to the next phase of understanding the AI model.

## 2. Understanding the Credit Risk AI Model and Its Card
Duration: 00:07:00

Before you can assess risks, you must first thoroughly understand the AI model itself. This involves grasping its purpose, the algorithm it uses, and its operational environment. You've gathered initial details from the development team regarding the **Credit Risk Scoring Model**.

The application now displays a **Hypothetical AI Model Scenario Details**, offering a concise overview of the model's fundamental characteristics. Pay attention to details like its type (`Supervised Learning, Classification`), algorithm (`Gradient Boosting Classifier`), and `Intended Use` (`Automate approval... flag high-risk applicants...`). This foundational understanding is crucial for establishing the scope of your risk assessment.

Next, you will create an 'AI Model Card' for this model. An AI Model Card is a vital document for transparency and accountability, summarizing key information such as:

*   **Model Name**: The official name of the AI model.
*   **Purpose & Intended Use**: What the model is designed to do and how it will be deployed.
*   **Algorithm**: The underlying machine learning technique.
*   **Key Performance Metrics**: Important indicators like AUC and Precision@Recall, which show how well the model performs.
*   **Known Limitations**: Crucial insights into potential weaknesses, biases, or scenarios where the model might not perform optimally.
*   **Developer & Last Review Date**: Information about who built and validated the model.

The application has automatically generated a **AI Model Card: Credit Risk Scoring Model** based on the scenario details. Review this card carefully.

<aside class="positive">
<b>Why Model Cards Matter:</b> A well-structured Model Card provides a single source of truth about an AI model. For a Risk Manager, it immediately highlights crucial information like performance metrics (e.g., AUC: $0.85$, Precision@90%Recall: $0.60$) and, most importantly, proactively outlines "Known Limitations." These limitations will be central to your risk identification process, helping you anticipate where the model might fail or exhibit unintended behavior.
</aside>

Once you've reviewed the model overview and its card, proceed by clicking **Next: Data Card**.

## 3. Dissecting the Data for the Credit Risk Model and Its Card
Duration: 00:07:00

The integrity of any AI model is intrinsically linked to the quality and characteristics of the data it's trained on. As a Quantitative Analyst, you know that "garbage in, garbage out" applies rigorously to AI. Therefore, your next step is to examine and document the dataset used for the Credit Risk Scoring Model.

Similar to the Model Card, a 'Data Card' provides a comprehensive summary of the dataset. This document details:

*   **Dataset Name, Source, and Collection Method**: Where the data comes from and how it was compiled.
*   **Size (rows, features)**: The scale of the dataset.
*   **Features Description**: Explanations for each piece of information (e.g., 'Age', 'Income', 'CreditScore').
*   **Sensitive Features**: Features that could potentially lead to biased outcomes (e.g., demographic data).
*   **Potential Biases**: Pre-existing biases identified in the data that could be amplified by the model.
*   **Preprocessing Steps**: How the data was cleaned and transformed before model training.

The application now displays the **Data Card: Credit Application Data**. Take a moment to review this information.

<aside class="negative">
<b>Identifying Data Biases:</b> As a Risk Manager, the "Potential Biases" section is a critical area of focus. Note entries like "Historical lending bias" and "Underrepresentation." These are immediate red flags for fairness and ethical concerns. Similarly, "Missing Data" and "CreditScore Lag" highlight potential issues with data quality and reliability that could directly impact the model's accuracy. Documenting these aspects early is vital for a thorough risk assessment.
</aside>

After reviewing the Data Card, click **Next: AI Risk Frameworks** to move on to understanding the guiding principles for your assessment.

## 4. Foundations: SR 11-7 & NIST AI RMF 1.0
Duration: 00:08:00

As a Quantitative Analyst in a financial institution, your risk assessment isn't conducted in a vacuum. It's grounded in established frameworks that guide model governance and trustworthy AI practices.

### Foundations of Financial Model Risk: SR 11-7 in an AI Context

**SR 11-7 (Supervisory Guidance on Model Risk Management)** is the bedrock for model governance in finance. While it predates modern AI, its core principles of Model Risk Management (MRM) are highly relevant. You must consider how SR 11-7's pillars—model development, implementation, validation, and governance—translate to AI systems. This conceptual mapping ensures that even novel AI models are subject to the same rigor and oversight as traditional financial models.

<aside class="info">
<b>Key Takeaway from SR 11-7:</b> Model risk, defined as adverse consequences from incorrect or misused model outputs, intensifies with greater model complexity, higher input uncertainty, broader extent of use, and larger potential impact. AI models often amplify these factors.
</aside>

### Embracing Trustworthy AI: The NIST AI RMF 1.0 Framework

Beyond SR 11-7's financial focus, the **NIST AI Risk Management Framework (AI RMF 1.0)** provides a broader, cross-sector lens for managing AI risks and promoting trustworthy AI. This framework complements SR 11-7 by offering a structured approach to identifying, measuring, and managing the unique risks posed by AI systems across their entire lifecycle. You will leverage its taxonomy and attributes to ensure a comprehensive risk assessment.

The NIST AI RMF categorizes trustworthiness attributes as follows:

*   **Validity**: The AI system accurately performs its intended function.
*   **Reliability**: Consistent and stable performance over time.
*   **Safety**: Minimizing harm to individuals, society, or the environment.
*   **Security**: Protecting AI systems from attacks and ensuring data integrity.
*   **Transparency**: Understanding how AI systems arrive at outputs, often through interpretability.
*   **Fairness**: Identifying and mitigating biases to ensure equitable outcomes.
*   **Accountability**: Clear roles and policies for AI risk oversight.
*   **Privacy-Preserving**: Addressing data sensitivity and integrating privacy by design.

<aside class="info">
<b>Why NIST AI RMF is Essential:</b> While SR 11-7 focuses on financial risk, NIST AI RMF expands your view to encompass broader societal and ethical concerns, such as Fairness, Transparency, and Accountability. Both frameworks are crucial for deploying AI responsibly.
</aside>

Understanding these frameworks provides you with the conceptual tools needed to systematically identify and categorize risks. Now, click **Next: Identify AI Risks** to start populating your risk register.

## 5. AI Risk Register: Systematic Identification
Duration: 00:10:00

Now, equipped with the Model and Data Cards and guided by frameworks like SR 11-7 and NIST AI RMF, you begin the systematic identification of risks. You'll use a structured approach, working through key dimensions of AI risk.

The application provides an "AI Risk Register" where you can log identified risks. Each risk entry includes:

*   **Risk ID**: A unique identifier.
*   **Dimension**: The category of AI risk (e.g., Data, Model, System, Human, Organizational). This helps classify where the risk originates.
*   **Category**: A more specific type of risk within the dimension (e.g., Data Quality, Algorithmic Bias).
*   **Description**: A detailed explanation of the risk, its potential cause, and its impact.
*   **Potential Impact** and **Likelihood**: Initial qualitative assessments, which you'll refine later.

The application allows you to "Pre-populate Initial Risks". Click this button to quickly add a comprehensive set of common AI risks related to your Credit Risk Scoring Model scenario. This simulates a thorough initial brainstorming and identification process.

After clicking the button, you'll see the **Current AI Risk Register** populated with numerous risks. Review this table to understand the types of risks identified across the different dimensions.

<aside class="positive">
<b>The Value of Systematic Identification:</b> Systematically identifying risks across dimensions (Data, Model, System, Human, Organizational) ensures a holistic assessment. It prevents overlooking critical failure points and helps in building a comprehensive risk profile, which is a cornerstone of effective risk management.
</aside>

You also have the option to "Manually Add a New Risk" using the expander section. If you think of a unique risk not covered by the pre-populated list, you can add it here. Select a `Dimension`, input a `Category` and `Description`, and assign initial `Potential Impact` and `Likelihood`.

Once you've reviewed the identified risks, click **Next: Assess Risk Severity** to proceed to the next stage.

## 6. AI Risk Register: Severity Assessment
Duration: 00:08:00

With all potential risks identified, your next crucial step as a Risk Manager is to assess their severity. This involves assigning qualitative ratings for "Potential Impact" and "Likelihood" to each risk, typically as Low, Medium, or High. These ratings are then combined to calculate a numerical "Risk Score" using the formula $Risk = Impact \times Likelihood$.

This process allows you to prioritize risks, focusing mitigation efforts on those with the highest scores.

The application provides an "Auto-Assess Key Risks" button. Click this to automatically assign Impact and Likelihood ratings to the pre-populated risks and update their Risk Scores.

After auto-assessing, the **AI Risk Register with Assessed Risks** will be displayed, sorted by "Risk Score" in descending order. This immediately highlights the highest-priority risks.

<aside class="positive">
<b>Prioritization through Assessment:</b> As a Risk Manager, assigning Impact and Likelihood ratings is not merely a bureaucratic task. It's how you prioritize. High-scoring risks demand immediate attention and resources, ensuring that your mitigation efforts are strategically focused on the most significant threats to the AI model and the bank.
</aside>

The application also allows you to refine the impact and likelihood for any individual risk. Use the `Select Risk ID to Assess/Update` dropdown to choose a specific risk, and then adjust its `Potential Impact` and `Likelihood` using the respective select boxes. Click **Update Risk Severity** to apply your changes.

Once you are satisfied with the risk assessments, click **Next: Visualize Risk Landscape** to see your risks in a graphical format.

## 7. Visualizing the Risk Landscape: The AI Risk Matrix
Duration: 00:07:00

To effectively communicate the risk landscape to senior management and other stakeholders, a visual representation is essential. As a Risk Manager, you'll create a Risk Matrix, which plots each identified risk based on its assessed impact and likelihood.

The application automatically generates an **AI Model Risk Matrix: Credit Risk Scoring Model**.

*   The X-axis represents `Likelihood`.
*   The Y-axis represents `Potential Impact`.
*   Each point on the matrix represents an identified risk, labeled with its `Risk ID`.
*   The color and size of the points can indicate the overall risk score.
*   The matrix is typically divided into zones (e.g., green for low risk, yellow for medium, orange for medium-high, and red for high risk) to quickly convey severity.

<aside class="positive">
<b>Interpreting the Risk Matrix:</b> This visual tool immediately highlights high-priority risks that fall into the "red" zone (High Impact, High Likelihood). You can quickly identify critical risks like R007 ("Model Robustness"), R014 ("Loss of Human Oversight"), and R016 ("Lack of Incident Response Plan") as top priorities. This visual summary is an invaluable tool for driving discussions with non-technical stakeholders and securing resources for mitigation.
</aside>

Review the matrix and identify the risks that fall into the higher-severity quadrants. These are the risks that will require the most attention for mitigation.

When you are ready, click **Next: Develop Mitigation Strategies** to start planning how to address these risks.

## 8. AI Risk Register: Strategic Mitigation
Duration: 00:10:00

Identifying and assessing risks is only half the battle. As a Risk Manager, your next critical step is to propose concrete mitigation strategies and controls for the highest-priority risks. These strategies should align with NIST AI RMF's emphasis on control measures and SR 11-7's requirement for robust validation and governance.

The application provides an "Auto-Populate Mitigations for Top Risks" button. Click this to automatically add example mitigation strategies and responsible parties for some of the highest-scoring risks. This gives you a starting point for how to approach mitigation planning.

After auto-populating, the **AI Risk Register with Proposed Mitigations** will be displayed, showing the updated strategies and responsible parties.

<aside class="positive">
<b>Designing Effective Mitigations:</b> Mitigation strategies should be specific, actionable, and assigned to a responsible party. For example, for "Model Robustness" (R007), a strategy might involve "Implement continuous monitoring for concept drift." For "Loss of Human Oversight" (R014), it could be "Establish clear 'human-in-the-loop' checkpoints." These strategies transform identified risks into actionable plans.
</aside>

You can also add or update mitigation strategies for individual risks. Use the `Select Risk ID to Add/Update Mitigation` dropdown, then enter the `Mitigation Strategy Description` and the `Responsible Party`. Click **Add/Update Mitigation Strategy** to save your changes.

Take some time to review the proposed strategies. Once you're comfortable with the mitigation plans, click **Next: Generate Final Report**.

## 9. Comprehensive AI Risk Report
Duration: 00:07:00

The ultimate deliverable of your assessment is a comprehensive AI Risk Register. This living document consolidates all identified risks, their assessment (impact, likelihood, score), and the proposed mitigation strategies. As a Risk Manager, you understand that this register is crucial for ongoing monitoring, auditability, and demonstrating compliance. It serves as the single source of truth for the AI model's risk profile, empowering the organization to manage it effectively throughout its lifecycle.

The application now displays the **Comprehensive AI Model Risk Register: Credit Risk Scoring Model**. This table represents the complete consolidated view of all your work, sorted by risk score.

Additionally, a **Risk Distribution Across AI Dimensions** bar chart is generated. This visualization quickly shows which AI dimensions (e.g., Data, Model, Human) have the highest number of identified risks, offering a high-level overview of where the organization's primary AI risk exposure lies.

<aside class="positive">
<b>The Final Report as a Living Document:</b> This comprehensive register is not a static document. It's a living tool for continuous risk management. It enables ongoing monitoring, facilitates audits, and provides the necessary documentation for the "Effective Challenge" process — a core requirement of SR 11-7. Your work ensures that QuantBank can deploy AI models with confidence and accountability.
</aside>

### Concluding the Assessment: Preparing for Effective Challenge

Your detailed AI Risk Register and associated artifacts (Model Card, Data Card) form the basis for the "Effective Challenge" process. This principle, central to SR 11-7, mandates that objective and informed reviewers critically test models to identify hidden errors, biases, or limitations. By systematically identifying risks, assessing their impact, and proposing mitigations, you've provided the necessary documentation for internal validation teams, auditors, and senior management to rigorously scrutinize the Credit Risk Scoring Model. Your work ensures that QuantBank can deploy AI models with confidence, upholding regulatory compliance and fostering trustworthiness in AI.

This iterative process of identification, assessment, mitigation, and challenge is crucial for continuous improvement and adaptive governance in AI risk management.

Congratulations on completing your AI Model Risk Assessment! If you wish to go through the process again, click **Restart Assessment**.

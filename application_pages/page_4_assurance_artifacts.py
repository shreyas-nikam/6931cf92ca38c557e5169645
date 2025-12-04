
import streamlit as st

def main():
    st.title("Conceptual AI Assurance Artifacts: Model Cards & Data Cards")
    st.markdown("""
    As a Financial Data Engineer or Risk Manager, robust AI assurance relies on comprehensive documentation artifacts that enhance transparency, accountability, and explainability. Two critical examples are **Model Cards** and **Data Cards**. This section outlines their conceptual templates and guidance. These documents are vital for communicating critical information about AI systems to various stakeholders and are integral to effective governance.
    """)

    st.header("Model Cards")
    st.markdown("""
    Model Cards provide a comprehensive summary of an AI model's key facts, enhancing transparency and accountability. They are intended to document a model's performance, behavior, and intended use for various stakeholders, from technical teams to regulators.

    **Key Components of a Model Card:**
    *   **Model Details**:
        *   Model Name, Version, Developer, Date.
        *   Intended Use Cases and Context.
        *   Out-of-Scope Use Cases (Limitations).
    *   **Training Data Characteristics**:
        *   Description of the training dataset(s).
        *   Data collection process and provenance.
        *   Potential biases, sensitive attributes, or demographic information within the data.
    *   **Performance Metrics**:
        *   Quantitative metrics (e.g., accuracy, precision, recall, F1-score) for relevant subgroups.
        *   Fairness metrics (e.g., demographic parity, equalized odds) if applicable.
        *   Performance benchmarks against baselines.
    *   **Ethical Considerations**:
        *   Potential societal impacts, positive and negative.
        *   Risks identified (linking to Risk Register).
        *   Mitigation strategies for ethical concerns.
    *   **Usage Guidelines**:
        *   Instructions for appropriate model deployment and interaction.
        *   Monitoring and maintenance procedures.
        *   Responsible party for model oversight.

    As a Financial Data Engineer, you would typically contribute the technical details of the model, its training data, and performance metrics. As a Risk Manager, you would ensure the ethical considerations and risks are adequately addressed and linked to the broader risk register.
    """)

    st.divider()

    st.header("Data Cards")
    st.markdown("""
    Data Cards are essential for documenting the provenance and characteristics of datasets used in AI. They ensure transparency around data collection, processing, and potential biases, which are critical for addressing data-related risks. For a Financial Data Engineer, this is a core responsibility to ensure data quality and integrity.

    **Key Components of a Data Card:**
    *   **Dataset Overview**:
        *   Dataset Name, Creator, Version, Date.
        *   Purpose of the dataset.
        *   Description of data contents (features, labels).
    *   **Data Collection Process**:
        *   How the data was collected (sources, methods).
        *   Any preprocessing or cleaning steps applied.
        *   Anonymization or privacy-preserving techniques used.
    *   **Data Characteristics**:
        *   Statistics (e.g., distribution of features, missing values).
        *   Demographic or sensitive information present.
        *   Potential biases, limitations, or under-representation.
    *   **Data Provenance and Lineage**:
        *   Origin of the data (where it came from).
        *   History of transformations and modifications.
        *   Data rights and licensing information.
    *   **Maintenance and Updates**:
        *   Frequency of updates.
        *   Responsible party for data stewardship.

    These artifacts are crucial for enabling "effective challenge" and supporting regulatory compliance by providing clear, auditable evidence of responsible AI development and deployment. They directly inform the `Data` and `Model` risk categories and are integral to the `Map` and `Measure` functions of the NIST AI RMF. For a Financial Data Engineer, meticulous data card creation is a key part of ensuring data quality and mitigating data-related risks.
    """)

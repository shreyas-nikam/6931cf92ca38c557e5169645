# QuLab: AI Model Risk Assessment for Credit Risk Scoring

![QuantUniversity Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)

## Project Title and Description

This project, **QuLab: AI Model Risk Assessment for Credit Risk Scoring**, is a hands-on Streamlit application designed for Quantitative Analysts, Data Scientists, and Risk Managers. It simulates a critical scenario at "QuantBank" where users are tasked with conducting a formal risk assessment of a new AI-powered Credit Risk Scoring Model.

The application guides the user through a systematic, interactive workflow, integrating key concepts from industry-standard frameworks like **SR 11-7 (Supervisory Guidance on Model Risk Management)** and the **NIST AI Risk Management Framework (AI RMF 1.0)**. The goal is to ensure the integrity, compliance, and trustworthiness of AI models in financial services.

Users will:
- Understand model and data characteristics through "Model Cards" and "Data Cards".
- Grasp the foundations of AI risk management using SR 11-7 and NIST AI RMF.
- Systematically identify, assess, and document potential AI risks in a structured "Risk Register".
- Visualize the risk landscape using an interactive risk matrix.
- Propose effective mitigation strategies.
- Generate a comprehensive AI Risk Report for stakeholders and auditors.

The lab emphasizes the fundamental principle that **Risk = Impact × Likelihood**, guiding all assessment and prioritization efforts within the application.

## Features

The QuLab application offers a comprehensive suite of features to facilitate a full AI model risk assessment:

*   **Interactive Scenario Setup**: Introduces the role of a Quantitative Analyst at QuantBank and the core mission.
*   **Model Overview & Card Generation**: Displays hypothetical details of a Credit Risk Scoring Model and generates a standardized "AI Model Card" for transparency.
*   **Data Overview & Card Generation**: Presents details of a synthetic credit application dataset and produces a "Data Card" highlighting data provenance, features, and potential biases.
*   **AI Risk Frameworks Explanation**: Provides an overview of SR 11-7 and NIST AI RMF 1.0, explaining their relevance to AI model risk management.
*   **AI Risk Register (Identification)**:
    *   Allows pre-population of typical AI risks across Data, Model, System, Human, and Organizational dimensions.
    *   Enables manual identification and addition of new risks with custom descriptions and categories.
*   **AI Risk Register (Severity Assessment)**:
    *   Automates assessment of key pre-populated risks with predefined impact and likelihood scores.
    *   Allows users to manually select and update the "Potential Impact" and "Likelihood" for any identified risk, dynamically calculating the "Risk Score".
*   **AI Risk Matrix Visualization**: Generates an interactive scatter plot risk matrix to visually represent all assessed risks based on their impact and likelihood, highlighting high-priority risks.
*   **AI Risk Register (Mitigation Strategies)**:
    *   Automates the addition of mitigation strategies for top-priority risks.
    *   Enables users to manually add or update mitigation strategies and assign responsible parties for individual risks.
*   **Comprehensive AI Risk Report**: Generates a final, consolidated AI Risk Register table, sorted by risk score, and provides a distribution chart of risks across different AI dimensions.
*   **Session State Management**: Ensures that all identified risks, assessments, and mitigations persist throughout the user's session, even across different navigation pages.
*   **Intuitive Streamlit UI**: Provides a clean, user-friendly interface with clear navigation and actionable buttons.

## Getting Started

Follow these instructions to set up and run the QuLab application on your local machine.

### Prerequisites

*   Python 3.8+
*   `pip` (Python package installer)

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/quolab-ai-risk-assessment.git
    cd quolab-ai-risk-assessment
    ```
    (Replace `your-username/quolab-ai-risk-assessment` with the actual repository URL if it's hosted.)

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment**:
    *   **On Windows**:
        ```bash
        .\venv\Scripts\activate
        ```
    *   **On macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies**:
    Create a `requirements.txt` file in the root directory with the following content:
    ```
    streamlit>=1.0.0
    pandas>=1.0.0
    matplotlib>=3.0.0
    seaborn>=0.11.0
    ```
    Then, install them:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the Streamlit application:

1.  **Ensure your virtual environment is activated** (as described in the Installation section).
2.  **Navigate to the project root directory** (where `app.py` is located).
3.  **Run the Streamlit application**:
    ```bash
    streamlit run app.py
    ```

    This command will:
    *   Start the Streamlit server.
    *   Open the application in your default web browser (usually at `http://localhost:8501`).
    *   If it doesn't open automatically, copy and paste the URL provided in your terminal into your browser.

4.  **Navigate through the lab**: Use the sidebar on the left to move between the different steps of the AI Risk Assessment. Follow the instructions and interactive elements on each page.

## Project Structure

The project is organized into logical modules to maintain clarity and reusability.

```
quolab-ai-risk-assessment/
├── app.py                      # Main Streamlit application entry point
├── utils.py                    # Helper functions, session state initialization, and core logic (risk operations, plotting)
├── requirements.txt            # Python dependencies
└── application_pages/          # Directory containing individual Streamlit page modules
    ├── page_1_welcome.py       # Welcome & Scenario Setup
    ├── page_2_model_overview.py    # Model Overview & Card
    ├── page_3_data_overview.py     # Data Overview & Card
    ├── page_4_ai_frameworks.py     # AI Risk Frameworks
    ├── page_5_identify_risks.py    # AI Risk Register: Identify Risks
    ├── page_6_assess_severity.py   # AI Risk Register: Assess Risk Severity
    ├── page_7_risk_matrix.py       # AI Risk Matrix Visualization
    ├── page_8_mitigation_strategies.py # AI Risk Register: Mitigation Strategies
    └── page_9_final_report.py      # Final AI Risk Report
```

## Technology Stack

This application is built using the following core technologies and libraries:

*   **Python 3.x**: The primary programming language.
*   **Streamlit**: The open-source app framework used to build the interactive web application.
*   **Pandas**: For data manipulation and management of the AI Risk Register DataFrame.
*   **Matplotlib**: For creating static, interactive, and animated visualizations (e.g., risk matrix, distribution plots).
*   **Seaborn**: Built on Matplotlib, providing a high-level interface for drawing attractive and informative statistical graphics.

## Contributing

This project is primarily a lab exercise. However, if you have suggestions for improvements or encounter issues, feel free to:

1.  **Fork the repository**.
2.  **Create a new branch** (`git checkout -b feature/your-feature-name`).
3.  **Make your changes**.
4.  **Commit your changes** (`git commit -m 'Add new feature'`).
5.  **Push to the branch** (`git push origin feature/your-feature-name`).
6.  **Open a Pull Request**.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
(Note: You would need to create a `LICENSE` file in your repository.)

## Contact

For any questions or feedback, please reach out:

*   **Your Name/QuantUniversity Team**
*   **GitHub**: [Your GitHub Profile/Organization](https://github.com/your-username)
*   **Email**: [your.email@example.com](mailto:your.email@example.com)

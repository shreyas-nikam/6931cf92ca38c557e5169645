# AI Model Risk Register & Mitigation Planner - QuLab

![QuLab Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)

## Project Title

**AI Model Risk Register & Mitigation Planner: Principles of AI Risk and Assurance**

## Project Description

This Streamlit application serves as an interactive laboratory tool for identifying, assessing, mitigating, and continuously monitoring risks associated with Artificial Intelligence (AI) models. It is designed to provide a practical guide for risk managers, data engineers, AI ethicists, compliance officers, and model validators in regulated environments, particularly financial institutions.

The application deeply integrates foundational AI risk management frameworks, including the **NIST AI Risk Management Framework (AI RMF 1.0)** and the **SR 11-7 (Model Risk Management Guidance)**, to offer a structured approach to AI assurance. Users will explore a multidimensional AI risk taxonomy, simulate a dynamic AI Risk Register, visualize risk landscapes, and understand the importance of AI assurance artifacts like Model Cards and Data Cards. The goal is to ensure the responsible deployment and continuous assurance of AI systems by applying robust governance and risk management practices.

## Features

This application offers the following key functionalities:

*   **Comprehensive Home Page**:
    *   Detailed introduction to AI model risk management.
    *   Clear learning objectives and target audience identification.
    *   Contextualization of foundational frameworks (SR 11-7, NIST AI RMF).
    *   Detailed explanation of a multidimensional AI Risk Taxonomy (Data, Model, System, Human, Organizational risks).
    *   Conceptual overview of risk scoring, visualization, and assurance artifacts.
*   **Dynamic AI Risk Register**:
    *   **Synthetic Data Generation**: Quickly populate the register with configurable numbers of synthetic AI risk entries to simulate real-world scenarios.
    *   **CRUD Operations**: Add new risks, edit existing risk details, and delete risks (conceptual, not implemented in the provided code but a common extension).
    *   **Risk Priority Scoring**: Automatically calculates a `Risk_Priority_Score` based on assessed `Likelihood` and `Impact` using a quantitative matrix.
    *   **Status Tracking**: Update the mitigation `Status` of individual risks (e.g., Identified, In Progress, Mitigated, Monitored).
    *   Interactive display of the full risk register.
*   **Interactive Risk Dashboard**:
    *   **Risk Category Distribution**: Visualizes the spread of risks across different categories (Data, Model, System, Human, Organizational).
    *   **Likelihood vs. Impact Heatmap**: Provides a high-level overview of the overall risk profile, highlighting high-priority areas.
    *   **Risk Status Overview**: Shows the current progress of risk mitigation efforts.
    *   **Framework Alignment**: Visualizes the distribution of risks mapped against **NIST AI RMF Functions** (Govern, Map, Measure, Manage) and **SR 11-7 Pillars** (Development/Implementation, Validation, Governance, Ongoing Monitoring).
*   **Conceptual AI Assurance Artifacts**:
    *   Dedicated section outlining the key components and importance of **Model Cards** and **Data Cards** as critical documentation for transparency, accountability, and explainability in AI systems.
*   **Comprehensive Risk Report Generation**:
    *   Generates a detailed, Markdown-formatted summary report of the entire AI Risk Register, including risk summaries by category, priority, status, top high-priority risks, and framework adherence. This report is ideal for stakeholder communication and governance.

## Getting Started

Follow these instructions to set up and run the Streamlit application on your local machine.

### Prerequisites

*   Python 3.8+
*   `pip` (Python package installer)

### Installation

1.  **Clone the Repository (or download the files):**
    If this were a Git repository, you would clone it:
    ```bash
    git clone <repository_url_here>
    cd ai-risk-register-qulab
    ```
    For this lab, ensure you have all the provided Python files (`app.py` and the contents of `application_pages/`) in a single directory.

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Dependencies:**
    Create a `requirements.txt` file in the root directory of your project with the following content:
    ```
    streamlit>=1.30.0
    pandas>=2.0.0
    numpy>=1.20.0
    matplotlib>=3.5.0
    seaborn>=0.11.0
    plotly>=5.0.0
    Faker>=18.0.0
    ```
    Then install them:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the Streamlit Application:**
    Navigate to the project's root directory in your terminal (where `app.py` is located) and execute:
    ```bash
    streamlit run app.py
    ```

2.  **Access the Application:**
    Your web browser will automatically open a new tab displaying the Streamlit application (usually at `http://localhost:8501`). If it doesn't, copy and paste the URL from your terminal into your browser.

3.  **Navigate and Interact:**
    *   Use the **sidebar navigation** to switch between different sections: "Home", "AI Risk Register", "Risk Dashboard", "Assurance Artifacts", and "Risk Report".
    *   In the **"AI Risk Register"** page, start by generating synthetic data to populate the register. You can then add new risks or edit existing ones.
    *   Visit the **"Risk Dashboard"** to see interactive visualizations update with your register data.
    *   Explore the conceptual guidance on **"Assurance Artifacts"**.
    *   Generate a detailed summary report from the **"Risk Report"** page.

## Project Structure

The project is organized into modular Python files for better maintainability and clarity.

```
.
├── app.py                      # Main Streamlit application file, handles navigation and core logic/functions.
├── requirements.txt            # Lists all Python dependencies.
├── README.md                   # This file.
└── application_pages/          # Directory containing individual application page components.
    ├── home.py                 # Defines the content for the 'Home' page.
    ├── ai_risk_register.py     # Defines the content and interactive elements for the 'AI Risk Register' page.
    ├── risk_dashboard.py       # Defines the visualizations for the 'Risk Dashboard' page.
    ├── risk_report.py          # Defines the report generation for the 'Risk Report' page.
    └── assurance_artifacts.py  # Defines the content for the 'Conceptual AI Assurance Artifacts' page.
```

## Technology Stack

*   **Python**: The core programming language for the application logic.
*   **Streamlit**: The framework used to build the interactive web application and user interface.
*   **Pandas**: Essential for data manipulation, storage (DataFrames for the risk register), and analysis.
*   **Plotly Express**: Used for generating interactive and insightful data visualizations on the risk dashboard.
*   **Faker**: Utilized to generate realistic synthetic data for populating the AI Risk Register.
*   **NumPy**: A foundational library for numerical operations, often used by Pandas.
*   **Matplotlib / Seaborn**: Imported for potential future basic plotting, though Plotly is currently used for dashboard visualizations.

## Contributing

While this is a lab project, contributions are always welcome to enhance its functionality or educational value. If you wish to contribute:

1.  Fork the repository (if it were hosted on GitHub).
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Make your changes and commit them (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

Please ensure your code adheres to good practices, includes appropriate comments, and passes any existing tests (if applicable).

## License

This project is licensed under the MIT License - see the `LICENSE` file for details (or assume MIT if no explicit file is provided, as is common for educational/lab projects).

## Contact

For questions, feedback, or collaborations related to this project or other AI risk and assurance topics, please reach out to:

*   **Organization**: QuantUniversity
*   **Email**: info@quantuniversity.com
*   **Website**: [https://www.quantuniversity.com](https://www.quantuniversity.com)

---
Developed as part of "Lab 1: Principles of AI Risk and Assurance - Clone" at QuLab.

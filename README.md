This comprehensive `README.md` provides all the necessary information for users and developers interacting with the Streamlit AI Model Risk Register application.

---

# QuLab: AI Model Risk Register & Assurance Lab

![Streamlit App Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)

## Project Title and Description

**QuLab: AI Model Risk Register & Assurance Lab** is an interactive Streamlit application designed for risk managers, financial data engineers, and compliance officers. It provides a practical, hands-on environment to understand, establish, and manage an AI Model Risk Register, focusing on the responsible deployment and continuous assurance of AI systems in regulated environments, such as financial institutions.

This lab simulates an end-to-end workflow, guiding users through key concepts from foundational frameworks like **SR 11-7** and the **NIST AI Risk Management Framework (AI RMF)**. It demonstrates how to apply a structured AI risk taxonomy, assess risk likelihood and impact, track mitigation efforts, and generate comprehensive risk reports. The application aims to provide a story-driven experience, mirroring actual tasks performed in real-world AI risk management roles.

## Features

The application offers a rich set of features to facilitate AI risk management:

*   **Conceptual Foundations**: Detailed explanations of AI risk taxonomy (Data, Model, System, Human, Organizational), SR 11-7, and NIST AI RMF 1.0.
*   **Synthetic Data Generation**: Ability to generate a configurable number of synthetic AI risk entries to populate the register for demonstration and testing purposes.
*   **Interactive AI Risk Register**:
    *   View, add, edit, and delete individual AI risk entries.
    *   Automatically calculates `Risk_Priority_Score` based on `Likelihood` and `Impact`.
    *   Tracks `Mitigation_Controls`, `Response_Plan`, `Responsible_Party`, and `Status` for each risk.
    *   Maps risks to **NIST AI RMF Functions** (Govern, Map, Measure, Manage) and **SR 11-7 Pillars** (Development/Implementation, Validation, Governance, Ongoing Monitoring).
*   **Comprehensive Risk Dashboard**:
    *   Interactive visualizations (bar charts, heatmaps, pie charts) to show:
        *   Distribution of risks by category.
        *   Likelihood vs. Impact heatmap for overall risk profile.
        *   Current status of AI risks.
        *   Distribution of risks across NIST AI RMF Functions and SR 11-7 Pillars.
*   **Dynamic Risk Status Tracking**: Update the status of individual risks (Identified, In Progress, Mitigated, Monitored) to reflect mitigation progress.
*   **Conceptual AI Assurance Artifacts**: Explores the importance and structure of Model Cards and Data Cards as key transparency and accountability tools.
*   **Detailed Risk Report Generation**: Generate a Markdown-formatted summary report of the entire AI Risk Register, suitable for stakeholders and regulatory reviews.
*   **Multi-Page Navigation**: Intuitive sidebar navigation to switch between different sections of the lab.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

*   Python 3.8+
*   `pip` (Python package installer)

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/quolab-ai-risk-assurance.git
    cd quolab-ai-risk-assurance
    ```
    *(Note: Replace `your-username/quolab-ai-risk-assurance.git` with the actual repository URL if this is hosted publicly.)*

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    *   **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies:**
    The application uses several Python libraries. It's good practice to create a `requirements.txt` file first.

    Create a `requirements.txt` file in the root directory of your project with the following content:

    ```
    streamlit>=1.30.0
    pandas>=2.0.0
    numpy>=1.20.0
    Faker>=18.0.0
    plotly>=5.0.0
    matplotlib>=3.0.0
    seaborn>=0.11.0
    ```

    Then install them:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the Streamlit application:

1.  **Ensure your virtual environment is activated.**
2.  **Navigate to the project's root directory** (where `app.py` is located).
3.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

    This command will open the application in your default web browser (usually at `http://localhost:8501`).

### Basic Workflow:

1.  **Home Page**:
    *   Read about the project's context, learning objectives, target audience, and foundational AI risk frameworks (SR 11-7, NIST AI RMF).
    *   Understand the **AI Risk Taxonomy**.
    *   **Generate Synthetic Data**: Input the number of risks and click "Generate Synthetic Data" to populate your initial AI Risk Register. This is the crucial first step.
    *   Observe the initial data exploration and the `Risk_Priority_Score` calculation.
2.  **AI Risk Register Page**:
    *   View the full register.
    *   **Add New Risk**: Manually input details for a new risk.
    *   **Edit Existing Risk**: Select a `Risk_ID` to modify its details.
    *   **Update Risk Status**: Change the `Status` of a risk as mitigation progresses.
3.  **Risk Dashboard Page**:
    *   Explore interactive charts and graphs that visualize the distribution of risks by category, likelihood vs. impact, status, and alignment with NIST AI RMF and SR 11-7 frameworks.
    *   A demonstration of updating risk status is also available here.
4.  **Assurance Artifacts Page**:
    *   Learn about the conceptual importance and key components of **Model Cards** and **Data Cards** in AI assurance.
5.  **Risk Report Page**:
    *   Click "Generate Comprehensive Risk Report" to create a markdown-formatted summary report based on the current state of your AI Risk Register. This report includes various summaries and a list of top-priority risks.

## Project Structure

The project is organized into modular files for clarity and maintainability:

```
quolab-ai-risk-assurance/
├── app.py                            # Main Streamlit application entry point and page routing.
├── utils.py                          # Contains core utility functions for data generation, risk calculation, and report generation.
├── requirements.txt                  # Lists all Python dependencies.
├── README.md                         # This file.
└── application_pages/                # Directory for individual Streamlit pages.
    ├── page_1_home.py                # Introduction, theoretical concepts, and synthetic data generation.
    ├── page_2_risk_register.py       # CRUD operations for the AI Risk Register (add, edit, view, update status).
    ├── page_3_risk_dashboard.py      # Interactive visualizations and risk analytics dashboard.
    ├── page_4_assurance_artifacts.py # Explains Model Cards and Data Cards conceptually.
    └── page_5_risk_report.py         # Generates a comprehensive summary report of the risk register.
```

## Technology Stack

*   **Python**: The core programming language.
*   **Streamlit**: For building the interactive web application and user interface.
*   **Pandas**: For data manipulation and management of the AI Risk Register DataFrame.
*   **Plotly Express**: For generating interactive and informative data visualizations.
*   **Faker**: For generating realistic synthetic data entries for the risk register.
*   **NumPy**: For numerical operations, implicitly used by Pandas.
*   **Matplotlib & Seaborn**: Imported for potential use, but Plotly Express is primarily utilized for dashboard visualizations.

## Contributing

This is a lab project intended for learning and demonstration. Contributions are welcome! If you have ideas for improvements, new features, or bug fixes, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

Please ensure your code adheres to good practices and includes appropriate comments and documentation.

## License

This project is open-source and available under the MIT License. See the `LICENSE` file for more details.

## Contact

For questions, suggestions, or collaboration opportunities, please reach out:

*   **Project Lead**: QuantUniversity
*   **Website**: [www.quantuniversity.com](https://www.quantuniversity.com)
*   **Email**: info@quantuniversity.com

---

import streamlit as st
from utils import go_to_page # Import the navigation helper

st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()

st.markdown("""
In this lab, you will step into the shoes of a Quantitative Analyst at QuantBank, tasked with a critical mission: to conduct a formal risk assessment of a new AI-powered Credit Risk Scoring Model. This model is poised to automate loan approvals and flag high-risk applicants, making its integrity and compliance paramount.

This application will guide you through a systematic process, from understanding the model and its data to identifying, assessing, mitigating, and reporting AI risks. All steps are framed within the context of stringent financial regulations (SR 11-7) and best practices for trustworthy AI (NIST AI RMF 1.0). Each interactive step reflects a real-world task you would perform, moving you closer to ensuring responsible AI deployment at QuantBank.
""")

# Page names for navigation
pages = [
    "Welcome & Scenario Setup",
    "Model Overview & Card",
    "Data Overview & Card",
    "AI Risk Frameworks",
    "AI Risk Register: Identify Risks",
    "AI Risk Register: Assess Risk Severity",
    "AI Risk Matrix Visualization",
    "AI Risk Register: Mitigation Strategies",
    "Final AI Risk Report"
]

# Initialize current_sidebar_page_index if not already present
if "current_sidebar_page_index" not in st.session_state:
    st.session_state.current_sidebar_page_index = 0

page_selection = st.sidebar.selectbox(
    label="Navigation",
    options=pages,
    index=st.session_state.current_sidebar_page_index,
    key="sidebar_navigation"
)

# Update session state if sidebar selection changes
if pages.index(page_selection) != st.session_state.current_sidebar_page_index:
    st.session_state.current_sidebar_page_index = pages.index(page_selection)
    st.rerun()


if page_selection == "Welcome & Scenario Setup":
    from application_pages.page_1_welcome import main
    main()
elif page_selection == "Model Overview & Card":
    from application_pages.page_2_model_overview import main
    main()
elif page_selection == "Data Overview & Card":
    from application_pages.page_3_data_overview import main
    main()
elif page_selection == "AI Risk Frameworks":
    from application_pages.page_4_ai_frameworks import main
    main()
elif page_selection == "AI Risk Register: Identify Risks":
    from application_pages.page_5_identify_risks import main
    main()
elif page_selection == "AI Risk Register: Assess Risk Severity":
    from application_pages.page_6_assess_severity import main
    main()
elif page_selection == "AI Risk Matrix Visualization":
    from application_pages.page_7_risk_matrix import main
    main()
elif page_selection == "AI Risk Register: Mitigation Strategies":
    from application_pages.page_8_mitigation_strategies import main
    main()
elif page_selection == "Final AI Risk Report":
    from application_pages.page_9_final_report import main
    main()

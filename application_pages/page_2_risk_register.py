
import streamlit as st
import pandas as pd
from utils import calculate_risk_priority_score, update_risk_status

def main():
    st.title("AI Risk Register Management")
    st.markdown("""
    As a Risk Manager, this is your primary tool for actively managing the organization's AI risks. Here, you can perform crucial operations like adding new risks, modifying existing risk details, and updating their mitigation status. Maintaining an accurate and up-to-date register is critical for effective AI risk governance.
    """)

    if 'ai_risk_register_df' not in st.session_state or st.session_state.ai_risk_register_df.empty:
        st.warning("The AI Risk Register is currently empty. Please go to the 'Home' page to generate synthetic data or add risks manually below.")
        st.session_state.ai_risk_register_df = pd.DataFrame(columns=[
            "Risk_ID", "Risk_Description", "Risk_Category", "Likelihood", "Impact",
            "Mitigation_Controls", "Response_Plan", "NIST_AI_RMF_Function",
            "SR_11_7_Pillar", "Responsible_Party", "Status", "Risk_Priority_Score"
        ])


    st.header("Current AI Risk Register")
    st.markdown("""
    Review the current state of your AI Risk Register. You can sort and search through entries to quickly find specific risks or understand the overall risk landscape.
    """)
    st.dataframe(st.session_state.ai_risk_register_df, use_container_width=True)


    st.divider()
    st.header("Add New Risk Entry")
    st.markdown("""
    When a new potential AI risk is identified, you, as a Risk Manager, need to document it thoroughly. Use this section to record all relevant details, which will automatically be incorporated into the register and assigned a priority score.
    """)
    with st.form("add_risk_form"):
        # Automatically determine new Risk_ID
        next_risk_id = 1 if st.session_state.ai_risk_register_df.empty else st.session_state.ai_risk_register_df["Risk_ID"].max() + 1
        st.write(f"**New Risk ID**: {next_risk_id}")

        risk_description = st.text_input("Risk Description", key="add_risk_description")
        risk_category = st.selectbox("Risk Category", ["Data", "Model", "System", "Human", "Organizational"], key="add_risk_category")
        likelihood = st.selectbox("Likelihood", ["Low", "Medium", "High"], key="add_likelihood")
        impact = st.selectbox("Impact", ["Low", "Medium", "High"], key="add_impact")
        mitigation_controls = st.text_area("Mitigation Controls", key="add_mitigation_controls")
        response_plan = st.text_area("Response Plan", key="add_response_plan")
        nist_ai_rmf_function = st.selectbox("NIST AI RMF Function", ["Govern", "Map", "Measure", "Manage"], key="add_nist_ai_rmf_function")
        sr_11_7_pillar = st.selectbox("SR 11-7 Pillar", ["Development/Implementation", "Validation", "Governance", "Ongoing Monitoring"], key="add_sr_11_7_pillar")
        responsible_party = st.text_input("Responsible Party", key="add_responsible_party")
        status = st.selectbox("Status", ["Identified", "In Progress", "Mitigated", "Monitored"], key="add_status")

        add_submitted = st.form_submit_button("Add New Risk")

        if add_submitted:
            if not risk_description or not mitigation_controls or not response_plan or not responsible_party:
                st.error("Please fill in all required fields for Risk Description, Mitigation Controls, Response Plan, and Responsible Party.")
            else:
                new_risk_data = {
                    "Risk_ID": next_risk_id,
                    "Risk_Description": risk_description,
                    "Risk_Category": risk_category,
                    "Likelihood": likelihood,
                    "Impact": impact,
                    "Mitigation_Controls": mitigation_controls,
                    "Response_Plan": response_plan,
                    "NIST_AI_RMF_Function": nist_ai_rmf_function,
                    "SR_11_7_Pillar": sr_11_7_pillar,
                    "Responsible_Party": responsible_party,
                    "Status": status
                }
                new_risk_df = pd.DataFrame([new_risk_data])
                new_risk_df["Risk_Priority_Score"] = calculate_risk_priority_score(new_risk_df)
                st.session_state.ai_risk_register_df = pd.concat([st.session_state.ai_risk_register_df, new_risk_df], ignore_index=True)
                st.success(f"Risk ID {next_risk_id} added successfully!")
                st.rerun() # Rerun to clear form and update dataframe


    st.divider()
    st.header("Edit Existing Risk")
    st.markdown("""
    As more information becomes available or as the understanding of a risk evolves, you, as a Risk Manager, need to update its details. Select a `Risk_ID` to load its current information, make your changes, and save them to keep the register accurate.
    """)
    if not st.session_state.ai_risk_register_df.empty:
        risk_ids = st.session_state.ai_risk_register_df["Risk_ID"].unique().tolist()
        selected_risk_id_edit = st.selectbox("Select Risk ID to Edit", risk_ids, key="edit_risk_id")

        if selected_risk_id_edit is not None:
            current_risk_details = st.session_state.ai_risk_register_df[st.session_state.ai_risk_register_df["Risk_ID"] == selected_risk_id_edit].iloc[0]

            with st.form("edit_risk_form"):
                st.write(f"**Editing Risk ID**: {selected_risk_id_edit}")
                edit_risk_description = st.text_input("Risk Description", value=current_risk_details["Risk_Description"], key="edit_risk_description")
                edit_risk_category = st.selectbox("Risk Category", ["Data", "Model", "System", "Human", "Organizational"], index=["Data", "Model", "System", "Human", "Organizational"].index(current_risk_details["Risk_Category"]), key="edit_risk_category")
                edit_likelihood = st.selectbox("Likelihood", ["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(current_risk_details["Likelihood"]), key="edit_likelihood")
                edit_impact = st.selectbox("Impact", ["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(current_risk_details["Impact"]), key="edit_impact")
                edit_mitigation_controls = st.text_area("Mitigation Controls", value=current_risk_details["Mitigation_Controls"], key="edit_mitigation_controls")
                edit_response_plan = st.text_area("Response Plan", value=current_risk_details["Response_Plan"], key="edit_response_plan")
                edit_nist_ai_rmf_function = st.selectbox("NIST AI RMF Function", ["Govern", "Map", "Measure", "Manage"], index=["Govern", "Map", "Measure", "Manage"].index(current_risk_details["NIST_AI_RMF_Function"]), key="edit_nist_ai_rmf_function")
                edit_sr_11_7_pillar = st.selectbox("SR 11-7 Pillar", ["Development/Implementation", "Validation", "Governance", "Ongoing Monitoring"], index=["Development/Implementation", "Validation", "Governance", "Ongoing Monitoring"].index(current_risk_details["SR_11_7_Pillar"]), key="edit_sr_11_7_pillar")
                edit_responsible_party = st.text_input("Responsible Party", value=current_risk_details["Responsible_Party"], key="edit_responsible_party")
                edit_status = st.selectbox("Status", ["Identified", "In Progress", "Mitigated", "Monitored"], index=["Identified", "In Progress", "Mitigated", "Monitored"].index(current_risk_details["Status"]), key="edit_status")

                edit_submitted = st.form_submit_button("Save Edited Risk")

                if edit_submitted:
                    if not edit_risk_description or not edit_mitigation_controls or not edit_response_plan or not edit_responsible_party:
                        st.error("Please fill in all required fields for Risk Description, Mitigation Controls, Response Plan, and Responsible Party.")
                    else:
                        idx_to_update = st.session_state.ai_risk_register_df[st.session_state.ai_risk_register_df["Risk_ID"] == selected_risk_id_edit].index[0]
                        st.session_state.ai_risk_register_df.loc[idx_to_update, "Risk_Description"] = edit_risk_description
                        st.session_state.ai_risk_register_df.loc[idx_to_update, "Risk_Category"] = edit_risk_category
                        st.session_state.ai_risk_register_df.loc[idx_to_update, "Likelihood"] = edit_likelihood
                        st.session_state.ai_risk_register_df.loc[idx_to_update, "Impact"] = edit_impact
                        st.session_state.ai_risk_register_df.loc[idx_to_update, "Mitigation_Controls"] = edit_mitigation_controls
                        st.session_state.ai_risk_register_df.loc[idx_to_update, "Response_Plan"] = edit_response_plan
                        st.session_state.ai_risk_register_df.loc[idx_to_update, "NIST_AI_RMF_Function"] = edit_nist_ai_rmf_function
                        st.session_state.ai_risk_register_df.loc[idx_to_update, "SR_11_7_Pillar"] = edit_sr_11_7_pillar
                        st.session_state.ai_risk_register_df.loc[idx_to_update, "Responsible_Party"] = edit_responsible_party
                        st.session_state.ai_risk_register_df.loc[idx_to_update, "Status"] = edit_status
                        # Recalculate priority score for the updated row
                        st.session_state.ai_risk_register_df.loc[idx_to_update, "Risk_Priority_Score"] = calculate_risk_priority_score(st.session_state.ai_risk_register_df.loc[[idx_to_update]])
                        st.success(f"Risk ID {selected_risk_id_edit} updated successfully!")
                        st.rerun() # Rerun to update dataframe and potentially clear form


    st.divider()
    st.header("Update Risk Status")
    st.markdown("""
    As mitigation strategies are implemented, you, as a Risk Manager, need to update the status of each risk. This allows for clear tracking of progress and informs stakeholders about the current state of risk resolution.
    """)
    if not st.session_state.ai_risk_register_df.empty:
        risk_ids_for_status_update = st.session_state.ai_risk_register_df["Risk_ID"].unique().tolist()
        selected_risk_id_status = st.selectbox("Select Risk ID to update status", risk_ids_for_status_update, key="update_risk_id_status")
        new_status_input = st.selectbox("New Status", ["Identified", "In Progress", "Mitigated", "Monitored"], key="new_status_input")

        if st.button("Update Risk Status", key="update_status_button"):
            # Ensure we pass a copy to avoid SettingWithCopyWarning if not needed, but update_risk_status handles the main df.
            # update_risk_status directly modifies the df, so pass session_state.ai_risk_register_df
            st.session_state.ai_risk_register_df = update_risk_status(st.session_state.ai_risk_register_df, selected_risk_id_status, new_status_input)
            st.rerun() # Rerun to update dataframe
    else:
        st.info("No risks in the register to update. Please add or generate some first.")

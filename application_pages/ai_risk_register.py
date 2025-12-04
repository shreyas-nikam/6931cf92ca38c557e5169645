import streamlit as st
import pandas as pd

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

    st.subheader("Current AI Risk Register")
    if not st.session_state.ai_risk_register_df.empty:
        st.dataframe(st.session_state.ai_risk_register_df, use_container_width=True)
    else:
        st.info("The AI Risk Register is currently empty. Generate some synthetic data or add a new risk to get started.")

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
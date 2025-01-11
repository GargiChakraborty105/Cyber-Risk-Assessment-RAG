# import pandas as pd

# # Load datasets
# incident_history = pd.read_excel("datasets/incident_history.xlsx")
# mock_tests = pd.read_excel("datasets/mock_tests.xlsx")
# user_behavior = pd.read_excel("datasets/user_behavior.xlsx")

# # Merge datasets
# merged_data = pd.merge(user_behavior, mock_tests, on="Employee_ID", how="outer")
# merged_data = pd.merge(merged_data, incident_history, on="Employee_ID", how="outer")

# # Ensure that columns with numeric data are correctly cast to their respective types
# merged_data['Severity'] = pd.to_numeric(merged_data['Severity'], errors='coerce')
# merged_data['Resolution_Time_Days'] = pd.to_numeric(merged_data['Resolution_Time_Days'], errors='coerce')
# merged_data['Score_Percentage'] = pd.to_numeric(merged_data['Score_Percentage'], errors='coerce')
# merged_data['Login_Attempts'] = pd.to_numeric(merged_data['Login_Attempts'], errors='coerce')
# merged_data['Suspicious_Access_Flags'] = pd.to_numeric(merged_data['Suspicious_Access_Flags'], errors='coerce')
# merged_data['Device_Sharing_Instances'] = pd.to_numeric(merged_data['Device_Sharing_Instances'], errors='coerce')

# # Function to assess Employee-Specific Training Needs
# def calculate_employee_training_needs(row):
#     training_needs = []

#     # 1. User Access Behavior Risk
#     if row['Login_Attempts'] > 5:
#         training_needs.append("Recommend additional training on secure login practices.")
#     if row['Suspicious_Access_Flags'] > 0:
#         training_needs.append("Recommend training on identifying and preventing unauthorized access.")
    
#     # 2. Incident History Severity
#     if row['Severity'] >= 3:  # High severity
#         training_needs.append("Recommend incident response and threat management training.")
#     if row['Resolution_Time_Days'] > 7:
#         training_needs.append("Recommend training on incident reporting and faster resolution strategies.")
    
#     # 3. Security Awareness Readiness
#     if row['Score_Percentage'] < 60:
#         training_needs.append("Recommend refresher training on phishing awareness and data privacy.")
    
#     # 4. Device and Data Sharing Behavior
#     if row['Device_Sharing_Instances'] > 2:
#         training_needs.append("Recommend training on secure device management and data protection.")
    
#     return ', '.join(training_needs) if training_needs else "No specific training needs identified."

# # Function to assess Organization-Level Security Gaps & Controls
# def calculate_org_security_gaps(row):
#     security_gaps = []
#     controls_needed = []
#     criticality = []
#     steps_needed = []

#     # 1. User Access Behavior Risk
#     if row['Login_Attempts'] > 5:
#         security_gaps.append("High login attempts detected, indicating potential brute force risks.")
#         controls_needed.append("Strengthen authentication policies, implement multi-factor authentication.")
#         criticality.append("H")
#         steps_needed.append("Implement CAPTCHA, enforce multi-factor authentication (MFA).")
#     elif 3 <= row['Login_Attempts'] <= 5:
#         security_gaps.append("Moderate login attempts detected, indicating potential unauthorized access risks.")
#         controls_needed.append("Monitor login activities and educate users on secure login practices.")
#         criticality.append("L")
#         steps_needed.append("Increase monitoring and provide secure login reminders.")

#     if row['Suspicious_Access_Flags'] > 0:
#         security_gaps.append("Suspicious access flags raised, indicating possible compromised accounts or insider threats.")
#         controls_needed.append("Enhance monitoring and alerts for suspicious access behavior.")
#         criticality.append("H")
#         steps_needed.append("Increase monitoring on login activities, implement anomaly detection systems.")
    
#     # 2. Incident History Severity
#     if row['Severity'] >= 3:
#         security_gaps.append("High-severity incidents detected, indicating possible gaps in employee security awareness.")
#         controls_needed.append("Provide organization-wide training on incident response and security protocols.")
#         criticality.append("H")
#         steps_needed.append("Launch targeted training programs on threat awareness and incident response.")
#     elif 1 <= row['Severity'] < 3:
#         security_gaps.append("Low-severity incidents detected, indicating minor security concerns.")
#         controls_needed.append("Monitor incident patterns and provide basic security awareness.")
#         criticality.append("L")
#         steps_needed.append("Conduct periodic awareness training for low-risk behaviors.")
    
#     if row['Resolution_Time_Days'] > 7:
#         security_gaps.append("Long resolution times observed, indicating inefficiencies in incident management.")
#         controls_needed.append("Implement a more efficient incident response process and training.")
#         criticality.append("M")
#         steps_needed.append("Revise incident management process to reduce response time, provide additional training.")
    
#     # 3. Security Awareness Readiness
#     if row['Score_Percentage'] < 60:
#         security_gaps.append("Low security awareness based on mock test performance.")
#         controls_needed.append("Implement company-wide refresher training on security topics such as phishing and secure login.")
#         criticality.append("H")
#         steps_needed.append("Increase frequency of phishing simulations, provide more in-depth security awareness courses.")
#     elif 50 <= row['Score_Percentage'] < 60:
#         security_gaps.append("Moderate security awareness based on mock test performance.")
#         controls_needed.append("Provide additional resources and minor refresher training.")
#         criticality.append("L")
#         steps_needed.append("Share online resources and conduct optional refresher sessions.")
    
#     # 4. Device and Data Sharing Behavior
#     if row['Device_Sharing_Instances'] > 2:
#         security_gaps.append("Frequent device sharing observed, which may violate security policies.")
#         controls_needed.append("Enforce stricter device management and access control policies.")
#         criticality.append("M")
#         steps_needed.append("Implement policies restricting device sharing, enforce encryption on shared devices.")
#     elif 1 <= row['Device_Sharing_Instances'] <= 2:
#         security_gaps.append("Low levels of device sharing observed, which could lead to minor security risks.")
#         controls_needed.append("Educate employees on risks of device sharing and best practices.")
#         criticality.append("L")
#         steps_needed.append("Provide guidance on secure device sharing practices.")

#     return (
#         ', '.join(security_gaps) if security_gaps else "No organizational security gaps identified.",
#         ', '.join(controls_needed) if controls_needed else "No controls needed.",
#         ', '.join(criticality) if criticality else "No criticality assigned.",
#         ', '.join(steps_needed) if steps_needed else "No steps identified."
#     )

# # Lists to store results for Employee-Specific Training Needs and Organizational Security Gaps
# employee_training_results = []
# org_security_results = []

# # Process each employee and calculate the training needs and security gaps
# for _, row in merged_data.iterrows():
#     # Calculate training needs
#     training_needs = calculate_employee_training_needs(row)

#     # Calculate organizational security gaps and controls
#     security_gaps, controls_needed, criticality, steps_needed = calculate_org_security_gaps(row)

#     # Append results
#     employee_training_results.append({
#         "Employee_ID": row['Employee_ID'],
#         "Training Needs": training_needs
#     })

#     org_security_results.append({
#         "Security Gaps": security_gaps,
#         "Controls Needed": controls_needed,
#         "Criticality": criticality,
#         "Steps Needed": steps_needed
#     })

# # Convert the employee-specific training needs results into a DataFrame
# employee_training_df = pd.DataFrame(employee_training_results)

# # Convert the organizational security loopholes results into a DataFrame
# org_security_df = pd.DataFrame(org_security_results)

# # Save the reports to Excel
# with pd.ExcelWriter("reports/employee_specific_training_needs.xlsx") as writer:
#     employee_training_df.to_excel(writer, sheet_name="Training Needs", index=False)

# with pd.ExcelWriter("reports/organizational_security_loopholes.xlsx") as writer:
#     org_security_df.to_excel(writer, sheet_name="Security Gaps & Controls", index=False)

# print("Reports saved as 'employee_specific_training_needs.xlsx' and 'organizational_security_loopholes.xlsx'.")


import os
import pandas as pd
import streamlit as st
import openai
import json
# Set OpenAI API Key (ensure not to hard-code in production)
openai.api_key = "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"

# Function to interact with OpenAI for training needs
def get_training_needs(employee_data):
    prompt = f"""
For the following employee data, provide their training needs in the json format:
- "Employee_ID": {employee_data['Employee_ID']}
- "Training Needs": A string contains detailed and structured sentence that describe of training recommendations. If no training is needed, state "No specific training needs identified." without any reasoning.

Employee Data:
- Login Attempts: {employee_data['Login_Attempts']}
- Suspicious Access Flags: {employee_data['Suspicious_Access_Flags']}
- Severity: {employee_data['Severity']}
- Resolution Time Days: {employee_data['Resolution_Time_Days']}
- Score Percentage: {employee_data['Score_Percentage']}
- Device Sharing Instances: {employee_data['Device_Sharing_Instances']}

Guidelines:
1. If Login Attempts > 5 or Suspicious Access Flags > 0, recommend training on secure login and unauthorized access prevention.
2. If Severity >= 3 or Resolution Time > 7 days, recommend training on incident reporting and faster resolution strategies.
3. If Score Percentage < 60, recommend refresher training on phishing awareness and secure login practices.
4. If Device Sharing Instances > 2, recommend training on secure device management and data protection.
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the model you're using
        messages=[
            {"role": "system", "content": "You are an expert in cybersecurity training needs assessment."},
            {"role": "user", "content": prompt}
        ]
    )
    # print(response['choices'][0]['message']['content'] )
    return response['choices'][0]['message']['content']  # Adjust this for the correct response format

# Function to interact with OpenAI for security gaps and controls
def get_security_gaps(employee_data):
    prompt = f"""
Based on the following employee data, identify security gaps, controls needed, criticality, and specific steps in a structured json format:
Employee Data:
- Login Attempts: {employee_data['Login_Attempts']}
- Suspicious Access Flags: {employee_data['Suspicious_Access_Flags']}
- Severity: {employee_data['Severity']}
- Resolution Time Days: {employee_data['Resolution_Time_Days']}
- Score Percentage: {employee_data['Score_Percentage']}
- Device Sharing Instances: {employee_data['Device_Sharing_Instances']}

Guidelines:
1. If Login Attempts > 5 or Suspicious Access Flags > 0, identify gaps like potential unauthorized access risks. Suggest controls like stronger authentication policies and monitoring.
2. If Severity >= 3 or Resolution Time > 7 days, identify gaps in incident management. Suggest faster resolution processes and training.
3. If Score Percentage < 60, highlight low security awareness. Suggest training and phishing simulations.
4. If Device Sharing Instances > 2, flag policy violations. Suggest stricter device management policies.


Return the result in this structured json format:
- "Security Gaps": A String Description of gaps. If No significant security gaps identified based on employee data, state "No significant security gaps identified based on employee data".
- "Controls Needed": A String that describe Specific controls for addressing the gaps. If No significant security gaps identified based on employee data, state "None".
- "Criticality": Levels (L, M, H). If No significant security gaps identified based on employee data, state "L".
- "Steps Needed": A string that describe Detailed actions to resolve the gaps. If No significant security gaps identified based on employee data, state "None".
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the model you're using
        messages=[
            {"role": "system", "content": "You are an expert in organizational security gap analysis."},
            {"role": "user", "content": prompt}
        ]
    )
    # print(response['choices'][0]['message']['content'] )
    return response['choices'][0]['message']['content']  # Adjust this for the correct response format

# Streamlit App
st.title("Cybersecurity Training and Gap Analysis")

if "employee_training_file" not in st.session_state:
    st.session_state.employee_training_file = None
if "org_security_file" not in st.session_state:
    st.session_state.org_security_file = None

# File uploads
st.sidebar.header("Upload Data")
incident_history_file = st.sidebar.file_uploader("Upload Incident History (Excel)", type=["xlsx"])
mock_tests_file = st.sidebar.file_uploader("Upload Mock Tests (Excel)", type=["xlsx"])
user_behavior_file = st.sidebar.file_uploader("Upload User Behavior (Excel)", type=["xlsx"])

if st.sidebar.button("Process and Generate Reports"):
    st.session_state.org_security_file = None
    st.session_state.employee_training_file = None
    if incident_history_file and mock_tests_file and user_behavior_file:
        # Load datasets
        incident_history = pd.read_excel(incident_history_file)
        mock_tests = pd.read_excel(mock_tests_file)
        user_behavior = pd.read_excel(user_behavior_file)

        # Merge datasets
        merged_data = pd.merge(user_behavior, mock_tests, on="Employee_ID", how="outer")
        merged_data = pd.merge(merged_data, incident_history, on="Employee_ID", how="outer")

        # Ensure numeric data is correctly cast
        numeric_columns = [
            "Severity", 
            "Resolution_Time_Days", 
            "Score_Percentage", 
            "Login_Attempts", 
            "Suspicious_Access_Flags", 
            "Device_Sharing_Instances"
        ]
        for column in numeric_columns:
            merged_data[column] = pd.to_numeric(merged_data[column], errors="coerce")

        # Lists to store results
        employee_training_results = []
        org_security_results = []

        # Process each employee
        for _, row in merged_data.iterrows():
            employee_data = row.to_dict()

            # Get training needs
            training_needs = get_training_needs(employee_data)
            training_needs = training_needs.replace("```", '')
            training_needs = training_needs.replace("json", '')
            print(training_needs)
            employee_training_results.append(json.loads(training_needs))
            # print(employee_training_results)
            # Get security gaps and controls
            security_gaps = get_security_gaps(employee_data)
            security_gaps = security_gaps.replace("```","")
            security_gaps = security_gaps.replace("json", "")
            print(security_gaps)
            org_security_results.append(json.loads(security_gaps))
            # lines = [line for line in security_gaps.split("\n") if line.strip()]  # Remove empty lines
            # # Safely extract data with fallback
            # gap_data = {
            #     "Security Gaps": lines[0].split(": ", 1)[1].strip() if len(lines) > 0 and ": " in lines[0] else "N/A",
            #     "Controls Needed": lines[1].split(": ", 1)[1].strip() if len(lines) > 1 and ": " in lines[1] else "N/A",
            #     "Criticality": lines[2].split(": ", 1)[1].strip() if len(lines) > 2 and ": " in lines[2] else "N/A",
            #     "Steps Needed": lines[3].split(": ", 1)[1].strip() if len(lines) > 3 and ": " in lines[3] else "N/A",
            # }
            # org_security_results.append(gap_data)
        # print(employee_training_results)
        # Convert results to DataFrames
        employee_training_df = pd.DataFrame(employee_training_results)
        org_security_df = pd.DataFrame(org_security_results)

        # Ensure the 'reports' directory exists
        if not os.path.exists("reports"):
            os.makedirs("reports")

        # Save reports in 'reports' directory
        st.session_state.employee_training_file = os.path.join("reports", "employee_specific_training_needs.xlsx")
        st.session_state.org_security_file = os.path.join("reports", "organizational_security_loopholes.xlsx")
        with pd.ExcelWriter(st.session_state.employee_training_file) as writer:
            employee_training_df.to_excel(writer, sheet_name="Training Needs", index=False)

        with pd.ExcelWriter(st.session_state.org_security_file) as writer:
            org_security_df.to_excel(writer, sheet_name="Security Gaps & Controls", index=False)

        st.success("Reports generated successfully!")
        
    else:
        st.error("Please upload all required files.")

# Display download buttons if files are generated
if st.session_state.employee_training_file and st.session_state.org_security_file:
    with open(st.session_state.employee_training_file, "rb") as f:
        st.download_button(
            label="Download Employee Training Needs",
            data=f,
            file_name="employee_specific_training_needs.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    with open(st.session_state.org_security_file, "rb") as f:
        st.download_button(
            label="Download Security Gaps Report",
            data=f,
            file_name="organizational_security_loopholes.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
import pandas as pd

# Load datasets
incident_history = pd.read_excel("datasets/incident_history.xlsx")
mock_tests = pd.read_excel("datasets/mock_tests.xlsx")
user_behavior = pd.read_excel("datasets/user_behavior.xlsx")

# Merge datasets
merged_data = pd.merge(user_behavior, mock_tests, on="Employee_ID", how="outer")
merged_data = pd.merge(merged_data, incident_history, on="Employee_ID", how="outer")

# Ensure that columns with numeric data are correctly cast to their respective types
merged_data['Severity'] = pd.to_numeric(merged_data['Severity'], errors='coerce')
merged_data['Resolution_Time_Days'] = pd.to_numeric(merged_data['Resolution_Time_Days'], errors='coerce')
merged_data['Score_Percentage'] = pd.to_numeric(merged_data['Score_Percentage'], errors='coerce')
merged_data['Login_Attempts'] = pd.to_numeric(merged_data['Login_Attempts'], errors='coerce')
merged_data['Suspicious_Access_Flags'] = pd.to_numeric(merged_data['Suspicious_Access_Flags'], errors='coerce')
merged_data['Device_Sharing_Instances'] = pd.to_numeric(merged_data['Device_Sharing_Instances'], errors='coerce')

# Function to assess Employee-Specific Training Needs
def calculate_employee_training_needs(row):
    training_needs = []

    # 1. User Access Behavior Risk
    if row['Login_Attempts'] > 5:
        training_needs.append("Recommend additional training on secure login practices.")
    if row['Suspicious_Access_Flags'] > 0:
        training_needs.append("Recommend training on identifying and preventing unauthorized access.")
    
    # 2. Incident History Severity
    if row['Severity'] >= 3:  # High severity
        training_needs.append("Recommend incident response and threat management training.")
    if row['Resolution_Time_Days'] > 7:
        training_needs.append("Recommend training on incident reporting and faster resolution strategies.")
    
    # 3. Security Awareness Readiness
    if row['Score_Percentage'] < 60:
        training_needs.append("Recommend refresher training on phishing awareness and data privacy.")
    
    # 4. Device and Data Sharing Behavior
    if row['Device_Sharing_Instances'] > 2:
        training_needs.append("Recommend training on secure device management and data protection.")
    
    return ', '.join(training_needs) if training_needs else "No specific training needs identified."

# Function to assess Organization-Level Security Gaps & Controls
def calculate_org_security_gaps(row):
    security_gaps = []
    controls_needed = []
    criticality = []
    steps_needed = []

    # 1. User Access Behavior Risk
    if row['Login_Attempts'] > 5:
        security_gaps.append("High login attempts detected, indicating potential brute force risks.")
        controls_needed.append("Strengthen authentication policies, implement multi-factor authentication.")
        criticality.append("H")
        steps_needed.append("Implement CAPTCHA, enforce multi-factor authentication (MFA).")
    elif 3 <= row['Login_Attempts'] <= 5:
        security_gaps.append("Moderate login attempts detected, indicating potential unauthorized access risks.")
        controls_needed.append("Monitor login activities and educate users on secure login practices.")
        criticality.append("L")
        steps_needed.append("Increase monitoring and provide secure login reminders.")

    if row['Suspicious_Access_Flags'] > 0:
        security_gaps.append("Suspicious access flags raised, indicating possible compromised accounts or insider threats.")
        controls_needed.append("Enhance monitoring and alerts for suspicious access behavior.")
        criticality.append("H")
        steps_needed.append("Increase monitoring on login activities, implement anomaly detection systems.")
    
    # 2. Incident History Severity
    if row['Severity'] >= 3:
        security_gaps.append("High-severity incidents detected, indicating possible gaps in employee security awareness.")
        controls_needed.append("Provide organization-wide training on incident response and security protocols.")
        criticality.append("H")
        steps_needed.append("Launch targeted training programs on threat awareness and incident response.")
    elif 1 <= row['Severity'] < 3:
        security_gaps.append("Low-severity incidents detected, indicating minor security concerns.")
        controls_needed.append("Monitor incident patterns and provide basic security awareness.")
        criticality.append("L")
        steps_needed.append("Conduct periodic awareness training for low-risk behaviors.")
    
    if row['Resolution_Time_Days'] > 7:
        security_gaps.append("Long resolution times observed, indicating inefficiencies in incident management.")
        controls_needed.append("Implement a more efficient incident response process and training.")
        criticality.append("M")
        steps_needed.append("Revise incident management process to reduce response time, provide additional training.")
    
    # 3. Security Awareness Readiness
    if row['Score_Percentage'] < 60:
        security_gaps.append("Low security awareness based on mock test performance.")
        controls_needed.append("Implement company-wide refresher training on security topics such as phishing and secure login.")
        criticality.append("H")
        steps_needed.append("Increase frequency of phishing simulations, provide more in-depth security awareness courses.")
    elif 50 <= row['Score_Percentage'] < 60:
        security_gaps.append("Moderate security awareness based on mock test performance.")
        controls_needed.append("Provide additional resources and minor refresher training.")
        criticality.append("L")
        steps_needed.append("Share online resources and conduct optional refresher sessions.")
    
    # 4. Device and Data Sharing Behavior
    if row['Device_Sharing_Instances'] > 2:
        security_gaps.append("Frequent device sharing observed, which may violate security policies.")
        controls_needed.append("Enforce stricter device management and access control policies.")
        criticality.append("M")
        steps_needed.append("Implement policies restricting device sharing, enforce encryption on shared devices.")
    elif 1 <= row['Device_Sharing_Instances'] <= 2:
        security_gaps.append("Low levels of device sharing observed, which could lead to minor security risks.")
        controls_needed.append("Educate employees on risks of device sharing and best practices.")
        criticality.append("L")
        steps_needed.append("Provide guidance on secure device sharing practices.")

    return (
        ', '.join(security_gaps) if security_gaps else "No organizational security gaps identified.",
        ', '.join(controls_needed) if controls_needed else "No controls needed.",
        ', '.join(criticality) if criticality else "No criticality assigned.",
        ', '.join(steps_needed) if steps_needed else "No steps identified."
    )

# Lists to store results for Employee-Specific Training Needs and Organizational Security Gaps
employee_training_results = []
org_security_results = []

# Process each employee and calculate the training needs and security gaps
for _, row in merged_data.iterrows():
    # Calculate training needs
    training_needs = calculate_employee_training_needs(row)

    # Calculate organizational security gaps and controls
    security_gaps, controls_needed, criticality, steps_needed = calculate_org_security_gaps(row)

    # Append results
    employee_training_results.append({
        "Employee_ID": row['Employee_ID'],
        "Training Needs": training_needs
    })

    org_security_results.append({
        "Security Gaps": security_gaps,
        "Controls Needed": controls_needed,
        "Criticality": criticality,
        "Steps Needed": steps_needed
    })

# Convert the employee-specific training needs results into a DataFrame
employee_training_df = pd.DataFrame(employee_training_results)

# Convert the organizational security loopholes results into a DataFrame
org_security_df = pd.DataFrame(org_security_results)

# Save the reports to Excel
with pd.ExcelWriter("reports/employee_specific_training_needs.xlsx") as writer:
    employee_training_df.to_excel(writer, sheet_name="Training Needs", index=False)

with pd.ExcelWriter("reports/organizational_security_loopholes.xlsx") as writer:
    org_security_df.to_excel(writer, sheet_name="Security Gaps & Controls", index=False)

print("Reports saved as 'employee_specific_training_needs.xlsx' and 'organizational_security_loopholes.xlsx'.")

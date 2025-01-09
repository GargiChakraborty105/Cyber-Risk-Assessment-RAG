import pandas as pd

# Read data from Excel files
incident_history = pd.read_excel("incident_history.xlsx")
mock_tests = pd.read_excel("mock_tests.xlsx")
user_behavior = pd.read_excel("user_behavior.xlsx")

# Display loaded datasets
print("Incident History Data:")
print(incident_history.head())

print("\nMock Test Data:")
print(mock_tests.head())

print("\nUser Behavior Data:")
print(user_behavior.head())

# Example processing: Assign RAG Ratings
def assign_rag_user_behavior(row):
    if row['Login_Attempts'] > 5 or row['Files_Accessed'] > 50 or row['Suspicious_Access_Flags'] > 1 or \
       row['Device_Sharing_Instances'] > 2 or row['Phishing_Email_Clicks'] > 2:
        return 'Red'
    elif 3 <= row['Login_Attempts'] <= 5 or 30 <= row['Files_Accessed'] <= 50 or row['Suspicious_Access_Flags'] == 1 or \
         1 <= row['Device_Sharing_Instances'] <= 2 or 1 <= row['Phishing_Email_Clicks'] <= 2:
        return 'Amber'
    else:
        return 'Green'

user_behavior['RAG_User_Behavior'] = user_behavior.apply(assign_rag_user_behavior, axis=1)

def assign_rag_mock_tests(row):
    if row['Score_Percentage'] < 60:
        return 'Red'
    elif 60 <= row['Score_Percentage'] < 80:
        return 'Amber'
    else:
        return 'Green'

mock_tests['RAG_Mock_Test'] = mock_tests.apply(assign_rag_mock_tests, axis=1)

def assign_rag_incident_history(row):
    if row['Severity'] == 'Critical':
        return 'Red'
    elif row['Severity'] == 'High' and row['Resolution_Time_Days'] > 7:
        return 'Red'
    elif row['Severity'] == 'High' or (row['Severity'] == 'Medium' and row['Resolution_Time_Days'] > 4):
        return 'Amber'
    else:
        return 'Green'

incident_history['RAG_Incident_History'] = incident_history.apply(assign_rag_incident_history, axis=1)

# Merge all datasets on Employee_ID
combined_data = user_behavior.merge(mock_tests, on='Employee_ID', how='outer').merge(incident_history, on='Employee_ID', how='outer')

# Save the combined data with RAG ratings
combined_data.to_excel("risk_assessment_report.xlsx", index=False)

print("\nRAG Ratings assigned and saved in 'risk_assessment_report.xlsx'.")

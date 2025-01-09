import openai
import pandas as pd

# Load datasets
incident_history = pd.read_excel("incident_history.xlsx")
mock_tests = pd.read_excel("mock_tests.xlsx")
user_behavior = pd.read_excel("user_behavior.xlsx")

# Set your OpenAI API key
openai.api_key = "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"

# Merge datasets
merged_data = pd.merge(user_behavior, mock_tests, on="Employee_ID", how="outer")
merged_data = pd.merge(merged_data, incident_history, on="Employee_ID", how="outer")

# Function to create a detailed prompt for each employee
def create_detailed_prompt(row):
    return f"""
    You are a cybersecurity expert and are tasked with analyzing an employee's behavior and performance to assess their cybersecurity risk. Based on the data provided below, generate a comprehensive Risk Assessment Report for the employee, ensuring that the results are clear, actionable, and aligned with organizational goals for improving cybersecurity.

    **Employee Data**:

    **User Behavior**:
    - Login Attempts: {row['Login_Attempts']}
    - Files Accessed: {row['Files_Accessed']}
    - Suspicious Access Flags: {row['Suspicious_Access_Flags']}
    - Device Sharing Instances: {row['Device_Sharing_Instances']}
    - Phishing Email Clicks: {row['Phishing_Email_Clicks']}

    **Mock Test Performance**:
    - Test Score Percentage: {row['Score_Percentage']}
    - Pass/Fail: {row['Pass_Fail']}

    **Incident History**:
    - Incident Type: {row['Incident_Type']}
    - Incident Severity: {row['Severity']}
    - Resolution Time (days): {row['Resolution_Time_Days']}
    - Status: {row['Status']}

    The following parameters will guide your risk assessment:
    1. **User Access Behavior Risk**: Evaluate login attempts, file access patterns, suspicious activity flags, and phishing email interactions.
    2. **Incident History Severity**: Consider the severity and frequency of incidents, as well as resolution time and recurrence.
    3. **Security Awareness Readiness**: Assess the employee's security awareness based on mock test performance.
    4. **Device and Data Sharing Behavior**: Examine device sharing patterns and incidents of data exfiltration.

    **Please provide the following structured results for this employee**:
    1. **RAG Ratings**: Provide a Red-Amber-Green (RAG) rating for:
        - User Behavior: Assess based on login behavior, suspicious access flags, and phishing email clicks.
        - Incident History: Evaluate based on severity and frequency of past incidents.
        - Security Awareness Readiness: Assess based on test performance (scores, trends).
    2. **Key Risk Factors**: List the most critical security risks identified from the provided data.
        - Focus on areas like weak login patterns, recurring incidents, low security awareness, and improper data handling.
    3. **Overall Risk Level**: Based on all the above factors, assess the overall risk level for the employee (Low, Medium, or High).
    4. **Actionable Recommendations**: Provide clear and actionable recommendations to mitigate risks and improve the employee's security posture. These could include:
        - Training in specific areas (e.g., phishing awareness, secure login).
        - Process improvements (e.g., reducing login attempts, improving incident resolution time).
        - Security policy changes (e.g., restricting device sharing, securing data).
        
    **Make sure to base your recommendations on the data provided, and tailor them specifically to the employee's situation. Ensure that each of your responses is actionable and can be implemented by the employee or organization to reduce cybersecurity risk.**
    """



# List to store detailed results
results = []

# Process each employee
for _, row in merged_data.iterrows():
    try:
        # Generate a unique prompt for the employee
        prompt = create_detailed_prompt(row)

        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" for better results if available
            messages=[
                {"role": "system", "content": "You are a cybersecurity risk assessment expert."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=700,
            temperature=0.7
        )

        # Parse the response
        generated_report = response['choices'][0]['message']['content']
        
        # Extract sections with error handling
        rag_ratings = "Not provided"
        key_risks = "Not provided"
        overall_risk = "Not provided"
        recommendations = "Not provided"

        # Attempt to parse expected sections from the report
        if "RAG Ratings:" in generated_report:
            rag_ratings = generated_report.split("RAG Ratings:")[1].split("\n")[0].strip()
        if "Key Risk Factors:" in generated_report:
            key_risks = generated_report.split("Key Risk Factors:")[1].split("\n")[0].strip()
        if "Overall Risk Level:" in generated_report:
            overall_risk = generated_report.split("Overall Risk Level:")[1].split("\n")[0].strip()
        if "Actionable Recommendations:" in generated_report:
            recommendations = generated_report.split("Actionable Recommendations:")[1].strip()

        # Append structured results
        results.append({
            "Employee_ID": row['Employee_ID'],
            "RAG Ratings": rag_ratings,
            "Key Risk Factors": key_risks,
            "Overall Risk Level": overall_risk,
            "Actionable Recommendations": recommendations,
        })

    except Exception as e:
        print(f"Error processing Employee_ID {row['Employee_ID']}: {e}")

# Convert results into a DataFrame
results_df = pd.DataFrame(results)

# Save the detailed employee-level report to Excel
results_df.to_excel("detailed_risk_assessment_report.xlsx", index=False)

print("Detailed Risk Assessment Report saved to 'detailed_risk_assessment_report.xlsx'.")

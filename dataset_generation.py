import pandas as pd
import random

# Generate sample data for each prompt with extensive random choices for all fields and save as CSVs
def generate_prompt_9_module_2():
    data = {
        'Activity': [random.choice(['Planning', 'Review', 'Execution', 'Monitoring', 'Reporting', 'Risk Assessment', 'Documentation', 'Training']) for _ in range(50)],
        'Milestone': [random.choice(['Initiation', 'Mid-Project Review', 'Completion', 'Feedback', 'Stakeholder Approval', 'Pilot Testing', 'Go-Live']) for _ in range(50)],
        'AI Contribution': [random.choice(['Real-time progress tracking', 'Predictive analysis', 'Automated reporting', 'Anomaly Detection', 'Resource Optimization']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_2_prompt_9.csv', index=False)
    return 'Module_2_prompt_9.csv'

def generate_prompt_4_module_3():
    data = {
        'Stakeholder': [random.choice(['Team Lead', 'Manager', 'Analyst', 'Developer', 'QA', 'Product Owner', 'Scrum Master', 'Sponsor']) for _ in range(50)],
        'Participation Level': [random.randint(1, 10) for _ in range(50)],
        'Common Themes': [random.choice(['Collaboration', 'Project Progress', 'Risk Management', 'Resource Allocation', 'Goal Alignment', 'Performance Issues', 'Strategic Planning']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_3_prompt_4.csv', index=False)
    return 'Module_3_prompt_4.csv'

def generate_prompt_8_module_3():
    data = {
        'Key Requirements': [random.choice([ 'Data Encryption', 'Scalability', 'User Authentication', 'System Reliability', 'API Integration', 'Data Privacy', 'Backup Mechanisms', 'Real-time Analytics', 'Cross-platform Compatibility', 'Performance Optimization']) for _ in range(50)],
        'Open Questions': [random.choice(['Clarification Needed', 'Pending Approval', 'Additional Details Required', 'Resource Allocation Clarification', 'Timeline Adjustment']) for _ in range(50)],
        'Next Steps': [random.choice(['Follow-Up Meeting', 'Document Update', 'Final Approval', 'Prototype Testing', 'Stakeholder Review']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_2_prompt_8.csv', index=False)
    return 'Module_2_prompt_8.csv'

def generate_prompt_9_module_3():
    data = {
        'Excerpt': [random.choice([
            'The system should ensure data encryption.', 'User feedback indicated satisfaction with UI.', 'Multiple stakeholders requested performance improvements.', 'Concerns about data privacy were raised.', 'Scalability was identified as a key factor.', 'User authentication needs clarification.'
        ]) for _ in range(50)],
        'Sentiment': [random.choice(['Positive', 'Neutral', 'Negative', 'Mixed', 'Highly Positive', 'Highly Negative']) for _ in range(50)],
        'Suggested Action': [random.choice(['Acknowledge feedback', 'Address concerns', 'Clarify requirements', 'Improve Communication', 'Review Documentation']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_3_prompt_9.csv', index=False)
    return 'Module_3_prompt_9.csv'

def generate_prompt_10_module_3():
    data = {
        'Requirement': [random.choice(['Functional', 'Non-Functional', 'Business', 'Technical', 'Operational']) for _ in range(50)],
        'Type': [random.choice(['Performance', 'Usability', 'Security', 'Compliance', 'Scalability', 'Accessibility']) for _ in range(50)],
        'Priority': [random.choice(['High', 'Medium', 'Low', 'Critical', 'Optional']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_3_prompt_10.csv', index=False)
    return 'Module_3_prompt_10.csv'

# Generate all CSVs and save file names
csv_files = [
    generate_prompt_9_module_2(),
    generate_prompt_4_module_3(),
    generate_prompt_8_module_3(),
    generate_prompt_9_module_3(),
    generate_prompt_10_module_3()
]

print("CSV files generated and saved successfully:", csv_files)

import pandas as pd
import random

# Generate sample data for each prompt with extensive random choices for all fields and save as CSVs
def generate_prompt_2_module_4():
    data = {
        'Change': [random.choice(['Requirement Added', 'Requirement Removed', 'Requirement Modified']) for _ in range(50)],
        'Reason for Change': [random.choice(['Stakeholder Request', 'Scope Adjustment', 'Regulatory Requirement', 'Technical Feasibility', 'Budget Constraints']) for _ in range(50)],
        'Impact on Deliverables': [random.choice(['Delayed Delivery', 'Increased Cost', 'Revised Timeline', 'Increased Scope']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_4_prompt_2.csv', index=False)
    return 'Module_4_prompt_2.csv'

def generate_prompt_3_module_4():
    data = {
        'Requirement': [random.choice(['Data Security', 'User Authentication', 'Scalability', 'System Reliability', 'API Integration', 'Data Privacy']) for _ in range(50)],
        'Priority Level': [random.choice(['High', 'Medium', 'Low', 'Critical']) for _ in range(50)],
        'Justification': [random.choice(['Business Necessity', 'Technical Feasibility', 'Stakeholder Request', 'Regulatory Requirement']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_4_prompt_3.csv', index=False)
    return 'Module_4_prompt_2.csv'

def generate_prompt_4_module_4():
    data = {
        'Requirement': [random.choice(['Data Security', 'User Authentication', 'Scalability', 'System Reliability', 'API Integration', 'Data Privacy']) for _ in range(50)],
        'Status': [random.choice(['Completed', 'In Progress', 'At Risk']) for _ in range(50)],
        'Risk Mitigation Recommendations': [random.choice(['Increase Resources', 'Reassign Tasks', 'Extend Timeline', 'Conduct Additional Testing']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_4_prompt_4.csv', index=False)
    return 'Module_4_prompt_4.csv'

def generate_prompt_5_module_4():
    data = {
        'Missing Elements': [random.choice(['Data Security Details', 'User Role Definitions', 'Performance Benchmarks', 'Integration Points']) for _ in range(50)],
        'Ambiguities': [random.choice(['Unclear Terminology', 'Vague Scope', 'Unspecified Metrics']) for _ in range(50)],
        'Suggested Improvements': [random.choice(['Clarify Definitions', 'Provide Examples', 'Add Performance Metrics']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_4_prompt_5.csv', index=False)
    return 'Module_4_prompt_5.csv'

def generate_prompt_6_module_4():
    data = {
        'Change Description': [random.choice(['Scope Expansion', 'Timeline Adjustment', 'Budget Increase']) for _ in range(50)],
        'Affected Areas': [random.choice(['Project Schedule', 'Resource Allocation', 'Quality Assurance']) for _ in range(50)],
        'Recommendations': [random.choice(['Extend Deadlines', 'Allocate More Resources', 'Adjust Project Scope']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_4_prompt_6.csv', index=False)
    return 'Module_4_prompt_6.csv'

def generate_prompt_8_module_4():
    data = {
        'Requirement': [random.choice(['Data Encryption', 'Scalability', 'User Authentication', 'System Reliability', 'API Integration']) for _ in range(50)],
        'Dependent Requirements': [random.choice(['API Integration', 'System Reliability', 'User Authentication']) for _ in range(50)],
        'Critical Dependencies': [random.choice(['Yes', 'No']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_4_prompt_8.csv', index=False)
    return 'Module_4_prompt_8.csv'

def generate_prompt_9_module_4():
    data = {
        'Requirement': [random.choice(['Data Encryption', 'Scalability', 'User Authentication', 'System Reliability', 'API Integration']) for _ in range(50)],
        'Validation Status': [random.choice(['Valid', 'Invalid', 'Needs Clarification']) for _ in range(50)],
        'Comments/Recommendations': [random.choice(['Clarify Terminology', 'Add Performance Metrics', 'Refine Scope']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_4_prompt_9.csv', index=False)
    return 'Module_4_prompt_9.csv'

def generate_prompt_10_module_4():
    data = {
        'Conflicting Requirement': [random.choice(['Data Encryption', 'User Authentication', 'API Integration', 'System Scalability']) for _ in range(50)],
        'Impact': [random.choice(['Delays in Timeline', 'Increased Cost', 'Quality Compromise']) for _ in range(50)],
        'Resolution Strategy': [random.choice(['Re-negotiate Requirements', 'Change Project Scope', 'Increase Resources']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_4_prompt_10.csv', index=False)
    return 'Module_4_prompt_10.csv'

def generate_prompt_12_module_4():
    data = {
        'Stakeholder': [random.choice(['Team Lead', 'Manager', 'Analyst', 'Developer', 'Product Owner']) for _ in range(50)],
        'Original Requirement': [random.choice(['Data Security', 'API Integration', 'User Authentication', 'System Scalability']) for _ in range(50)],
        'Consolidated Requirement': [random.choice(['Enhanced Data Encryption', 'Integrated API Security', 'Robust User Authentication']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_4_prompt_12.csv', index=False)
    return 'Module_4_prompt_12.csv'

# Generate all CSVs and save file names
csv_files = [
    generate_prompt_2_module_4(),
    generate_prompt_3_module_4(),
    generate_prompt_4_module_4(),
    generate_prompt_5_module_4(),
    generate_prompt_6_module_4(),
    generate_prompt_8_module_4(),
    generate_prompt_9_module_4(),
    generate_prompt_10_module_4(),
    generate_prompt_12_module_4()
]

print("CSV files generated and saved successfully:", csv_files)


import pandas as pd
import random

# Module 5: Strategy Analysis with Generative AI

def generate_prompt_1_module_5():
    data = {
        'Strengths': [random.choice(['Strong Brand', 'Innovative Product', 'Skilled Team', 'High Market Share']) for _ in range(50)],
        'Weaknesses': [random.choice(['High Costs', 'Limited Reach', 'Low Customer Loyalty', 'Dependence on One Product']) for _ in range(50)],
        'Opportunities': [random.choice(['Emerging Market', 'Partnerships', 'Technological Advancements', 'New Product Lines']) for _ in range(50)],
        'Threats': [random.choice(['Competition', 'Regulatory Changes', 'Economic Downturn', 'Changing Customer Preferences']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_5_prompt_1.csv', index=False)
    return 'Module_5_prompt_1.csv'


def generate_prompt_2_module_5():
    data = {
        'Competitor': [random.choice(['Competitor A', 'Competitor B', 'Competitor C', 'Competitor D']) for _ in range(50)],
        'Key Strengths': [random.choice(['Strong Distribution', 'Established Brand', 'Innovation Focus', 'Loyal Customer Base']) for _ in range(50)],
        'Key Weaknesses': [random.choice(['High Costs', 'Slow R&D', 'Limited Reach', 'Lack of Differentiation']) for _ in range(50)],
        'Recommendations': [random.choice(['Increase Marketing Efforts', 'Enhance Product Features', 'Reduce Operational Costs', 'Expand Partnerships']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_5_prompt_1.csv', index=False)
    return 'Module_5_prompt_1.csv'


def generate_prompt_3_module_5():
    data = {
        'Goal': [random.choice(['Increase Revenue', 'Expand Market Share', 'Enhance Customer Experience', 'Improve Product Quality']) for _ in range(50)],
        'Strategic Vision': [random.choice(['Be a Market Leader', 'Offer Premium Products', 'Ensure Sustainability', 'Focus on Innovation']) for _ in range(50)],
        'Alignment Actions': [random.choice(['Invest in R&D', 'Expand Marketing', 'Improve Customer Support', 'Develop New Products']) for _ in range(50)],
        'Potential Risks': [random.choice(['Market Saturation', 'Rising Costs', 'Regulatory Hurdles', 'Competitor Actions']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_5_prompt_3.csv', index=False)
    return 'Module_5_prompt_3.csv'


def generate_prompt_4_module_5():
    data = {
        'Problem Description': [random.choice(['Declining Sales', 'Poor Customer Satisfaction', 'Operational Inefficiency', 'Product Defects']) for _ in range(50)],
        'Root Causes': [random.choice(['Lack of Innovation', 'Poor Marketing', 'Operational Bottlenecks', 'Inadequate Training']) for _ in range(50)],
        'Recommended Solutions': [random.choice(['Invest in R&D', 'Improve Customer Service', 'Streamline Operations', 'Employee Training Programs']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_5_prompt_4.csv', index=False)
    return 'Module_5_prompt_4.csv'


def generate_prompt_5_module_5():
    data = {
        'Objective': [random.choice(['Increase Revenue', 'Enhance Brand Awareness', 'Improve Customer Satisfaction', 'Boost Productivity']) for _ in range(50)],
        'Perspective': [random.choice(['Financial', 'Customer', 'Internal Process', 'Learning']) for _ in range(50)],
        'Dependencies': [random.choice(['Marketing Strategy', 'Product Development', 'Customer Service', 'Technology Improvements']) for _ in range(50)],
        'Milestones': [random.choice(['Quarterly Review', 'Product Launch', 'Customer Feedback Survey', 'Internal Training']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_5_prompt_5.csv', index=False)
    return 'Module_5_prompt_5.csv'


def generate_prompt_6_module_5():
    data = {
        'Strategic Option': [random.choice(['Expand into New Markets', 'Develop New Products', 'Partnership with Tech Firms', 'Optimize Operations']) for _ in range(50)],
        'Priority': [random.choice(['High', 'Medium', 'Low']) for _ in range(50)],
        'Justification': [random.choice(['High ROI', 'Low Feasibility', 'High Market Potential', 'Low Cost']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_5_prompt_6.csv', index=False)
    return 'Module_5_prompt_6.csv'


def generate_prompt_7_module_5():
    data = {
        'Scenario': [random.choice(['Optimistic', 'Realistic', 'Pessimistic']) for _ in range(50)],
        'Expected Outcome': [random.choice(['Revenue Growth', 'Stable Market Position', 'Decline in Market Share', 'Cost Reduction']) for _ in range(50)],
        'Associated Risks': [random.choice(['High Competition', 'Technological Failure', 'Regulatory Changes', 'Market Volatility']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_5_prompt_7.csv', index=False)
    return 'Module_5_prompt_7.csv'


def generate_prompt_8_module_5():
    data = {
        'Metric': [random.choice(['Revenue Growth', 'Customer Satisfaction', 'Market Share', 'Operational Efficiency']) for _ in range(50)],
        'Current Performance': [random.randint(50, 100) for _ in range(50)],
        'Industry Benchmark': [random.randint(60, 90) for _ in range(50)],
        'Improvement Recommendation': [random.choice(['Increase Marketing Spend', 'Enhance Product Features', 'Improve Customer Service', 'Cut Costs']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_5_prompt_8.csv', index=False)
    return 'Module_5_prompt_8.csv'


def generate_prompt_9_module_5():
    data = {
        'Opportunity': [random.choice(['New Market Entry', 'Product Diversification', 'Cost Optimization', 'Strategic Partnerships']) for _ in range(50)],
        'Description': [random.choice(['Expansion into Asia', 'Launching Eco-Friendly Products', 'Improving Operational Efficiency', 'Collaborating with Leading Brands']) for _ in range(50)],
        'Alignment with Current Capabilities': [random.choice(['High', 'Medium', 'Low']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_5_prompt_9.csv', index=False)
    return 'Module_5_prompt_9.csv'


def generate_prompt_10_module_5():
    data = {
        'Milestone': [random.choice(['Quarter 1 Review', 'Technology Pilot', 'Internal Training', 'Product Launch']) for _ in range(50)],
        'Description': [random.choice(['Assess Current Progress', 'Test New Systems', 'Prepare Teams', 'Evaluate Success Metrics']) for _ in range(50)],
        'Resources Required': [random.choice(['Team Members', 'Budget Allocation', 'Equipment', 'Training Sessions']) for _ in range(50)],
        'Risk Mitigation': [random.choice(['Regular Monitoring', 'Resource Redistribution', 'Backup Plans', 'Risk Analysis Sessions']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_5_prompt_10.csv', index=False)
    return 'Module_5_prompt_10.csv'


# Continue with similar code for Module 6: Requirements Analysis and Design Definition (RADD) if needed.
csv_files = [
generate_prompt_1_module_5(),
generate_prompt_2_module_5(),
generate_prompt_3_module_5(),
generate_prompt_4_module_5(),
generate_prompt_5_module_5(),
generate_prompt_6_module_5(),
generate_prompt_7_module_5(),
generate_prompt_8_module_5(),
generate_prompt_9_module_5(),
generate_prompt_10_module_5()
]
print("CSV files generated and saved successfully:", csv_files)

# import pandas as pd
import random

# Generate sample data for Module 6 prompts

def generate_prompt_1_module_6():
    data = {
        'Requirement ID': [f'FR-{i+1}' for i in range(50)],
        'Requirement Description': [random.choice([
            'User login functionality', 'Data encryption', 'Real-time data sync',
            'Role-based access control', 'Error handling mechanisms',
            'Data validation', 'Notification system', 'Payment gateway integration',
            'Audit logging', 'Multilingual support'
        ]) for _ in range(50)],
        'Priority Level': [random.choice(['High', 'Medium', 'Low']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_6_prompt_1.csv', index=False)
    return 'Module_6_prompt_1.csv'


def generate_prompt_2_module_6():
    data = {
        'NFR Category': [random.choice(['Performance', 'Usability', 'Security', 'Scalability']) for _ in range(50)],
        'Requirement': [random.choice([
            'System uptime of 99.9%', 'Response time under 1 second',
            'Data encryption using AES-256', 'Support for 10,000 concurrent users',
            'Data redundancy', 'Accessibility compliance', 'Multi-language support',
            'Single sign-on integration', 'Backup and recovery plans'
        ]) for _ in range(50)],
        'Description': [random.choice([
            'Ensure high availability for critical services',
            'Implement strict data protection protocols',
            'Optimize the UI for accessibility compliance',
            'Support for high traffic loads during peak hours',
            'Ensure easy-to-use navigation and responsive design',
            'Provide multi-factor authentication for all users'
        ]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_6_prompt_2.csv', index=False)
    return 'Module_6_prompt_2.csv'


def generate_prompt_3_module_6():
    data = {
        'Use Case ID': [f'UC-{i+1}' for i in range(50)],
        'Use Case Description': [random.choice([
            'User registration and login', 'Product search and filtering', 'Order placement',
            'Payment processing', 'Admin dashboard access', 'Password reset functionality',
            'Profile management', 'Content publishing', 'User role management', 'Report generation'
        ]) for _ in range(50)],
        'Actors': [random.choice([
            'Customer, Admin', 'User, System', 'Admin, System', 'Customer, Payment Gateway',
            'User, Database', 'Admin, Content Management System', 'Admin, Support Team'
        ]) for _ in range(50)],
        'Interactions': [random.choice([
            'User submits login credentials', 'Admin reviews orders', 'System processes payment',
            'User filters products by category', 'Admin manages user roles', 'Customer tracks order status'
        ]) for _ in range(50)],
        'System Boundaries': [random.choice([
            'Website frontend and backend', 'Mobile app and server', 'Payment API',
            'Admin panel and database', 'User interface and third-party integrations'
        ]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_6_prompt_3.csv', index=False)
    return 'Module_6_prompt_3.csv'


def generate_prompt_4_module_6():
    data = {
        'Process Step': [f'Step {i+1}' for i in range(50)],
        'Step Description': [random.choice([
            'Customer initiates order', 'Payment processed by system', 'Admin reviews order status',
            'System checks inventory availability', 'Order shipped to customer', 'Invoice generated',
            'Product delivered to customer', 'Customer provides feedback', 'Order cancelled',
            'Order refunded'
        ]) for _ in range(50)],
        'Decision Points': [random.choice([
            'Is product in stock?', 'Is payment successful?', 'Is customer verified?',
            'Has shipment left warehouse?', 'Is order eligible for return?', 'Has refund been processed?'
        ]) for _ in range(50)],
        'Outputs': [random.choice([
            'Order confirmation email sent', 'Invoice generated', 'Shipment tracking number issued',
            'Refund request submitted', 'Feedback request sent', 'Order status updated'
        ]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_6_prompt_4.csv', index=False)
    return 'Module_6_prompt_4.csv'


def generate_prompt_5_module_6():
    data = {
        'Entity Name': [random.choice([
            'Customer', 'Order', 'Product', 'Invoice', 'Payment', 'Category', 'Supplier'
        ]) for _ in range(50)],
        'Attributes': [random.choice([
            'Name, Age, Email', 'Order ID, Date, Total', 'Product ID, Name, Price',
            'Payment Method, Date, Amount', 'Supplier ID, Name, Contact', 'Category Name, Description'
        ]) for _ in range(50)],
        'Relationships': [random.choice([
            'Customer-Order (1:N)', 'Order-Product (M:N)', 'Invoice-Payment (1:1)',
            'Supplier-Product (1:M)', 'Category-Product (1:M)', 'Customer-Feedback (1:N)'
        ]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_6_prompt_5.csv', index=False)
    return 'Module_6_prompt_5.csv'


def generate_prompt_6_module_6():
    data = {
        'Current Capability': [random.choice([
            'User login via username/password', 'Basic search functionality', 'Basic order processing',
            'Email notification system', 'Basic reporting tools'
        ]) for _ in range(50)],
        'Proposed Capability': [random.choice([
            'OAuth 2.0 integration for login', 'Advanced search with filters', 'Real-time order processing',
            'SMS/Email push notifications', 'Advanced analytics and reporting'
        ]) for _ in range(50)],
        'Gap Description': [random.choice([
            'Current system lacks multi-factor authentication', 'Search functionality is limited',
            'Order processing is not optimized for scalability', 'No mobile notification system'
        ]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_6_prompt_6.csv', index=False)
    return 'Module_6_prompt_6.csv'


def generate_prompt_7_module_6():
    data = {
        'Wireframe Element': [f'Element {i+1}' for i in range(50)],
        'Element Description': [random.choice([
            'Navigation menu', 'Search bar', 'Product listing', 'Order summary', 'Footer', 
            'User profile section', 'Sidebar', 'Button for action', 'Modal window', 'Table for data display'
        ]) for _ in range(50)],
        'Wireframe Layout': [random.choice([
            'Header at the top, content below', 'Sidebar on the left, content on the right',
            'Full-screen navigation bar', 'Footer fixed at the bottom', 'Grid layout for products'
        ]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_6_prompt_7.csv', index=False)
    return 'Module_6_prompt_7.csv'


def generate_prompt_8_module_6():
    data = {
        'Requirement ID': [f'FR-{i+1}' for i in range(50)],
        'Priority Level': [random.choice(['High', 'Medium', 'Low']) for _ in range(50)],
        'Justification': [random.choice([
            'Critical for business operations', 'Depends on customer feedback', 'Enhances user experience',
            'Requires complex implementation', 'Direct impact on revenue generation'
        ]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_6_prompt_8.csv', index=False)
    return 'Module_6_prompt_8.csv'


def generate_prompt_9_module_6():
    data = {
        'Requirement': [f'Requirement {i+1}' for i in range(50)],
        'Alignment Status': [random.choice(['Aligned', 'Not Aligned']) for _ in range(50)],
        'Improvement Suggestion': [random.choice([
            'Increase collaboration with business teams', 'Refine requirement details',
            'Reevaluate business objectives', 'Clarify goals with stakeholders'
        ]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_6_prompt_9.csv', index=False)
    return 'Module_6_prompt_9.csv'


def generate_prompt_10_module_6():
    data = {
        'Requirement': [f'Requirement {i+1}' for i in range(50)],
        'Feasibility Status': [random.choice(['Feasible', 'Not Feasible']) for _ in range(50)],
        'Challenge': [random.choice([
            'Lack of technical resources', 'Integration issues', 'High development cost', 'Time constraints'
        ]) for _ in range(50)],
        'Mitigation Strategy': [random.choice([
            'Increase resource allocation', 'Partner with third-party vendors', 'Optimize development process',
            'Extend project timeline'
        ]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_6_prompt_10.csv', index=False)
    return 'Module_6_prompt_10.csv'


def generate_prompt_11_module_6():
    data = {
        'Requirement ID': [f'FR-{i+1}' for i in range(50)],
        'Test Scenario': [random.choice([
            'Test login functionality', 'Test order placement', 'Test product search', 'Test payment processing',
            'Test user profile update'
        ]) for _ in range(50)],
        'Test Objective': [random.choice([
            'Verify user credentials', 'Ensure payment gateway processes successfully', 'Ensure data is displayed correctly'
        ]) for _ in range(50)],
        'Expected Outcome': [random.choice([
            'User logged in successfully', 'Order placed and confirmed', 'Search results filtered correctly'
        ]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_6_prompt_11.csv', index=False)
    return 'Module_6_prompt_11.csv'


def generate_prompt_12_module_6():
    data = {
        'Original Requirement': [f'Requirement {i+1}' for i in range(50)],
        'Stakeholder': [random.choice(['Business', 'Development', 'Quality Assurance', 'Operations']) for _ in range(50)],
        'Consolidated Requirement': [random.choice([
            'User authentication functionality', 'Data analytics dashboard', 'Role-based user access',
            'Multilingual UI support', 'Automated testing framework'
        ]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_6_prompt_12.csv', index=False)
    return 'Module_6_prompt_12.csv'


# Generate all CSVs for Module 6
csv_files_module_6 = [
    generate_prompt_1_module_6(),
    generate_prompt_2_module_6(),
    generate_prompt_3_module_6(),
    generate_prompt_4_module_6(),
    generate_prompt_5_module_6(),
    generate_prompt_6_module_6(),
    generate_prompt_7_module_6(),
    generate_prompt_8_module_6(),
    generate_prompt_9_module_6(),
    generate_prompt_10_module_6(),
    generate_prompt_11_module_6(),
    generate_prompt_12_module_6()
]

print("Module 6 CSV files generated and saved successfully:", csv_files_module_6)




import pandas as pd
import random
import os

# Ensure the directory exists
os.makedirs('generated_datas', exist_ok=True)

def generate_prompt_1():
    data = {
        'Metric': [random.choice(['User Adoption Rate', 'Efficiency Gains', 'ROI']) for _ in range(50)],
        'Current Performance': [random.choice(['80%', '90%', '70%', '85%']) for _ in range(50)],
        'Evaluation Summary': [random.choice(['Good', 'Excellent', 'Satisfactory', 'Needs Improvement']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_7_prompt_1.csv', index=False)

def generate_prompt_2():
    data = {
        'Costs': [random.choice(['$10,000', '$50,000', '$100,000', '$20,000']) for _ in range(50)],
        'Tangible Benefits': [random.choice(['Increased sales by 20%', 'Improved user efficiency by 30%', 'Cost reduction of 10%', 'Reduced time to market by 25%']) for _ in range(50)],
        'Intangible Benefits': [random.choice(['Improved brand perception', 'Increased employee morale', 'Better decision-making', 'Enhanced collaboration']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_7_prompt_2.csv', index=False)

def generate_prompt_3():
    data = {
        'Satisfaction Overview': [random.choice(['High', 'Medium', 'Low', 'Very High']) for _ in range(50)],
        'Positive Feedback': [random.choice(['User-friendly interface', 'Faster response time', 'Better reporting', 'Easy integration', 'Improved workflow', 'Time-saving features']) for _ in range(50)],
        'Areas for Improvement': [random.choice(['Lack of mobile app', 'Improvement in analytics', 'More integrations', 'Need for better support', 'Improved UI/UX', 'Expand training resources']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_7_prompt_3.csv', index=False)

def generate_prompt_4():
    data = {
        'Risk Description': [random.choice(['Data Loss', 'System Downtime', 'Security Breach', 'Incompatibility issues', 'Scalability challenges', 'Lack of integration']) for _ in range(50)],
        'Likelihood': [random.choice(['Low', 'Medium', 'High', 'Very High']) for _ in range(50)],
        'Impact': [random.choice(['Low', 'Medium', 'High', 'Critical']) for _ in range(50)],
        'Mitigation Strategy': [random.choice(['Enhanced training', 'Better testing procedures', 'Improved infrastructure', 'More rigorous planning', 'Upgrade security protocols']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_7_prompt_4.csv', index=False)

def generate_prompt_5():
    data = {
        'Solution Option': [random.choice(['Option A', 'Option B', 'Option C']) for _ in range(50)],
        'Criteria': [random.choice(['Cost', 'Scalability', 'Ease of Implementation']) for _ in range(50)],
        'Evaluation Score': [random.choice([1, 2, 3, 4, 5]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_7_prompt_5.csv', index=False)

def generate_prompt_6():
    data = {
        'Current Functionality': [random.choice(['Manual data entry', 'Batch processing', 'Basic reporting']) for _ in range(50)],
        'Gap Description': [random.choice(['No real-time updates', 'Slow processing time', 'Limited reporting features']) for _ in range(50)],
        'Recommended Improvement': [random.choice(['Automated reporting', 'Faster data processing', 'Advanced analytics capabilities']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_7_prompt_6.csv', index=False)

def generate_prompt_7():
    data = {
        'Overview': [random.choice(['Pilot test passed with minor issues', 'Pilot test failed, requires rework', 'Pilot test exceeded expectations']) for _ in range(50)],
        'Key Findings': [random.choice(['Improved user engagement', 'System crashes under load', 'Users found interface confusing', 'Positive feedback from users', 'Performance issues identified', 'Lack of clarity on features']) for _ in range(50)],
        'Recommendations': [random.choice(['Optimize system performance', 'Enhance user interface', 'Provide additional training', 'Integrate additional features', 'Improve data security']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_7_prompt_7.csv', index=False)

def generate_prompt_8():
    data = {
        'Scalability Criteria': [random.choice(['Expected User Growth', 'Data Volume', 'Infrastructure Requirements']) for _ in range(50)],
        'Evaluation': [random.choice(['High scalability', 'Medium scalability', 'Low scalability']) for _ in range(50)],
        'Recommendations': [random.choice(['Optimize infrastructure', 'Cloud-based solution recommended', 'Enhance database architecture', 'Increase server capacity', 'Upgrade to scalable cloud services']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_7_prompt_8.csv', index=False)

def generate_prompt_9():
    data = {
        'Metric': [random.choice(['Processing Speed', 'Data Throughput', 'Error Rate']) for _ in range(50)],
        'Solution Performance': [random.choice(['High', 'Medium', 'Low']) for _ in range(50)],
        'Industry Benchmark': [random.choice(['High', 'Medium', 'Low']) for _ in range(50)],
        'Recommendation': [random.choice(['Optimize performance', 'Monitor errors closely', 'Increase data throughput', 'Improve speed', 'Reduce latency']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_7_prompt_9.csv', index=False)

def generate_prompt_10():
    data = {
        'Overview': [random.choice(['Solution meets business objectives', 'Solution requires additional tuning', 'Solution is underperforming']) for _ in range(50)],
        'Strengths': [random.choice(['User-friendly', 'Fast implementation', 'Cost-effective', 'Scalable', 'Well-integrated', 'Easy to maintain']) for _ in range(50)],
        'Weaknesses': [random.choice(['Limited functionality', 'Lacks integration', 'Poor user experience', 'Slower than expected', 'High maintenance cost']) for _ in range(50)],
        'Recommendations': [random.choice(['Improve scalability', 'Add more features', 'Enhance user experience', 'Optimize performance', 'Simplify setup']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_7_prompt_10.csv', index=False)

def generate_prompt_11():
    data = {
        'Cost': [random.choice(['$100,000', '$50,000', '$200,000']) for _ in range(50)],
        'Benefits': [random.choice(['Increased revenue', 'Operational efficiency', 'Customer retention']) for _ in range(50)],
        'Calculation Steps': [random.choice(['Subtract costs from benefits', 'Use ROI formula']) for _ in range(50)],
        'ROI Value': [random.choice(['30%', '40%', '50%', '60%']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_7_prompt_11.csv', index=False)

# Generate all prompts and save CSVs
generate_prompt_1()
generate_prompt_2()
generate_prompt_3()
generate_prompt_4()
generate_prompt_5()
generate_prompt_6()
generate_prompt_7()
generate_prompt_8()
generate_prompt_9()
generate_prompt_10()
generate_prompt_11()

print("All CSV files have been generated in the 'generated_datas' directory.")




import pandas as pd
import random

# Function for Prompt 1: Setting Up Real-Time Monitoring Dashboards with AI
def generate_prompt_1_module_8():
    data = {
        'Metric': [random.choice(['Task Completion Rate', 'Resource Utilization', 'Risk Levels', 'Budget Spent', 'Milestones Achieved']) for _ in range(50)],
        'Description': [random.choice([
            'Percentage of tasks completed in time', 
            'Percentage of resources utilized compared to the plan',
            'Current risk status of the project',
            'Total budget spent vs planned',
            'List of completed milestones and pending'
        ]) for _ in range(50)],
        'Visualization Method': [random.choice(['Bar chart', 'Line chart', 'Pie chart', 'Gauge chart', 'Heatmap']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_8_prompt_1.csv', index=False)
    return 'Module_8_prompt_1.csv'


# Function for Prompt 2: AI-Assisted Metrics Identification
def generate_prompt_2_module_8():
    data = {
        'Metric': [random.choice(['Time to Market', 'Customer Satisfaction', 'Team Collaboration', 'Cost Efficiency', 'Quality Control']) for _ in range(50)],
        'Description': [random.choice([
            'Duration from project inception to launch', 
            'Customer feedback and survey results', 
            'Frequency of cross-functional team meetings',
            'Comparison of actual vs planned cost for project completion',
            'Level of product defects and bug reports'
        ]) for _ in range(50)],
        'Alignment': [random.choice(['High', 'Medium', 'Low']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_8_prompt_2.csv', index=False)
    return 'Module_8_prompt_2.csv'


# Function for Prompt 3: Tracking Team Productivity with AI
def generate_prompt_3_module_8():
    data = {
        'Metrics': [random.choice(['Task Completion Rate', 'Average Time Per Task', 'Delay Rate', 'Resource Allocation Efficiency', 'Team Collaboration Index']) for _ in range(50)],
        'Current Performance': [random.choice(['Good', 'Average', 'Poor']) for _ in range(50)],
        'Recommendations': [random.choice([
            'Increase task delegation', 
            'Provide additional training for team members',
            'Optimize resource allocation',
            'Improve communication between team members',
            'Use task automation tools'
        ]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_8_prompt_3.csv', index=False)
    return 'Module_8_prompt_3.csv'


# Function for Prompt 4: Risk Monitoring and Alerts System
def generate_prompt_4_module_8():
    data = {
        'Risk': [random.choice(['Budget Overrun', 'Resource Shortage', 'Scope Creep', 'Quality Issues', 'Delayed Deliverables']) for _ in range(50)],
        'Trigger': [random.choice(['Exceeded 80% budget', 'Critical resource unavailable', 'Scope change request', 'High number of defects', 'Delay in milestones']) for _ in range(50)],
        'Alert Type': [random.choice(['Email', 'Dashboard Notification', 'SMS', 'Push Notification', 'Phone Call']) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_8_prompt_4.csv', index=False)
    return 'Module_8_prompt_4.csv'


# Function for Prompt 5: Automated Progress Reporting with AI
def generate_prompt_5_module_8():
    data = {
        'Overview': [random.choice(['Project in progress', 'Milestone reached', 'Delayed due to resource issues']) for _ in range(50)],
        'Current Status': [random.choice(['On Track', 'Delayed', 'At Risk', 'Completed']) for _ in range(50)],
        'Issues': [random.choice([
            'Resource bottleneck', 
            'Quality concerns', 
            'Unexpected scope changes',
            'Schedule delays',
            'Budget overrun'
        ]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_8_prompt_5.csv', index=False)
    return 'Module_8_prompt_5.csv'


# Function for Prompt 6: AI-Assisted Variance Analysis
def generate_prompt_6_module_8():
    data = {
        'Metric': [random.choice(['Task Completion Rate', 'Budget Utilization', 'Milestone Achievement', 'Resource Allocation', 'Quality Control']) for _ in range(50)],
        'Planned Value': [random.choice([80, 90, 95, 100, 85]) for _ in range(50)],
        'Actual Value': [random.choice([70, 85, 92, 100, 80]) for _ in range(50)],
        'Variance': [lambda x, y: x - y for x, y in zip([80, 90, 95, 100, 85] * 10, [70, 85, 92, 100, 80] * 10)],
        'Corrective Action': [random.choice([
            'Reallocate resources', 
            'Adjust project scope', 
            'Increase team collaboration', 
            'Revise project timeline',
            'Implement automation tools'
        ]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_8_prompt_6.csv', index=False)
    return 'Module_8_prompt_6.csv'


# Function for Prompt 7: Monitoring Budget Utilization with AI Insights
def generate_prompt_7_module_8():
    data = {
        'Budget Overview': [random.choice(['Budget allocation', 'Overspent', 'Underspent']) for _ in range(50)],
        'Utilization Analysis': [random.choice(['80% utilized', '95% utilized', '100% utilized', 'Over budget', 'Under budget']) for _ in range(50)],
        'Recommendations': [random.choice([
            'Reallocate funds to priority areas', 
            'Investigate areas of overspending', 
            'Trim unnecessary expenses',
            'Adjust the project scope for budget fit',
            'Forecast future expenses'
        ]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_8_prompt_7.csv', index=False)
    return 'Module_8_prompt_7.csv'


# Function for Prompt 8: Identifying Bottlenecks in Project Progress
def generate_prompt_8_module_8():
    data = {
        'Task': [random.choice(['Task A', 'Task B', 'Task C', 'Task D', 'Task E']) for _ in range(50)],
        'Bottleneck Description': [random.choice([
            'Delayed resource allocation', 
            'Slow decision-making process', 
            'External dependency delay', 
            'Insufficient budget allocation',
            'Poor communication between teams'
        ]) for _ in range(50)],
        'AI Recommendation': [random.choice([
            'Reallocate resources', 
            'Streamline decision-making process',
            'Negotiate with external vendors',
            'Increase team communication',
            'Increase budget allocation for the task'
        ]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_8_prompt_8.csv', index=False)
    return 'Module_8_prompt_8.csv'


# Function for Prompt 9: KPI Analysis with AI
def generate_prompt_9_module_8():
    data = {
        'KPI': [random.choice(['Completion Rate', 'Budget Variance', 'Milestone Progress', 'Resource Utilization', 'Defect Rate']) for _ in range(50)],
        'Performance Level': [random.choice(['Good', 'Average', 'Poor']) for _ in range(50)],
        'Insight': [random.choice([
            'On track, no concerns', 
            'Needs attention, minor issues', 
            'Critical, requires intervention',
            'Slightly behind schedule, needs improvement'
        ]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_8_prompt_9.csv', index=False)
    return 'Module_8_prompt_9.csv'


# Run all functions to generate the required CSV files
generate_prompt_1_module_8()
generate_prompt_2_module_8()
generate_prompt_3_module_8()
generate_prompt_4_module_8()
generate_prompt_5_module_8()
generate_prompt_6_module_8()
generate_prompt_7_module_8()
generate_prompt_8_module_8()
generate_prompt_9_module_8()

print("All CSV files have been generated in the 'generated_datas' directory.")


import pandas as pd
import random

# Function for Prompt 1: Identifying Key Competencies for Business Analysts Using AI
def generate_prompt_1_module_9():
    data = {
        'Competency': [random.choice(['Communication Skills', 'Analytical Thinking', 'Problem Solving', 'Technical Knowledge', 'Stakeholder Management']) for _ in range(50)],
        'Description': [random.choice([
            'Ability to communicate complex ideas effectively',
            'Capacity to analyze data and draw meaningful insights',
            'Ability to approach and solve complex problems',
            'Technical expertise in tools and systems used by the business',
            'Managing relationships and expectations with stakeholders'
        ]) for _ in range(50)],
        'AI Enhancement': [random.choice([
            'AI-powered data analysis tools for enhanced decision-making',
            'Natural language processing tools for better communication',
            'AI-driven simulations for problem-solving scenarios',
            'AI-powered technical support and automated systems',
            'AI tools for analyzing stakeholder feedback'
        ]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_9_prompt_1.csv', index=False)
    return 'Module_9_prompt_1.csv'


# Function for Prompt 3: Gap Analysis of Competencies Using AI
def generate_prompt_3_module_9():
    data = {
        'Competency': [random.choice(['Communication Skills', 'Business Process Analysis', 'Data Management', 'Project Management', 'Strategic Thinking']) for _ in range(50)],
        'Gap Identified': [random.choice([
            'Lack of formal training',
            'Limited exposure to real-world scenarios',
            'Difficulty in handling data complexities',
            'Limited project experience',
            'Lack of strategic decision-making ability'
        ]) for _ in range(50)],
        'Suggested Resource': [random.choice([
            'Online courses and webinars',
            'Hands-on project opportunities',
            'AI-based data management platforms',
            'Project management certification programs',
            'AI-driven decision-making frameworks'
        ]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_9_prompt_3.csv', index=False)
    return 'Module_9_prompt_3.csv'


# Function for Prompt 6: Leveraging AI for Conflict Resolution
def generate_prompt_6_module_9():
    data = {
        'Conflict Overview': [random.choice(['Stakeholders disagree on project priorities', 'Team members have different views on resource allocation', 'Unclear project scope leading to conflicting expectations']) for _ in range(50)],
        'AI Analysis': [random.choice([
            'AI-powered sentiment analysis to understand underlying concerns',
            'AI tools for prioritizing stakeholder interests',
            'AI-driven analysis of previous conflict resolution strategies'
        ]) for _ in range(50)],
        'Resolution Strategies': [random.choice([
            'AI-generated negotiation techniques based on data trends',
            'AI-powered decision-making frameworks for prioritization',
            'Utilizing AI to model different conflict resolution scenarios'
        ]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_9_prompt_6.csv', index=False)
    return 'Module_9_prompt_6.csv'


# Function for Prompt 7: AI-Driven Mind Mapping for Business Analysts
def generate_prompt_7_module_9():
    data = {
        'Requirement Category': [random.choice(['Functional', 'Non-functional', 'Technical']) for _ in range(50)],
        'Description': [random.choice([
            'Functional requirements related to business processes',
            'Non-functional requirements such as performance and security',
            'Technical requirements involving system architecture'
        ]) for _ in range(50)],
        'AI Application': [random.choice([
            'AI-based clustering of requirements for better categorization',
            'Natural language processing to extract requirements from documents',
            'AI-powered tools for mapping interdependencies between requirements'
        ]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_9_prompt_7.csv', index=False)
    return 'Module_9_prompt_7.csv'


# Function for Prompt 8: Competency Development Roadmap Using AI
def generate_prompt_8_module_9():
    data = {
        'Milestone': [random.choice(['Initial Assessment', 'Competency Building', 'Skill Evaluation', 'Advanced Development', 'Final Assessment']) for _ in range(50)],
        'Description': [random.choice([
            'Evaluate current competencies and identify gaps',
            'Provide AI-based learning resources for skill enhancement',
            'Evaluate progress through AI-assisted assessments',
            'Offer advanced AI training for further competency growth',
            'Final evaluation to assess competency improvements'
        ]) for _ in range(50)],
        'AI Resource': [random.choice([
            'AI-driven competency assessment tools',
            'AI-powered learning management systems',
            'Machine learning models for tracking progress',
            'AI-driven personalized learning paths',
            'AI evaluation platforms for skill testing'
        ]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_9_prompt_8.csv', index=False)
    return 'Module_9_prompt_8.csv'


# Function for Prompt 9: Measuring the Effectiveness of BA Techniques Using AI
def generate_prompt_9_module_9():
    data = {
        'Techniques Evaluated': [random.choice(['Requirements Gathering', 'Process Modeling', 'Stakeholder Interviews', 'Data Analysis', 'Change Management']) for _ in range(50)],
        'Metrics': [random.choice([
            'Stakeholder satisfaction scores',
            'Time taken to complete tasks',
            'Reduction in errors after process improvement',
            'Time saved due to AI-based automation',
            'Cost savings achieved through better resource allocation'
        ]) for _ in range(50)],
        'Findings': [random.choice([
            'Techniques were effective in improving project timelines',
            'Stakeholder satisfaction improved with clear communication',
            'Process modeling resulted in significant cost savings',
            'Data analysis techniques led to better decision-making',
            'Change management strategies reduced resistance to new processes'
        ]) for _ in range(50)]
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_9_prompt_9.csv', index=False)
    return 'Module_9_prompt_9.csv'


# Run all functions to generate the required CSV files
generate_prompt_1_module_9()
generate_prompt_3_module_9()
generate_prompt_6_module_9()
generate_prompt_7_module_9()
generate_prompt_8_module_9()
generate_prompt_9_module_9()

print("All CSV files have been generated in the 'generated_datas' directory.")

import pandas as pd
import random
import os

# Ensure the directory exists
os.makedirs('generated_datas', exist_ok=True)

# Prompt 2: AI-Driven Industry Disruption Scenarios
def generate_prompt_2():
    data = {
        'Industry': [random.choice(['Healthcare', 'Finance', 'Retail', 'Manufacturing', 'Transportation']) for _ in range(50)],
        'Disruption Scenario': [random.choice(['AI for automation of manual tasks', 'AI-driven predictive maintenance', 'AI-powered customer personalization', 'AI-enhanced supply chain optimization', 'AI-based fraud detection']) for _ in range(50)],
        'Impact on Business Analysts': [random.choice(['Increased demand for data analysis skills', 'Need for AI integration expertise', 'Focus on data-driven decision making', 'Proficiency in AI tools and platforms', 'Greater focus on stakeholder collaboration']) for _ in range(50)],
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_10_prompt_2.csv', index=False)

# Prompt 5: Assessing AI Maturity Levels in Organizations
def generate_prompt_5():
    data = {
        'Assessment Criteria': [random.choice(['Data Readiness', 'AI Adoption', 'Team Skills', 'Infrastructure Strength', 'Process Integration']) for _ in range(50)],
        'Current Status': [random.choice(['In progress', 'Fully implemented', 'Limited implementation', 'Not started', 'On hold']) for _ in range(50)],
        'Recommendations': [random.choice(['Invest in data collection infrastructure', 'Conduct AI training workshops', 'Adopt cloud-based AI solutions', 'Build internal AI talent', 'Enhance collaboration with external AI partners']) for _ in range(50)],
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_10_prompt_5.csv', index=False)

# Prompt 6: AI-Enhanced Business Models for the Future
def generate_prompt_6():
    data = {
        'AI-Enabled Business Model': [random.choice(['AI-driven subscription services', 'AI for predictive analytics in marketing', 'AI-powered autonomous vehicles', 'AI-based customer service automation', 'AI-enhanced product recommendation systems']) for _ in range(50)],
        'Description': [random.choice(['Leveraging AI to offer subscription-based services that adapt to customer preferences', 'Using AI to predict consumer behavior and optimize marketing strategies', 'Developing self-driving vehicles using AI technology', 'Automating customer service with AI chatbots and voice assistants', 'Enhancing e-commerce experiences through AI-driven personalized recommendations']) for _ in range(50)],
        'Required Capabilities': [random.choice(['AI algorithms and machine learning models', 'Robust data analytics capabilities', 'Advanced computer vision and sensor technology', 'Natural language processing for chatbots', 'Deep learning and recommendation algorithms']) for _ in range(50)],
        'Potential Risks': [random.choice(['Data privacy concerns', 'High implementation costs', 'Regulatory challenges', 'Dependency on third-party AI platforms', 'Integration challenges with legacy systems']) for _ in range(50)],
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_10_prompt_6.csv', index=False)

# Prompt 7: Identifying Opportunities in AI-Driven Decision Making
def generate_prompt_7():
    data = {
        'Decision Process': [random.choice(['Sales forecasting', 'Supply chain management', 'Customer service automation', 'Risk management', 'Product development']) for _ in range(50)],
        'AI Enhancement': [random.choice(['AI-based demand prediction', 'Machine learning for route optimization', 'AI-powered customer sentiment analysis', 'AI-driven risk assessment', 'AI-based market trend analysis']) for _ in range(50)],
        'Expected Benefit': [random.choice(['Improved decision accuracy', 'Reduced operational costs', 'Faster decision-making', 'Better customer satisfaction', 'Higher product innovation']) for _ in range(50)],
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_10_prompt_7.csv', index=False)

# Prompt 8: Preparing for AI Regulatory Changes
def generate_prompt_8():
    data = {
        'Regulation Overview': [random.choice(['GDPR Compliance', 'AI ethics guidelines', 'AI transparency requirements', 'Data privacy laws', 'Bias mitigation regulations']) for _ in range(50)],
        'Impact on BA Practices': [random.choice(['Need for data privacy awareness', 'Increased focus on AI transparency', 'Stricter data usage policies', 'Enhanced ethical responsibility', 'Changes in stakeholder communication regarding AI use']) for _ in range(50)],
        'Adaptation Strategies': [random.choice(['Implement data encryption measures', 'Conduct regular AI audits', 'Create transparency reports', 'Establish ethical AI guidelines', 'Ensure data anonymization practices']) for _ in range(50)],
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_10_prompt_8.csv', index=False)

# Prompt 9: Building a Future-Ready AI Strategy
def generate_prompt_9():
    data = {
        'Step': [random.choice(['Technology Evaluation', 'Skill Development', 'Process Transformation', 'AI Pilot Projects', 'AI Integration Strategy']) for _ in range(50)],
        'Description': [random.choice(['Assessing the latest AI tools and technologies for integration', 'Training teams on AI tools and methodologies', 'Revamping business processes to accommodate AI', 'Running small-scale AI projects for testing', 'Formulating a roadmap for AI adoption across departments']) for _ in range(50)],
    }
    df = pd.DataFrame(data)
    df.to_csv('generated_datas/Module_10_prompt_9.csv', index=False)

# Call the function for each prompt
generate_prompt_2()
generate_prompt_5()
generate_prompt_6()
generate_prompt_7()
generate_prompt_8()
generate_prompt_9()



print("All CSV files have been generated in the 'generated_datas' directory.")

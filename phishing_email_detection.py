import openai
import re
from urllib.parse import urlparse
import requests

# Set your OpenAI API key here
openai.api_key = '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'

# Helper function to check for suspicious sender domain
def check_sender(sender):
    suspicious_domains = ["@gmail.com", "@yahoo.com", "@outlook.com", "@hotmail.com", "@icloud.com", 
    "@aol.com", "@mail.com", "@yandex.com", "@mail.ru", "@fakebank.com", 
    "@support.com", "@noreply.com", "@webmail.com", "@customer-service.com", 
    "@mybankinfo.com", "@security-notification.com"]  # You can add more domains
    if any(domain in sender.lower() for domain in suspicious_domains):
        return True
    return False

# Helper function to detect phishing keywords in email body
def check_phishing_keywords(body):
    phishing_keywords = [
        "urgent", "immediate action required", "your account is suspended", "last warning", 
    "important notice", "final notice", "limited time offer", "hurry", "now", "claim your prize",
    "don’t miss out", "verify your account", "reset your password", "click here", "submit your details",
    "provide your information", "update your account", "verify your identity", "enter your bank details", 
    "confirm your email", "sign in to your account", "access your account", "bank account details", 
    "credit card details", "social security number", "tax refund", "dear user", "dear customer", 
    "you’ve been selected", "you’ve won", "unusual activity detected", "suspicious login", "account compromised", 
    "security alert", "click to resolve", "open your file", "download the attachment", "if you do not act immediately", 
    "your account is about to expire", "your subscription will be canceled", "security breach", "help us protect your account", 
    "activate your account", "payment is due", "final warning", "please send us your information"
    ]
    # Check if any phishing keywords are in the email body (case insensitive)
    return any(keyword in body.lower() for keyword in phishing_keywords)

# Helper function to validate URLs
def check_url_safety(url):
    # Check if the URL uses HTTPS and is a valid domain
    parsed_url = urlparse(url)
    if parsed_url.scheme != 'https':
        return False  # Insecure URL
    return True

# Function to analyze content using OpenAI API (Improved for newer models)
def analyze_content_with_openai(subject, sender, body, links):
    # Update the prompt for the new models
    messages = [
        {"role": "system", "content": "You are an AI system that detects phishing emails."},
        {"role": "user", "content": f"""
        Given the following email:

        Subject: {subject}
        Sender: {sender}
        Body: {body}
        Links: {', '.join(links)}

        Is this email a phishing attempt? Respond with 'Yes' or 'No' and explain why or why not.
        """}
    ]

    try:
        # Use gpt-3.5-turbo (or gpt-4 if available) for better results
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=messages,
            max_tokens=200,
            temperature=0.5
        )

        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error analyzing email: {str(e)}"

# Main function to analyze an email for phishing
def analyze_email(subject, sender, body, links):
    # 1. Check if the sender's email domain is suspicious
    if check_sender(sender):
        return "Suspicious sender domain detected."

    # 2. Check for common phishing keywords in the email body
    if check_phishing_keywords(body):
        return "Phishing keywords detected in email body."

    # 3. Check each link in the email for HTTPS safety
    for link in links:
        if not check_url_safety(link):
            return f"Suspicious link detected (not using HTTPS): {link}"

    # 4. Analyze the email content with OpenAI for deeper context
    result = analyze_content_with_openai(subject, sender, body, links)
    return result

# Sample email for testing
sample_subject = "URGENT: Account Update Required"
sample_sender = "johndoe@email.com"
sample_body = """
Dear Jane Doe,

Thank you for applying for the Software Developer position at XYZ Corp. We are reviewing your application and will contact you if we would like to schedule an interview.

If you have any questions, please contact us at hr@xyz-corp.com.

Best regards,  
XYZ Corp. HR Team

"""
sample_links = ["https://www.google.com/"]

# Analyze the sample email
result = analyze_email(sample_subject, sample_sender, sample_body, sample_links)
print(result)

import os
import base64
import pandas as pd
from datetime import datetime
import google.generativeai as genai
import smtplib
from email.message import EmailMessage
import streamlit as st
from prompts import get_prompt  # Import team-specific prompt function

# Configure the Generative AI API using Streamlit secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Generation configuration remains constant
generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

def summarize_report(team: str, member: str, month: str) -> str:
    # Build the CSV path for the selected member in the team
    csv_path = os.path.join("data", team, f"{member}.csv")
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path)
    
    # Parse the 'date' column to datetime using the specified format
    df['datetime'] = pd.to_datetime(df['date'], format="%d %b %Y, %H:%M")
    
    # If month is not "overall", filter by the specified month
    if month.lower() != "overall":
        month_number = datetime.strptime(month, "%B").month
        df = df[df['datetime'].dt.month == month_number]

    # Combine 'content' and 'date' to build the report content text
    df["data"] = df["from"] + " " + df["content"] + " " + df["date"]
    text_data = "\n".join(df['data'].tolist())
    
    # Get the team-specific prompt from prompts.py
    team_prompt = get_prompt(team)
    
    # Create the Generative AI model using the team prompt
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash-8b",
        generation_config=generation_config,
        system_instruction=team_prompt
    )
    
    # Start a chat session with the model and send the text data
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(text_data)
    
    # Extract and return the summary from the response
    summary = response.text
    print("Generated Summary:", summary)
    return summary

def send_email_report(recipient_email: str, pdf_data: bytes, member: str, team: str, period: str) -> bool:
    """
    Sends an email with the provided PDF attachment.
    Returns True if the email was sent successfully; otherwise, False.
    """
    # Email configuration from Streamlit secrets
    sender_email = st.secrets["SENDER_EMAIL"]
    sender_password = st.secrets["SENDER_PASSWORD"]
    subject = f"Daily Report Summary for {member} ({team}) - {period}"
    body = "Please find attached your daily report summary."
    
    try:
        print("[DEBUG] Preparing email message...")
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg.set_content(body)
        msg.add_attachment(pdf_data,
                           maintype="application",
                           subtype="pdf",
                           filename=f"{member}_report_{period}.pdf")
        
        print("[DEBUG] Connecting to SMTP server...")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        print("[DEBUG] Email sent successfully!")
        return True
    except Exception as e:
        print(f"[DEBUG] Error sending email: {e}")
        return False

# Streamlit UI
def main():
    st.title("Daily Report Generator")
    
    # Input fields
    team = st.selectbox("Select Team", ["TeamA", "TeamB", "TeamC"])  # Replace with your teams
    member = st.text_input("Enter Member Name")
    month = st.selectbox("Select Month", ["Overall", "January", "February", "March", "April", "May", "June", 
                                          "July", "August", "September", "October", "November", "December"])
    recipient_email = st.text_input("Recipient Email")
    
    if st.button("Generate and Send Report"):
        if member and recipient_email:
            # Generate summary
            summary = summarize_report(team, member, month)
            st.write("### Generated Summary")
            st.write(summary)
            
            # For demo, we'll simulate PDF data (since PDF generation isn't in your code yet)
            pdf_data = b"Sample PDF content"  # Replace with actual PDF generation logic if needed
            
            # Send email
            success = send_email_report(recipient_email, pdf_data, member, team, month)
            if success:
                st.success("Report emailed successfully!")
            else:
                st.error("Failed to send email. Check logs for details.")
        else:
            st.warning("Please fill in all fields.")

if __name__ == "__main__":
    main()



















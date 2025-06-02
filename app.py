
# app.py

import os
import base64
import pandas as pd
from datetime import datetime
import google.generativeai as genai
import smtplib
from email.message import EmailMessage
from prompts import get_prompt  # Import our new team-specific prompt function

# Configure the Generative AI API (replace with your actual key)
genai.configure(api_key="AIzaSyCYsvqn20T0hqpzXXfvacOhm16au1oynaE")

# Generation configuration remains constant.
generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8000,
    "response_mime_type": "text/plain",
}

def summarize_report(team: str, member: str, month: str) -> str:
    try:
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
            model_name="gemini-2.0-flash-thinking-exp-01-21",
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
    except Exception as e:
        print(f"Error in monthly report generation: {str(e)}")
        return "The EDR's was not in structured form to generate proper summary."

def send_email_report(recipient_email: str, pdf_data: bytes, member: str, team: str, period: str) -> bool:
    """
    Sends an email with the provided PDF attachment.
    Returns True if the email was sent successfully; otherwise, False.
    """
    # Email configuration (ensure you replace these with secure and proper credentials)
    sender_email = "nx.ai@nxfin.in"  # Replace with your sender email
    sender_password = "rfhw ennv swoo lono"  # Replace with your email password or secure storage method
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
        # Connect to the SMTP server (using Gmail's SMTP server in this example)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        print("[DEBUG] Email sent successfully!")
        return True
    except Exception as e:
        print(f"[DEBUG] Error sending email: {e}")
        return False


























# from flask import Flask, request, jsonify
# import pandas as pd
# import os
# from datetime import datetime
# import google.generativeai as genai
# from flask import Flask, request, jsonify
# import smtplib
# from email.message import EmailMessage
# import base64



# # Initialize Flask app
# app = Flask(__name__)

# # Route to summarize work reports
# @app.route('/summarize', methods=['POST'])
# def summarize():
#     # Parse input data
#     data = request.json
#     team = data.get('team')
#     member = data.get('member')
#     month = data.get('month')

#     # Build the CSV path for the selected member in the team
#     csv_path = os.path.join("data", team, f"{member}.csv")
    
#     # Read CSV file into a DataFrame
#     df = pd.read_csv(csv_path)
    
#     # Parse the 'date' column to datetime using the given format
#     df['datetime'] = pd.to_datetime(df['date'], format="%d %b %Y, %H:%M")
    
#     # Filter by month if not "overall"
#     if month.lower() != "overall":
#         month_number = datetime.strptime(month, "%B").month
#         df = df[df['datetime'].dt.month == month_number]

#     df["data"] = df["content"] + df["date"]
    
#     # Combine the report contents into one text string
#     text_data = "\n".join(df['data'].tolist())

#     # Configure the Generative AI API
#     genai.configure(api_key="AIzaSyC9MGO2NzRz3gLJ0V1HhIcKhGe3HLN_RQM")

#     # Define generation configuration
#     generation_config = {
#         "temperature": 0,
#         "top_p": 0.95,
#         "top_k": 40,
#         "max_output_tokens": 8192,
#         "response_mime_type": "text/plain",
#     }

#     # Create the Generative AI model
#     model = genai.GenerativeModel(
#         model_name="gemini-1.5-flash-8b",
#         generation_config=generation_config,
#         system_instruction=(
#                 "summarize"
#         )

#     )


#     # Start a chat session with the model
#     chat_session = model.start_chat(history=[])

#     # Send the text data to the model and get the response
#     response = chat_session.send_message(text_data)

#     # Extract the summary from the response
#     summary = response.text

#     print(summary)
#     # Return the summary as a JSON response
#     return jsonify({"summary": summary})




# @app.route('/send_email_report', methods=['POST'])
# def send_email_report_endpoint():
#     data = request.get_json()
#     recipient_email = data.get("recipient_email")
#     pdf_base64 = data.get("pdf_data")
#     member = data.get("member")
#     team = data.get("team")
#     period = data.get("period")
    
#     # Validate required fields.
#     if not all([recipient_email, pdf_base64, member, team, period]):
#         return jsonify({"error": "Missing one or more required fields."}), 400
    
#     try:
#         # Decode the PDF data from Base64.
#         pdf_data = base64.b64decode(pdf_base64)
#     except Exception as e:
#         return jsonify({"error": f"Invalid PDF data encoding: {e}"}), 400

#     # Email configuration
#     sender_email = "nx.ai@nxfin.in"       # Replace with your sender email
#     sender_password = "rfhw ennv swoo lono"  # Replace with your email password or use secure storage
#     subject = f"Daily Report Summary for {member} ({team}) - {period}"
#     body = "Please find attached your daily report summary."
    
#     try:
#         print("[DEBUG] Preparing email message in Flask API...")
#         msg = EmailMessage()
#         msg["Subject"] = subject
#         msg["From"] = sender_email
#         msg["To"] = recipient_email
#         msg.set_content(body)
#         msg.add_attachment(pdf_data,
#                            maintype="application",
#                            subtype="pdf",
#                            filename=f"{member}_report_{period}.pdf")
        
#         print("[DEBUG] Connecting to SMTP server from Flask API...")
#         # Example using Gmail SMTP server; adjust if needed.
#         with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
#             smtp.login(sender_email, sender_password)
#             smtp.send_message(msg)
#         print("[DEBUG] Email sent successfully via Flask API!")
#         return jsonify({"message": "Email sent successfully!"}), 200
#     except Exception as e:
#         print(f"[DEBUG] Error sending email in Flask API: {e}")
#         return jsonify({"error": str(e)}), 500



# # Run the Flask app
# if __name__ == "__main__":
#     app.run(debug=True)



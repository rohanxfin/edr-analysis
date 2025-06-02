# # streamlit.py

# import base64
# import streamlit as st
# import os
# import io
# import markdown
# from typing import List, Optional
# # Import the functions from app.py directly
# from app import summarize_report, send_email_report
# from constants import emails_list  # Assuming emails_list is defined in constants.py

# # Page configuration
# st.set_page_config(
#     page_title="Daily Report Summarizer",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# # Custom CSS styling
# def load_css():
#     css = """
#     <style>
#     body {
#         background: linear-gradient(to bottom, #f5f7fa, #c3cfe2);
#         font-family: 'Helvetica Neue', sans-serif;
#         margin: 0;
#         padding: 0;
#         font-size: 1.2rem;
#     }
#     .stApp {
#         width: 100%;
#         margin: 0;
#     }
#     h1 {
#         text-align: center;
#         color: #2c3e50;
#         font-size: 3rem;
#         margin: 2rem 0;
#     }
#     h2 {
#         color: #2c3e50;
#         font-size: 2rem;
#         margin-top: 1.5rem;
#     }
#     .sidebar .sidebar-content {
#         background: linear-gradient(180deg, #34495e, #2c3e50);
#         padding: 0.8rem;
#         width: 250px;
#     }
#     .stButton>button {
#         background-color: #2980b9;
#         color: white;
#         border: none;
#         padding: 1rem 2.5rem;
#         border-radius: 8px;
#         font-weight: 500;
#         font-size: 1.2rem;
#         transition: all 0.3s ease;
#     }
#     .stButton>button:hover {
#         background-color: #1abc9c;
#         box-shadow: 0 2px 4px rgba(0,0,0,0.1);
#     }
#     .summary-card {
#         background-color: #4AA09B;
#         border-radius: 12px;
#         padding: 1.5rem;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
#         margin: 1rem 0;
#         line-height: 1.6;
#         font-size: 1.2rem;
#     }
#     .stSelectbox > label {
#         font-size: 1.3rem;
#         color: #ecf0f1;
#     }
#     </style>
#     """
#     st.markdown(css, unsafe_allow_html=True)

# # Data handling functions
# def get_team_names() -> List[str]:
#     try:
#         return [folder for folder in os.listdir("data") if os.path.isdir(os.path.join("data", folder))]
#     except FileNotFoundError:
#         st.error("Data directory not found. Please ensure 'data' folder exists.")
#         return []
#     except Exception as e:
#         st.error(f"Error loading teams: {str(e)}")
#         return []

# def get_members(team: str) -> List[str]:
#     try:
#         team_folder = os.path.join("data", team)
#         return [file.replace('.csv', '') for file in os.listdir(team_folder) if file.endswith(".csv")]
#     except Exception as e:
#         st.error(f"Error loading members: {str(e)}")
#         return []

# from reportlab.lib.pagesizes import letter
# from reportlab.lib import colors
# from reportlab.pdfgen import canvas
# from io import BytesIO

# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet
# import io




# import re
# from io import BytesIO
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
# from reportlab.lib.pagesizes import LETTER
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# def generate_pdf(team: str, member: str, period: str, summary: str) -> bytes:
#     """
#     Generates a PDF where '**bold text**' is rendered as actual bold
#     (i.e., <b>bold text</b>) rather than showing the '**' asterisks.
#     """

#     # Prepare a buffer to hold PDF data
#     buffer = BytesIO()
#     doc = SimpleDocTemplate(buffer, pagesize=LETTER)

#     # Get default styles
#     styles = getSampleStyleSheet()
#     # Create a story flowable list
#     story = []

#     # 1) Title (example)
#     title_str = f"Daily Report Summary - {member} ({team})"
#     story.append(Paragraph(title_str, styles["Title"]))
#     story.append(Spacer(1, 10))

#     # 2) Period example
#     period_str = f"Period: {period}"
#     story.append(Paragraph(period_str, styles["Normal"]))
#     story.append(Spacer(1, 12))

#     # 3) Convert "**something**" to <b>something</b> in the summary
#     #    Also replace newline characters (\n) with <br/> so we keep line breaks.
#     processed_summary = summary.replace('\n', '<br/>')
#     processed_summary = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', processed_summary)

#     # 4) Add final summary paragraph
#     story.append(Paragraph(processed_summary, styles["Normal"]))

#     # Build the PDF
#     doc.build(story)
#     pdf_data = buffer.getvalue()
#     buffer.close()
#     return pdf_data


# # Sidebar rendering
# def render_sidebar() -> tuple:
#     st.sidebar.header("Member Selection", divider="blue")
    
#     teams = get_team_names()
#     if not teams:
#         st.sidebar.warning("No teams available")
#         return None, None, None
    
#     selected_team = st.sidebar.selectbox(
#         "1. Select Team",
#         options=[""] + teams,
#         help="Choose a team to analyze",
#         key="selected_team"
#     )
    
#     selected_member = None
#     time_period = None
    
#     if selected_team:
#         members = get_members(selected_team)
#         if members:
#             selected_member = st.sidebar.selectbox(
#                 "2. Select Member",
#                 options=[""] + members,
#                 help="Choose a team member",
#                 key="selected_member"
#             )
    
#     if selected_member:
#         time_periods = ["February", "March", "April", "Overall"]
#         time_period = st.sidebar.selectbox(
#             "3. Select Time Period",
#             options=[""] + time_periods,
#             help="Choose the time period for summary",
#             key="time_period"
#         )
    
#     return selected_team, selected_member, time_period

# # Main content rendering
# def render_main_content(team: str, member: str, period: str):
#     st.title("Daily Report Summarizer")
#     st.markdown("Select options from the sidebar to generate a customized team member report.")
    
#     col1, col2 = st.columns([2, 1])
    
#     with col1:
#         st.subheader("Generate Your Report")
#         st.markdown("Click below to create a summary based on your selections.")
        
#         # Display existing summary if available
#         if "summary" in st.session_state:
#             st.subheader("Report Summary")
#             st.markdown(f"<div class='summary-card'>{st.session_state['summary']}</div>", unsafe_allow_html=True)
        
#         button_disabled = not all([team, member, period])
#         if st.button("Generate Summary", key="generate_btn", disabled=button_disabled, use_container_width=True):
#             with st.spinner("Processing your request..."):
#                 # Directly call the summarize_report function instead of a Flask endpoint
#                 summary = summarize_report(team, member, period)
#                 if summary:
#                     st.session_state['summary'] = summary
#                     st.session_state['team'] = team
#                     st.session_state['member'] = member
#                     st.session_state['period'] = period
                    
#                     st.subheader("Report Summary")
#                     st.markdown(f"<div class='summary-card'>{summary}</div>", unsafe_allow_html=True)
        
#         # PDF and Email actions (only if summary exists)
#         if "summary" in st.session_state:
#             pdf_data = generate_pdf(team, member, period, st.session_state['summary'])
#             spacer, col_actions = st.columns([3, 1])
#             with col_actions:
#                 st.download_button(
#                     label="Download as PDF",
#                     data=pdf_data,
#                     file_name=f"{member}_report_{period}.pdf",
#                     mime="application/pdf",
#                     key="download_pdf_btn",
#                     use_container_width=True
#                 )
                
#                 if st.button("Send via Email", key="send_email_btn", use_container_width=True):
#                     recipient_email = None
                    
#                     team_emails = emails_list.get(team, [])
#                     for person in team_emails:
#                         if person.get("name", "").replace(" ", "_").lower() == member.lower():
#                             recipient_email = person.get("email")
#                             break
                    
#                     if recipient_email:
#                         # Directly call the send_email_report function
#                         success = send_email_report(recipient_email, pdf_data, member, team, period)
#                         if success:
#                             st.success("Email sent successfully!")
#                         else:
#                             st.error("Failed to send email.")
#                     else:
#                         st.error("Recipient email not found.")
    
#     with col2:
#         st.subheader("Current Selection")
#         st.info(
#             f"**Team:** {team or 'Not selected'}\n\n"
#             f"**Member:** {member or 'Not selected'}\n\n"
#             f"**Period:** {period or 'Not selected'}"
#         )

# def main():
#     load_css()
#     selected_team, selected_member, time_period = render_sidebar()
    
#     # Use session state as fallback if selections are incomplete
#     if not selected_team and "team" in st.session_state:
#         selected_team = st.session_state["team"]
#     if not selected_member and "member" in st.session_state:
#         selected_member = st.session_state["member"]
#     if not time_period and "period" in st.session_state:
#         time_period = st.session_state["period"]
    
#     if all([selected_team, selected_member, time_period]):
#         render_main_content(selected_team, selected_member, time_period)
#     else:
#         st.title("Daily Report Summarizer")
#         st.warning("Please complete all selections in the sidebar to proceed.")

# if __name__ == "__main__":
#     main()


# streamlit.py

# streamlit.py

# streamlit.py

import base64
import streamlit as st
import os
import io
from io import BytesIO
import markdown
from typing import List, Optional
from app import summarize_report, send_email_report
from constants import emails_list
import re
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from datetime import datetime
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Daily Report Summarizer",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS styling
def load_css():
    css = """
    <style>
    body {
        background: linear-gradient(to bottom, #f5f7fa, #c3cfe2);
        font-family: 'Helvetica Neue', sans-serif;
        margin: 0;
        padding: 0;
        font-size: 1.2rem;
    }
    .stApp {
        width: 100%;
        margin: 0;
    }
    h1 {
        text-align: center;
        color: #2c3e50;
        font-size: 3rem;
        margin: 2rem 0;
    }
    h2 {
        color: #2c3e50;
        font-size: 2rem;
        margin-top: 1.5rem;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #34495e, #2c3e50);
        padding: 0.8rem;
        width: 250px;
    }
    .stButton>button {
        background-color: #2980b9;
        color: white;
        border: none;
        padding: 1rem 2.5rem;
        border-radius: 8px;
        font-weight: 500;
        font-size: 1.2rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1abc9c;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stSelectbox > label {
        font-size: 1.3rem;
        color: #ecf0f1;
    }
    .stTextInput > label {
        font-size: 1.3rem;
        color: #2c3e50;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Data handling functions
def get_team_names() -> List[str]:
    try:
        return [folder for folder in os.listdir("data") if os.path.isdir(os.path.join("data", folder))]
    except FileNotFoundError:
        st.error("Data directory not found. Please ensure 'data' folder exists.")
        return []
    except Exception as e:
        st.error(f"Error loading teams: {str(e)}")
        return []

def get_members(team: str) -> List[str]:
    try:
        team_folder = os.path.join("data", team)
        return [file.replace('.csv', '') for file in os.listdir(team_folder) if file.endswith(".csv")]
    except Exception as e:
        st.error(f"Error loading members: {str(e)}")
        return []

def generate_pdf(team: str, member: str, period: str, summary: str) -> bytes:
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=LETTER)
    styles = getSampleStyleSheet()
    story = []

    title_str = f"Report Summary - {member} ({team})"
    story.append(Paragraph(title_str, styles["Title"]))
    story.append(Spacer(1, 10))

    period_str = f"Period: {period}"
    story.append(Paragraph(period_str, styles["Normal"]))
    story.append(Spacer(1, 12))

    processed_summary = summary.replace('\n', '<br/>')
    processed_summary = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', processed_summary)
    story.append(Paragraph(processed_summary, styles["Normal"]))

    doc.build(story)
    pdf_data = buffer.getvalue()
    buffer.close()
    return pdf_data

def validate_emails(email_input: str) -> List[str]:
    emails = [email.strip() for email in email_input.split(",") if email.strip()]
    valid_emails = []
    for email in emails:
        if re.match(r'^[\w\.-]+@(nxfin\.in|nxfin\.com)$', email):
            valid_emails.append(email)
        else:
            st.warning(f"Invalid email: {email}. Emails must end with @nxfin.in or @nxfin.com.")
    return valid_emails

def summarize_daily_report(team: str, member: str, month: str) -> str:
    try:
        csv_path = os.path.join("data", team, f"{member}.csv")
        df = pd.read_csv(csv_path)
        df['datetime'] = pd.to_datetime(df['date'], format="%d %b %Y, %H:%M")
        
        if month.lower() != "overall":
            month_number = datetime.strptime(month, "%B").month
            df = df[df['datetime'].dt.month == month_number]
        
        daily_summaries = []
        for date in sorted(df['datetime'].dt.date.unique()):
            daily_df = df[df['datetime'].dt.date == date]
            daily_df["data"] = daily_df["from"] + " " + daily_df["content"] + " " + daily_df["date"]
            text_data = "\n".join(daily_df['data'].tolist())
            
            from app import genai, generation_config
            from prompts import get_daily_prompt
            model = genai.GenerativeModel(
                model_name="gemini-1.5-flash-8b",
                generation_config=generation_config,
                system_instruction=get_daily_prompt(team)
            )
            chat_session = model.start_chat(history=[])
            response = chat_session.send_message(text_data)
            daily_summary = f"**Date: {date}**\n{response.text}"
            daily_summaries.append(daily_summary)
        
        return "\n\n---\n\n".join(daily_summaries)
    except Exception as e:
        print(f"Error in daily report generation: {str(e)}")
        return "The EDR's was not in structured form to generate proper summary."

# Sidebar rendering
def render_sidebar() -> tuple:
    st.sidebar.header("Member Selection", divider="blue")
    
    teams = get_team_names()
    if not teams:
        st.sidebar.warning("No teams available")
        return None, None, None
    
    selected_team = st.sidebar.selectbox(
        "1. Select Team",
        options=[""] + teams,
        help="Choose a team to analyze",
        key="selected_team"
    )
    
    selected_member = None
    time_period = None
    
    if selected_team:
        members = get_members(selected_team)
        if members:
            selected_member = st.sidebar.selectbox(
                "2. Select Member",
                options=[""] + members,
                help="Choose a team member",
                key="selected_member"
            )
    
    if selected_member:
        time_periods = ["February", "March", "April", "May" , "Overall"]
        time_period = st.sidebar.selectbox(
            "3. Select Time Period",
            options=[""] + time_periods,
            help="Choose the time period for summary",
            key="time_period"
        )
    
    return selected_team, selected_member, time_period

# Main content rendering
def render_main_content(team: str, member: str, period: str):
    st.title("Daily Report Summarizer")
    st.markdown("Select options from the sidebar to generate a customized team member report.")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Generate Your Report")
        st.markdown("Click below to create a monthly or daily summary based on your selections.")
        
        button_disabled = not all([team, member, period])
        col_monthly, col_daily, col_reset = st.columns([1, 1, 1])
        
        with col_monthly:
            if st.button("Generate Monthly Report", key="generate_monthly_btn", disabled=button_disabled, use_container_width=True):
                with st.spinner("Processing your monthly report..."):
                    # Clear previous summary
                    if 'summary' in st.session_state:
                        del st.session_state['summary']
                    summary = summarize_report(team, member, period)
                    if summary:
                        st.session_state['summary'] = summary
                        st.session_state['team'] = team
                        st.session_state['member'] = member
                        st.session_state['period'] = period
                        st.session_state['report_type'] = 'monthly'
        
        with col_daily:
            if st.button("Generate Daily Report", key="generate_daily_btn", disabled=button_disabled, use_container_width=True):
                with st.spinner("Processing your daily report..."):
                    # Clear previous summary
                    if 'summary' in st.session_state:
                        del st.session_state['summary']
                    summary = summarize_daily_report(team, member, period)
                    if summary:
                        st.session_state['summary'] = summary
                        st.session_state['team'] = team
                        st.session_state['member'] = member
                        st.session_state['period'] = period
                        st.session_state['report_type'] = 'daily'
        
        with col_reset:
            if st.button("Reset", key="reset_btn", use_container_width=True):
                st.session_state.clear()
                st.rerun()
        
        if "summary" in st.session_state:
            report_type = st.session_state.get('report_type', 'monthly')
            pdf_data = generate_pdf(team, member, f"{period} ({report_type.capitalize()})", st.session_state['summary'])
            spacer, col_actions = st.columns([3, 1])
            with col_actions:
                st.download_button(
                    label="Download as PDF",
                    data=pdf_data,
                    file_name=f"{member}_report_{period}_{report_type}.pdf",
                    mime="application/pdf",
                    key="download_pdf_btn",
                    use_container_width=True
                )
                
                email_input = st.text_input(
                    "Enter recipient email(s) (comma-separated, e.g., user1@nxfin.in,user2@nxfin.com)",
                    key="email_input"
                )
                
                if st.button("Send via Email", key="send_email_btn", use_container_width=True):
                    if email_input:
                        valid_emails = validate_emails(email_input)
                        if valid_emails:
                            success_count = 0
                            for email in valid_emails:
                                success = send_email_report(email, pdf_data, member, team, f"{period} ({report_type.capitalize()})")
                                if success:
                                    success_count += 1
                            if success_count == len(valid_emails):
                                st.success("Email(s) sent successfully to all recipients!")
                            else:
                                st.error(f"Failed to send email to {len(valid_emails) - success_count} recipient(s).")
                        else:
                            st.error("No valid emails provided.")
                    else:
                        st.error("Please enter at least one email address.")
    
    with col2:
        st.subheader("Current Selection")
        st.info(
            f"**Team:** {team or 'Not selected'}\n\n"
            f"**Member:** {member or 'Not selected'}\n\n"
            f"**Period:** {period or 'Not selected'}"
        )
    
    # Full-width report display
    if "summary" in st.session_state:
        st.subheader(f"{st.session_state['report_type'].capitalize()} Report Summary")
        if st.session_state['summary'] == "The EDR's was not in structured form to generate proper summary.":
            st.error(st.session_state['summary'])
        else:
            st.markdown(st.session_state['summary'], unsafe_allow_html=True)

def main():
    load_css()
    selected_team, selected_member, time_period = render_sidebar()
    
    if not selected_team and "team" in st.session_state:
        selected_team = st.session_state["team"]
    if not selected_member and "member" in st.session_state:
        selected_member = st.session_state["member"]
    if not time_period and "period" in st.session_state:
        time_period = st.session_state["period"]
    
    if all([selected_team, selected_member, time_period]):
        render_main_content(selected_team, selected_member, time_period)
    else:
        st.title("Daily Report Summarizer")
        st.warning("Please complete all selections in the sidebar to proceed.")

if __name__ == "__main__":
    main()
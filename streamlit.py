# streamlit.py

import base64
import streamlit as st
import os
import io
import markdown
from typing import List, Optional
# Import the functions from app.py directly
from app import summarize_report, send_email_report
from constants import emails_list  # Assuming emails_list is defined in constants.py

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
    .summary-card {
        background-color: #4AA09B;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin: 1rem 0;
        line-height: 1.6;
        font-size: 1.2rem;
    }
    .stSelectbox > label {
        font-size: 1.3rem;
        color: #ecf0f1;
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

<<<<<<< HEAD


# def generate_pdf(team: str, member: str, period: str, summary: str) -> bytes:
#     """
#     Generates a PDF file from the summary and returns the PDF as a byte string.
#     """
#     markdown_text = (
#         f"# Daily Report Summary - {member} ({team})\n\n"
#         f"**Period:** {period}\n\n"
#         "## Summary\n\n"
#         f"{summary}"
#     )
#     html_content = markdown.markdown(markdown_text)
#     css_string = """
#     body {
#         font-family: "Times New Roman", serif;
#         margin: 20px;
#     }
#     h1, h2, h3, h4, h5, h6 {
#         font-family: "Times New Roman", serif;
#     }
#     """
#     css = CSS(string=css_string)
#     pdf_bytes = HTML(string=html_content).write_pdf(stylesheets=[css])
#     return pdf_bytes
=======
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from io import BytesIO

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import io


>>>>>>> c00f0cc310ce695f1b60c6099973e99e23b04e7b


import re
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_pdf(team: str, member: str, period: str, summary: str) -> bytes:
    """
    Generates a PDF where '**bold text**' is rendered as actual bold
    (i.e., <b>bold text</b>) rather than showing the '**' asterisks.
    """

    # Prepare a buffer to hold PDF data
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=LETTER)

    # Get default styles
    styles = getSampleStyleSheet()
    # Create a story flowable list
    story = []

    # 1) Title (example)
    title_str = f"Daily Report Summary - {member} ({team})"
    story.append(Paragraph(title_str, styles["Title"]))
    story.append(Spacer(1, 10))

    # 2) Period example
    period_str = f"Period: {period}"
    story.append(Paragraph(period_str, styles["Normal"]))
    story.append(Spacer(1, 12))

    # 3) Convert "**something**" to <b>something</b> in the summary
    #    Also replace newline characters (\n) with <br/> so we keep line breaks.
    processed_summary = summary.replace('\n', '<br/>')
    processed_summary = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', processed_summary)

    # 4) Add final summary paragraph
    story.append(Paragraph(processed_summary, styles["Normal"]))

    # Build the PDF
    doc.build(story)
    pdf_data = buffer.getvalue()
    buffer.close()
    return pdf_data


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
        time_periods = ["February", "March", "April", "Overall"]
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
        st.markdown("Click below to create a summary based on your selections.")
        
        # Display existing summary if available
        if "summary" in st.session_state:
            st.subheader("Report Summary")
            st.markdown(f"<div class='summary-card'>{st.session_state['summary']}</div>", unsafe_allow_html=True)
        
        button_disabled = not all([team, member, period])
        if st.button("Generate Summary", key="generate_btn", disabled=button_disabled, use_container_width=True):
            with st.spinner("Processing your request..."):
                # Directly call the summarize_report function instead of a Flask endpoint
                summary = summarize_report(team, member, period)
                if summary:
                    st.session_state['summary'] = summary
                    st.session_state['team'] = team
                    st.session_state['member'] = member
                    st.session_state['period'] = period
                    
                    st.subheader("Report Summary")
                    st.markdown(f"<div class='summary-card'>{summary}</div>", unsafe_allow_html=True)
        
        # PDF and Email actions (only if summary exists)
        if "summary" in st.session_state:
            pdf_data = generate_pdf(team, member, period, st.session_state['summary'])
            spacer, col_actions = st.columns([3, 1])
            with col_actions:
                st.download_button(
                    label="Download as PDF",
                    data=pdf_data,
                    file_name=f"{member}_report_{period}.pdf",
                    mime="application/pdf",
                    key="download_pdf_btn",
                    use_container_width=True
                )
                
                if st.button("Send via Email", key="send_email_btn", use_container_width=True):
                    recipient_email = None
                    
                    team_emails = emails_list.get(team, [])
                    for person in team_emails:
                        if person.get("name", "").replace(" ", "_").lower() == member.lower():
                            recipient_email = person.get("email")
                            break
                    
                    if recipient_email:
                        # Directly call the send_email_report function
                        success = send_email_report(recipient_email, pdf_data, member, team, period)
                        if success:
                            st.success("Email sent successfully!")
                        else:
                            st.error("Failed to send email.")
                    else:
                        st.error("Recipient email not found.")
    
    with col2:
        st.subheader("Current Selection")
        st.info(
            f"**Team:** {team or 'Not selected'}\n\n"
            f"**Member:** {member or 'Not selected'}\n\n"
            f"**Period:** {period or 'Not selected'}"
        )

def main():
    load_css()
    selected_team, selected_member, time_period = render_sidebar()
    
    # Use session state as fallback if selections are incomplete
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



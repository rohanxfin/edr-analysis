# prompts.py

# Define different prompt templates for each team.

sales_team_prompt = """         

Give response in well structure  format with clear insights and key points, i will dispaly on my streamlit frontend,dont write ``` or md or markdown in beginning of the response, just write the response , i will convert the md text by myself.
Give point wise , with space between each point, and use **bold** for headings and sub headings.
striclty avoid the usage of words like etc , others , many more as i need full details in the report, no names or numbers should be missed in the report.
You will be provided with the following monthly work reports:
{
monthly_work_reports
}

Analyze the reports and create a detailed summary in the following format:

**Dealer Visits and Discussions**
* Total number of dealerships visited (e.g., "Total Dealerships Visited: 25"), including a sample list of notable dealers (e.g., "Notable Dealers: Dealer A, Dealer B, Dealer C, and others").
* Key topics discussed with dealers (e.g., "Key Discussion Topics: CF cases, insurance, warranties, car scope activities").
* Specific CF cases collected from dealers, with counts and dealer names (e.g., "CF Cases Collected: 10 cases (3 from Dealer A, 2 from Dealer B, 5 from Dealer C)").

**CF Case Updates**
* Number of CF cases received from dealers (format: "CF CASE RECEIVE - [number]").
* Number of CF cases approved (format: "APPROVED CASE - [number]").
* Number of CF cases disbursed (format: "CF CASE RECEIVED - [number]").

**New Dealer Onboarding**
* Number of new dealers onboarded (e.g., "New Dealers Onboarded: 5"), with a sample list of names (e.g., "New Dealers: Dealer X, Dealer Y, Dealer Z, and others").
* Additional onboarding actions taken (e.g., "Onboarding Actions: Created WhatsApp groups, scheduled initial training sessions").

**Market Updates**
* Overview of market conditions affecting sales (e.g., "Market Conditions: Heavy rainfall impacted sales in the North region. New regulations on vehicle financing are expected next month.").
* Dealer feedback or interest areas (e.g., "Dealer Feedback: High interest in CF case resolution and extended warranty options.").

**Other**
* Additional activities not covered above (e.g., "Other Activities: Conducted car scope analysis at Dealer P and Dealer Q. Discussed upcoming CF file changes with Dealer R.").

**Dealer Visit Count**
* Exact count of visits per dealer in alphabetical order (e.g., "Dealer A: 3", "Dealer B: 2", "Dealer C: 1").

Example:

Input Monthly Work Reports:
"Visited Dealer A, discussed CF cases and insurance. Visited Dealer B, discussed warranties. Received 5 CF cases. Onboarded Dealer X. Heavy rain affected sales."

Output Summary:

**Dealer Visits and Discussions**
* Total Dealerships Visited: 2
* Notable Dealers: Dealer A, Dealer B
* Key Discussion Topics: CF cases, insurance, warranties
* CF Cases Collected: Not specified in reports

**CF Case Updates**
* CF CASE RECEIVE - 5
* APPROVED CASE - Not specified in reports
* CF CASE RECEIVED - Not specified in reports

**New Dealer Onboarding**
* New Dealers Onboarded: 1
* New Dealers: Dealer X
* Onboarding Actions: Not specified in reports

**Market Updates**
* Market Conditions: Heavy rain affected sales.
* Dealer Feedback: Not specified in reports

**Other**
* No other activities reported.

**Dealer Visit Count**
* Dealer A: 1
* Dealer B: 1

Ensure all data is extracted from the reports. Include specific dealer names and numbers where available, and summarize effectively when data is extensive. Use bullet points under each section as shown.
The report should be exhaustive, covering all details including names, numbers, dates, locations, car dealer interactions, file statuses, disbursement information, and any other relevant information. Structure the report clearly and logically, potentially using tables or bullet points to organize the data effectively. Ensure all the information from the provided text is included in the report.
"""


    
PROMPTS = {
    "Product Development EDR": 
        "Analyze the monthly work reports from a member of Product Development EDR team. Provide a concise summary with the following sections:\n"
        "foucus on writing the end result of completed task , ongoing work and pending items, rather than writing intermediate achivement, if the task is not complteted than go for intermediate issues\n"
        "- **Completed tasks:** List specific features, modules, or components completed, including successful tests, deployments, or integrations.\n"
        "- **Ongoing work:** Describe the status of major projects or sprints, noting ongoing tasks like coding, testing, or debugging.\n"
        "- **Pending items:** Highlight tasks behind schedule, bugs needing fixes, or backlog features.\n"
        "- **Key insights:** Identify patterns in challenges (e.g., resource constraints) or successes (e.g., meeting deadlines), and note any innovations or process improvements.\n"
        "Use bullet points for each section and limit key insights to 2-3 sentences.",

    "HR and Admin": 
        "Analyze the monthly work reports from a member HR and Admin team. Provide a concise summary with the following sections:\n"
        "- **Completed tasks:** List finalized HR and administrative duties, such as new hires onboarded, payroll processed, or office maintenance.\n"
        "- **Ongoing work:** Describe continuing processes like recruitment, training, or performance reviews.\n"
        "- **Pending items:** Highlight overdue tasks, such as pending background checks or unresolved issues.\n"
        "- **Key insights:** Identify recurring themes, like difficulties in hiring or efficiency gains from new procedures.\n"
        "Use bullet points for each section and limit key insights to 2-3 sentences.",

    "Management EDR": 
        "Analyze the monthly work reports from a member of Management EDR team. Provide a concise summary with the following sections:\n"
        "- **Completed tasks:** List strategic decisions made, projects approved, or resource allocations finalized.\n"
        "- **Ongoing work:** Describe current activities, such as project monitoring or strategy development.\n"
        "- **Pending items:** Highlight pending decisions, reports needing review, or scheduled meetings.\n"
        "- **Key insights:** Look for patterns in decision-making, such as delays in approvals or effective risk management.\n"
        "Use bullet points for each section and limit key insights to 2-3 sentences.",

    "Marketing EDR": 
        "Analyze the monthly work reports from a member of the Marketing EDR team. Provide a concise summary with the following sections:\n"
        "- **Completed tasks:** List campaigns launched, content published, or events organized.\n"
        "- **Ongoing work:** Describe current activities, such as social media management, market research, or branding.\n"
        "- **Pending items:** Highlight delayed campaigns, unfinished content, or upcoming deadlines.\n"
        "- **Key insights:** Identify successful strategies, customer engagement trends, or areas for improvement.\n"
        "Use bullet points for each section and limit key insights to 2-3 sentences.",

    "Accounts EDR": 
        "Analyze the monthly work reports from the member of Accounts EDR team. Provide a concise summary with the following sections:\n"
        "- **Completed tasks:** List financial tasks completed, such as invoices processed, payments received, or financial statements prepared.\n"
        "- **Ongoing work:** Describe continuing activities, like budget tracking, expense monitoring, or tax preparation.\n"
        "- **Pending items:** Highlight overdue payments, unresolved discrepancies, or upcoming deadlines.\n"
        "- **Key insights:** Look for patterns in financial management, such as cash flow issues or cost-saving measures.\n"
        "Use bullet points for each section and limit key insights to 2-3 sentences." ,

    "BLR EDR": sales_team_prompt, 
    "DEL NCR EDR": sales_team_prompt,
    "Himachal EDR": sales_team_prompt,
    "HYD EDR": sales_team_prompt,
    "Kolkata EDR":  sales_team_prompt,
    "MUM EDR": sales_team_prompt,
    "PUNE EDR": sales_team_prompt, 
    "Punjab and Chd EDR": sales_team_prompt,
    "RJ EDR": sales_team_prompt
}





def get_prompt(team: str) -> str:
    """
    Returns the team-specific prompt. If the team is not found,
    a default prompt is returned.
    """
    return PROMPTS.get(team, "Summarize the work report with clear insights and key points.")

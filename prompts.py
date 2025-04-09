# prompts.py

# Define different prompt templates for each team.

sales_team_prompt = """        

"Analyze the monthly work reports from a member of Sales EDR team and provide an in-depth summary focusing on sales performance with the following sections:\n"
        "- **Completed Sales & Conversions:** List the name and number of all the deals closed, total revenue generated, and key clients acquired. Include conversion rates (e.g., leads to sales) and highlight top-performing products or services.\n"
        "- **Places Visited:** Summarize all the locations (e.g., cities, regions) visited by the team, noting the frequency of visits and key outcomes (e.g., names , new leads, follow-ups, or deals).\n"
        "- **Dealers Engaged:** Detail interactions with dealers, including the number of dealers contacted, meetings held, and outcomes (e.g., partnerships formed, orders placed, or issues raised).\n"
        "- **Ongoing Efforts:** Describe active sales pursuits, such as leads in negotiation, follow-ups scheduled, or pipeline development, with estimated timelines or values where possible.\n"
        "- **Pending Items:** Highlight stalled deals, missed targets, overdue follow-ups, or unvisited priority locations/dealers, noting reasons for delays if provided.\n"
        "- **Key Insights:** Analyze patterns in conversion success (e.g., high-performing regions or products), challenges (e.g., dealer resistance, travel constraints), and opportunities (e.g., untapped markets or repeat clients). Suggest one actionable step based on the data.\n"
        "Use bullet points for each section and limit key insights to 3-4 sentences for depth."
        "mention all the names of each dealer and the places visited by the team in the summary"
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

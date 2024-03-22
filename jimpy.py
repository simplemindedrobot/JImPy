import os
import csv
from jira import JIRA
import pandas as pd

# Access token from environment variable
access_token = os.getenv('JIRA_ACCESS_TOKEN')

# Connect to JIRA
jira = JIRA(server='https://your-jira-server.atlassian.net', basic_auth=('email@example.com', access_token))

# Read issues from CSV
issues = []
with open('issues.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    for row in reader:
        issues.append({'summary': row[0], 'description': row[1], 'issuetype': {'name': 'Bug'}})

# Write issues to JIRA and store new issues
new_issues = []
for issue in issues:
    new_issue = jira.create_issue(project='PROJ', summary=issue['summary'], description=issue['description'], issuetype={'name': 'Bug'})
    new_issues.append({'id': new_issue.id, 'summary': new_issue.fields.summary})

# Write new issues to CSV
df = pd.DataFrame(new_issues)
df.to_csv('new_issues.csv', index=False)
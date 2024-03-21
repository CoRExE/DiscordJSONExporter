import datetime
import os
import json
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

# Set the path to the directory containing the JSON files
json_dir = './'

# Set the path to the template directory for the Jinja2 environment
template_dir = './template'

# Create a Jinja2 environment and loader
env = Environment(loader=FileSystemLoader(template_dir))

def format_datetime(value, format='%Y-%m-%d %H:%M:%S'):
    return value.strftime(format)

env.filters['format_datetime'] = format_datetime

# Create a dictionary to store the report data
report_data = {}

# Create a list to store the report authors
report_authors = []

# Loop through each JSON file in the directory
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)

        # Load the JSON data from the file
        with open(file_path, 'r') as f:
            json_data = json.load(f)

        # Check if the JSON file contains a list of messages
        if isinstance(json_data, list) and len(json_data) > 0 and all(isinstance(msg, dict) and 'author' in msg and 'content' in msg for msg in json_data):
            # Convert the timestamps to a readable format
            for msg in json_data:
                msg['timestamp'] = datetime.strptime(msg['timestamp'], '%Y-%m-%dT%H:%M:%S.%f%z').replace(tzinfo=None)
                if msg.get('edited_timestamp'):
                    msg['edited_timestamp'] = datetime.strptime(msg['edited_timestamp'], '%Y-%m-%dT%H:%M:%S.%f%z').replace(tzinfo=None)
                # Add the author to the list of report authors if not already present
                if msg['author']['username'] not in report_authors:
                    report_authors.append(msg['author']['username'])

            # Add the JSON data to the report data dictionary
            report_data[filename] = json_data

# Load the HTML template from the template directory
template = env.get_template('index.html')

# Render the HTML template with the report data and authors
html_output = template.render(report_data=report_data, report_authors=report_authors)

# Write the HTML output to a file
with open('report.html', 'w', encoding='utf-8') as f:
    f.write(html_output)

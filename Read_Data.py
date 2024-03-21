import json
import os

folder_path = './' # replace with the path to your folder

for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as f:
            data = json.load(f)
            if 'url' in data:
                print(f"Filename : {filename}, Url: {data['url']}")

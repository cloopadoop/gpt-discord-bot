import csv
import sys
import yaml
from tqdm import tqdm

if len(sys.argv) < 2:
    print("Usage: python script.py <filename.yaml> [encoding]")
    sys.exit(1)

filename = sys.argv[1]
encoding = 'utf-8' if len(sys.argv) < 3 else sys.argv[2]

with open(filename, 'r', encoding=encoding) as file:
    data = yaml.safe_load(file)

total_messages = sum(len(conversation['messages']) for conversation in data['example_conversations'])

with open('conversations.csv', 'w', newline='', encoding=encoding) as file:
    writer = csv.writer(file)
    writer.writerow(['User', 'Text'])
    for conversation in tqdm(data['example_conversations'], total=total_messages, desc='Conversations'):
        for message in conversation['messages']:
            if 'text' in message:
                writer.writerow([message['user'], message['text']])
            else:
                print(f"Error: message missing 'text' key: {message}")

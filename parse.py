import json
import os

data = json.load(open('email_domains.json'))
if os.path.exists('email_domains.txt'):
    os.remove('email_domains.txt')
output = open('email_domains.txt', 'a')
domains = []
for row in data:
    domains.append(row['domain'])
domains.sort()
domains = list(dict.fromkeys(domains))
output.write('\n'.join(domains))
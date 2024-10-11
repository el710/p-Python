"""
pip install openpyxl
"""
import requests
import pandas
import pprint

import os

os.system('git commit -am "new stage"')
os.system('git push')

print('Request: get()...\n')
req = requests.get('https://api.github.com/events')
print(f'Request URL: {req.url}')
print(f'status: {req.status_code}')
print(f'apparent_encoding: {req.apparent_encoding}')

data = req.json()
pprint.pprint(f'{pandas.Series(data[0])}')

df = pandas.DataFrame(
    {
        "login": [x['actor']['login'] for x in data],
        "repo_name": (x['repo']['name'] for x in data),
        "type": (x['type'] for x in data)
    }
)
df.to_excel('sheet.xlsx', sheet_name="sheet 1")





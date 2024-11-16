"""
pip install openpyxl
"""
import requests
import pandas
import pprint
from pandas import read_excel
import os


print('\nPOST request...')
r = requests.post('https://httpbin.org/post', data={'my_key': 'value1'})
pprint.pprint(r.json())

print('\nDEL request...')
r = requests.delete('https://httpbin.org/delete')
pprint.pprint(r.json())

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

new_df = read_excel('sheet.xlsx', sheet_name="sheet 1")
pprint.pprint(new_df)



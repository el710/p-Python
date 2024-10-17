import requests
import pprint
import json

print('Request: get()...\n')

# Response_object = requests.get(url=, 
#                                params=, 
#                                data=,
#                                headers=dictionary of HTTP headers to send - {"HTTP_HOST": "MyVeryOwnHost"} (HTTP_CONNECTION, HTTP_ACCEPT,....)
#                                cookies= dictionary of cookies to send to the specified url - {"favcolor": "Red"}
#                                files=None,
#                                auth=authothication - ('user', 'pass'),
#                                timeout= number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or send a response - timeout=0.001
#                                allow_redirects=Boolean to enable/disable redirection - True/False
#                                proxies=dictionary of the protocol to the proxy url - { "https" : "https://1.1.0.1:80"}
#                                hooks=None,
#                                stream=indication if the response should be immediately downloaded (False) or streamed (True)
#                                verify=Boolean or a String indication to verify the servers TLS certificate or not - verify='folder/tlscertificate'
#                                cert=String or Tuple specifying a cert file or key - 'folder/myclient.cert'
#                                json=None)

r = requests.get('https://api.github.com/events')
data = r.json()
pprint.pprint(data)
print(f'simple get(): {r.status_code}\n')
print(f'get(): {data[0].keys()}')


# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('https://httpbin.org/get', params=payload)
# print(f'get(params=): {r.url}\n')


# print('\nPOST request...')
# r = requests.post('https://httpbin.org/post', data={'my_key': 'value1'})
# pprint.pprint(r.json())

# r = requests.post('https://api.github.com/some/endpoint', data=json.dumps(payload))
# print(f'post(data=): {r.text}\n')

# r = requests.post('https://api.github.com/some/endpoint', json=payload)
# print(f'post(json=): {r.text}\n')




# print('\nPUT request...')
# r = requests.put('https://httpbin.org/put', data={'my_key': 'value2'})
# pprint.pprint(r.json())

# r = requests.delete('https://httpbin.org/delete')

# r = requests.head('https://httpbin.org/get')

# r = requests.options('https://httpbin.org/get')
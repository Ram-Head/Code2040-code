# Contributor: Maya Ramsey
# Description: Challenge II: reverse a string recieved from API.
# ---------------------------------------------------------------

import json
import requests

#accessing endpoint
payload1 = {'token' : '26200b75083ca3fdb0381b8815534373'}
url = 'http://challenge.code2040.org/api/reverse'
urlRev = 'http://challenge.code2040.org/api/reverse/validate'
response = requests.post(url, data=payload1)

#reverse string
print(response.text)
string = ''.join(reversed(response.text))
print(string)

# post reversed string
payload2 = {'token' : '26200b75083ca3fdb0381b8815534373', 'string' : string}
r = requests.post(urlRev, data=payload2)
post(r)

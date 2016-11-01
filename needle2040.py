import json
import requests

# accessing endpoint
payload1 = {'token' : '26200b75083ca3fdb0381b8815534373'}
url = 'http://challenge.code2040.org/api/haystack'
urlValid = 'http://challenge.code2040.org/api/haystack/validate'
response = requests.post(url, data=payload1)

# convert information
data  = json.loads(response.text)
haystack = data['haystack']
needle = data['needle']

#find needle
needleIndex = haystack.index(needle)

# post needleIndex
payload2 = {'token' : '26200b75083ca3fdb0381b8815534373', 'needle' : needleIndex}
r = requests.post(urlValid, data=payload2)
print(r)

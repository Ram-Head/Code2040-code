# Contributor: Maya Ramsey
# Description: Contents: Challenge IV: Recieves array and prefix string from API 
# and returns array of all the strings in the original array without the prefix.
# -----------------------------------------------------------------------------

import json
import requests

# access endpoint
payload1 = {'token' : '26200b75083ca3fdb0381b8815534373'}
url = 'http://challenge.code2040.org/api/prefix'
urlValid = 'http://challenge.code2040.org/api/prefix/validate'
response = requests.post(url, json=payload1)

response.status_code
print(response.text)

# convert information
data  = json.loads(response.text)
prefix = data['prefix']
array = data['array']

# remove elements with prefix from array
index = len(array) -1
while(index >= 0):
    if(array[index].startswith(prefix)):
        del array[index]
    index -= 1


print(array)

# post array
payload2 = {"token" : '26200b75083ca3fdb0381b8815534373', "array" : array}
r = requests.post(urlValid, json = payload2)
print(r.text)

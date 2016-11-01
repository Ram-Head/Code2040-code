# Contributor: Maya Ramsey
# Description: Contents: date2040.py - Challenge V: Recieves ISO 8601 datestamp 
# and interval in seconds from API. Returns sum of datestamp and interval ISO 8601 format.
# ------------------------------------------------------------

import json
import requests
import datetime
import dateutil.parser
import iso8601

# accessing endpoint
payload1 = {'token' : '26200b75083ca3fdb0381b8815534373'}
url = 'http://challenge.code2040.org/api/dating'
urlValid = 'http://challenge.code2040.org/api/dating/validate'
response = requests.post(url, json=payload1)

response.status_code

# convert information
print(response.text)
data  = json.loads(response.text)
datestamp = data['datestamp']
interval = data['interval']

# Turn datestamp into datetime, increment and then turn back into iso 8601 format
oldDate = iso8601.parse_date(datestamp)
newDate =  oldDate + datetime.timedelta(0, interval)
finalDate = newDate.isoformat()
returnDate = finalDate[:-6]
returnDate += 'Z'
print(returnDate)

# post updated date
payload2 = {"token" : '26200b75083ca3fdb0381b8815534373', "datestamp" : returnDate}
r = requests.post(urlValid, json=payload2)
print(r.text)

#Homework: Extracting Data from JSON

import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

## Test Data ##
url = 'http://py4e-data.dr-chuck.net/comments_42.json'
#url = 'http://py4e-data.dr-chuck.net/comments_773861.json'
#sum = 2553, 2039

#url = input('Enter location: ')
print('Retrieving', url)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
string = data.decode()
#print(string)

info = json.loads(string)
print(type(info))
tot = 0

for item in info['comments'] :
	num = item['count']
	tot = tot + num

print('Count: ', len(info['comments']))
print('Sum: ', tot)
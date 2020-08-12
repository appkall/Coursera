#Homework: Extracting Data from XML

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

## Test Data ##
#url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
#url = 'http://py4e-data.dr-chuck.net/comments_773860.xml'
#sum = 2553, 2257

url = input('Enter URL: ')
print('Retrieving', url)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

lst = tree.findall('comments/comment')

tot = 0
for item in lst :
	#print('Count', item.find('count').text)
	num = int(item.find('count').text)
	tot = tot + num

print('Count:', len(lst))
print('Sum:', tot)
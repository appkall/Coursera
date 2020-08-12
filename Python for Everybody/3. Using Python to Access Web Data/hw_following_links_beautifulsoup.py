#Homework: Following Links with BeautifulSoup

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

## Test Data ##
#url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url = 'http://py4e-data.dr-chuck.net/known_by_Annabelle.html'
#count = 4
#position = 3

## Inputs ##
num = 0
#url = input('Enter URL: ')
count = input('Enter count: ')
position = input('Enter position: ')
print('Retrieving', url)

count = int(count)
position = int(position)

while num <= count - 1 :
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')

	links = []

	for tag in tags :
		data = tag.get('href', None)
		links.append(data)

	num = num + 1
	url = links[position - 1]
	print('Retrieving:', links[position - 1])
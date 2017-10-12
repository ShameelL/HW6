import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter your count:'))
position = int(input('Enter your position:'))

for i in range(int(count)):
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	number = 0
	for tag in tags:
	    number += 1
	    if number == int(position):
	    	url = tag.get('href')
	    	if i == int(count) - 1:
	    		print (tag.contents[0])
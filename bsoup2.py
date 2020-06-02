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

url = input('Enter Url - ')
count = int(input('Enter Count - '))
inputposition = int(input('Enter Position - '))
indexposition = inputposition -1
#html = urllib.request.urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
#tags = soup('a')
#print('Retrieving:', tags[2].get('href', None))
# for tag in tags:
#     line = tag.split()
#     print (line[4])
    #print(tag.get('href', None))

n = 0
while n < count:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print('Retrieving:', tags[indexposition].get('href', None))
    url = tags[indexposition].get('href', None)
    n = n + 1

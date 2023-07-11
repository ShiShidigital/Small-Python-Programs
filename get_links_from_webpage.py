import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('URL: > ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
print()
#Get all the link tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

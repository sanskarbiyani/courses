import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter url : ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

sum = 0
tags = soup('span')
for tag in tags:
     number = int(tag.contents[0])
     sum += number

print(sum)

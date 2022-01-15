import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved',len(data), 'characters')
tree = ET.fromstring(data)
sum = 0

counts = tree.findall('.//count')
print('count:',len(counts) )
for count in counts:
    number = int(count.text)
    sum +=number
print('Sum:',sum)

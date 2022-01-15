import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

parms = dict()
serviceurl = "http://py4e-data.dr-chuck.net/json?"

address = input("Enter location: ")
if len(address) < 1: quit()

parms["address"] = address
parms["key"] = 42
url = serviceurl + urllib.parse.urlencode(parms)

print("Retreiving: ", url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print("Retreived", len(data), "characters")

try:
    js = json.loads(data)
except:
    js = None

if not js:
    print("Failed..Try again")
    quit()

#print(json.dumps(js, indent=3))
print("place_id: ", js["results"][0]["place_id"])

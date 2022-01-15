import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'
api_key = 42

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({"address" : address, "key" : api_key})
    print("Retreiving:", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retreived: ", len(url), "characters")

    try:
        info = json.loads(data)
    except:
        info = None

    if not info or 'status' not in info or info["status"]!="OK":
        print("====== RETREVAL FAILURE ======")
        print(data)
        continue

    print(json.dumps(info, indent=3))

    latitude = info["results"][0]['geometry']["location"]["lat"]
    longitude = info["results"][0]['geometry']["location"]["lng"]
    print("Latitude: ", latitude, "Longitude:", longitude)
    locality = info["results"][0]["formatted_address"]
    print(locality)

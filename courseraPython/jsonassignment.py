import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter location- ")
print("Retreiving", url)
if len(url) < 1:
    print("Error in opening url. Please check again")
    quit()

data = urllib.request.urlopen(url).read().decode()
print("Retreived", len(data), "characters")
jsInfo = json.loads(data)

#print(json.dumps(jsInfo, indent=3))

lst = jsInfo["comments"]
sum = 0

for i in range(len(lst)):
    sum += lst[i]["count"]

print("Count:", len(lst))
print("Sum:" , sum)

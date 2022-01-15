import json

# Input can be a list of dictionaries or dictionaries of dictionaries
input = '''[
    { "id" : "001",
      "x" : "2",
      "name" : "Sanskar"
    } ,
    {
      "id" : "002",
      "x" : "6",
      "name" : "Mamta"
    }
]'''

info = json.loads(input)
print("length:", len(info))
for item in info:
    print("Name:", item["name"])
    print("id:", item["id"])
    print("Attribute:", item["x"])
    print()

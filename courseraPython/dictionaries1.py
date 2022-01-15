counts = dict()
names = ['csev','cwen','csev','zqian','cwen','csev','csev']
for name in names:
    counts[name] = counts.get(name,0)+1

#loop goes through the keys not the values!!
for key in counts:
    print(key, counts[key])

print(list(counts))

print(counts.keys())

print(counts.values())

print(counts.items())

#to go through key value pair together
for key,value in counts.items():
    print(key,value)

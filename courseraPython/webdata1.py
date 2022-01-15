import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        count[word] = count.get(word,0) + 1

#print(count)
l = list()
print(sorted(count.items()))
print()
for k,v in sorted(count.items()):
    l.append( (v,k))

l = sorted(l,reverse=True)
print(l)

fname= input("Enter Filename: ")
try:
    fh = open(fname)
except:
    print("Enter correct Filename and Retry!! ")

words = list()
count = dict()

for line in fh:
    if line.startswith('From '):
        words = line.split()
        t = words[5].split(':')
        count[t[0]] = count.get(t[0],0) + 1

for k,v in sorted(count.items()):
    print(k,v)

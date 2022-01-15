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
        count[words[1]] = count.get(words[1],0) + 1

maxcount = None
maxname = None

for k,v in count.items():
    if maxcount is None or v>maxcount:
        maxcount = v
        maxname = k

print(maxname,maxcount)

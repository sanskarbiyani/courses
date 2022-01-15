fname = input("Enter file name : ")
fhandle = None
total = x = 0

try:
    fhandle = open(fname)
except:
    print("Incorrect File Name")
    quit()

for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    x+=1
    atpos = line.find(':')
    p = line[atpos+2: ]
    total += float(p)

avg = total/x
print("Average spam confidence:",avg)

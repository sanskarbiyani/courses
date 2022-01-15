fname = input("Enter file name")
fhandle = None

try:
    fhandle = open(fname)
except:
    print("Incorrect File Name")
    quit()

for line in fhandle:
    l = line.rstrip()
    print(l.upper())

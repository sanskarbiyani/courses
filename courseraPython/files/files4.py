fname= input("Enter Filename: ")

try:
    fh = open(fname)
except:
    print("Enter correct Filename and Retry!! ")

words = list()
count = 0
for line in fh:
    if line.startswith('From '):
        words = line.split()
        count +=1
        print(words[1])

print("There were", count, "lines in the file with From as the first word")

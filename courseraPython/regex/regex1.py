import re

name= input("Enter Filename: ")
try:
    fh = open(name)
except:
    print("Enter correct Filename and Retry!! ")
    quit()

sum = 0
for line in fh:
    t = list(map(int,re.findall('[0-9]+',line)))
    for number in t:
        sum += number

print(sum)

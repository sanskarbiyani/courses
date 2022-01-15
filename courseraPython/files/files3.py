fname= input("Enter Filename")

try:
    fh = open(fname)
except:
    print("Enter correct Filename and Retry")

words=list()
for line in fh:
    ls = line.split()
    for word in ls:
        if word not in words:
            words.append(word)

words.sort()
print(words)

fhandle = open("filename.txt", 'a')
fhandle.write("New Content added!\n")
fhandle.close()

fhandle = open("filename.txt")
for line in fhandle:
    print(line.strip())

fhandle.close()

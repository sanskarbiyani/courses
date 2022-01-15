N = int(input())
visi = [i+1 for i in range(N)]
perm = list(map(int, input().split()))
list = list()
while visi:
    word=''
    i = visi[0]
    while str(i) not in word:
        visi.remove(i)
        word += str(i)+' '
        i = perm[i-1]
    word += word[0]
    list.append(word)
print(len(list))
for i in list:
    print(i)

'''n=int(input())
a=[int(x) for x in input().split()]
arr,visited=[],[]
for i in range(n):
    if i+1 not in visited:
        l=[]
        while i+1 not in l:
            l.append(i+1)
            visited.append(i+1)
            i=a[i]-1
        l.append(i+1)
        arr.append(l)
print(len(arr))
for x in arr:
    print(*x)
'''

N,D = map(int, input().split())
L = list()
for _ in range(N):
    L.append(int(input()))
L.sort()
count = i = 0
while i<N-1:
    if L[i+1]-L[i] <= D:
        count +=1
        i +=1
    i+=1
print(count)

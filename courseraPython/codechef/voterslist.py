N1,N2,N3 = map(int,input().split())
n1 = list()
n2 = list()
n3 = list()
for i in range(N1):
    n1.append(int(input()))
for i in range(N2):
    n2.append(int(input()))
for i in range(N3):
    n3.append(int(input()))

a = set(n1)
b = set(n2)
c = set(n3)
int1 = a & b
int2 = b & c
int3 = c & a
uni1 = int1.union(int2)
lst = list(int3.union(uni1))
lst.sort()
print(len(lst))
for i in lst:
    print(i)

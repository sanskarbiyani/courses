'''c = 0

def prime(n):
    global c
    c+=1
    if n<12:
        if n<=4:
            return n-1
        elif n<= 7:
            if n == 6:
                return 5
            return n-2
        else:
            return 7
    else:
        for i in range(n-1, 1, -1):
            if i%2 !=0 and i%3!=0 and i%5!=0 and i%7!=0:
                return i

for _ in range(int(input())):
    N = int(input())
    if N<2:
        print('ALICE')
        continue
    while N>1:
        N = N-prime(N)
    if c%2==0:
        print('ALICE')
    else:
        print('BOB')
'''

for _ in range(int(input())):
    n=int(input())
    if n%4==1:
        print("ALICE")
    else:
        print("BOB")

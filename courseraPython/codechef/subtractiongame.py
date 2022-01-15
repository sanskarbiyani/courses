'''for _ in range(int(input())):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    while numbers[N-1]>numbers[0]:
        if all(x % numbers[0]==0 for x in numbers):
            break
        numbers[N-1] -= numbers[0]
        numbers.sort()
        print(numbers)
    print(numbers[0])'''

#USE GCD
from math import gcd
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    g=a[0]
    for i in a:
        g=gcd(g,i)
    print(g)

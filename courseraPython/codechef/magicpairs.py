for _ in range(int(input())):
    N = int(input())
    numbers = list(map(int, input().split()))
    c = N*(N-1)//2
    print(c)

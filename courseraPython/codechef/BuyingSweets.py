for _ in range(int(input())):
    N,X = map(int, input().split())
    A = list(map(int, input().split()))
    sum = sum(A)
    A.sort()
    if sum%X < A[0]:
        print(sum//X)
    else:
        print(-1)

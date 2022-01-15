for _ in range(int(input())):
    N,K = map(int,input().split())
    W = list(map(int,input().split()))
    W.sort()
    son = W[:K]
    chef = W[K:]
    print(abs(sum(chef)-sum(son)))

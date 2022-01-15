for _ in range(int(input())):
    X,Y,K,N = map(int,input().split())
    X -=Y
    c=0
    if X<0:
        X=0
    for _ in range(N):
        P,C = map(int,input().split())
        if c ==0:
            if P>=X and C<=K:
                c=1
    if c==1:
        print('LuckyChef')
    else:
        print('UnluckyChef')

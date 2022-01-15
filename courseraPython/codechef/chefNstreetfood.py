for _ in range(int(input())):
    maxprofit = 0
    for _ in range(int(input())):
        S,P,V = map(int,input().split())
        profit = (P//(S+1)) * V
        if profit>maxprofit:
            maxprofit = profit

    print(maxprofit)

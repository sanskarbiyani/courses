for _ in range(int(input())):
    N = int(input())
    S = list(map(int,input().split()))
    token = 0
    while len(S)>0:
        min = minindex =  None
        for i in range(len(S)):
            if min is None or min>S[i]:
                min = S[i]
                minindex = i
        token += min * len(S)
        S = [i-min for i in S[0:minindex]]
    print(token)

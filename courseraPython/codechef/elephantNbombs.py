for _ in range(int(input())):
    N = int(input())
    S = input()
    safe = N
    indexes = [i for i in range(N) if S[i]=='1']
    safe -= len(indexes)*3
    if len(indexes):
        if S[0] == '1':
            safe += 1
        if S[N-1] == '1':
            safe += 1
        for i in range(1, len(indexes)):
            if indexes[i]-indexes[i-1]==1:
                safe += 2
            elif indexes[i]-indexes[i-1]==2:
                safe += 1
        print(safe)
    else:
        print(N)

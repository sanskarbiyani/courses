for _ in range(int(input())):
    N = input()
    sum=list()
    for i in range(len(N)):
        str1 = N[:i]
        str2 = N[i+1:]
        sum.append(int(str1+str2))
    print(min(sum))

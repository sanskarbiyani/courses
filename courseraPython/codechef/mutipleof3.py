for _ in range(int(input())):
    K,d0,d1 = map(int,input().split())
    temp = d0 + d1
    num = d0*10 + d1
    x = K
    if K > 10:
        x = 10
    for i in range(2,x):
        num = num*10 + temp%10
        if num % 10 == 2:
            temp += ((K - i)//4) * 20
            if (K-i) % 4 == 1:
                temp += 2
            elif (K-i) % 4 == 2:
                temp += 6
            elif (K-i) % 4 == 3:
                temp += 14
            break
        temp += temp%10

    if temp%3 == 0:
        print('YES')
    else :
        print('NO')

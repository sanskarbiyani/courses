for _ in range(int(input())):
    L,R = map(int, input().split())
    l = L%10
    r = R%10
    if l!=0:
        L = L + (10 - l)
    R = R - r
    count = (R - L)//10 * 3
    if l != 0:
        for i in range(l,10):
            if i % 10 == 2 or i % 10 == 3 or i % 10 == 9:
                count+=1
    for i in range(1,r+1):
        if i % 10 == 2 or i % 10 == 3 or i % 10 == 9:
            count+=1
    print(count)

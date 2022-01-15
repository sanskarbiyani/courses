for _ in range(int(input())):
    N = int(input())
    people = list(map(int, input().split()))
    chef = c = 0
    for i in people:
        if i ==5:
            chef +=5
        elif i-5 <= chef:
            chef -= i-5
        else:
            c=1
            break
    if c==0:
        print('YES')
    else:
        print('NO')

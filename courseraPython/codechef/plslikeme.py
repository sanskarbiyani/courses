'''for _ in range(int(input())):
    L,D,S,C = map(int, input().split())
    l = S*(1+C)**(D-1)
    if l>=L:
        print('ALIVE AND KICKING')
    else:
        print('DEAD AND ROTTING')'''

for _ in range(int(input())):
    L,D,S,C=map(int,input().split())
    for i in range(d):
        if S>=L:
            print('ALIVE AND KICKING')
            break
        S=S*(c+1)
    else:
        print('DEAD AND ROTTING')

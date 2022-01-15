#mistake in the program......SOLVE IT!!!
'''for _ in range(int(input())):
    matches = int(input())
    score = input()
    s=len(score)
    teamA=teamB=0
    for i in range(matches):
        if score[i*2]==score[i*2+1]:
            continue
        elif int(score[i*2])>int(score[i*2+1]):
            teamA+=1
            s=i*2+2
        else:
            teamB+=1
            s=i*2+2

        if teamA>(matches//2):
            break
        elif teamB>(matches//2):
            break

    print(s)
'''
#CORRECT PROGRAM
for i in range(int(input())):
    N = int(input())
    score = list(map(int,input()))
    i = 0
    A=B=0
    turnsA=turnsB=N
    s = 2*N
    while(i<2*N):
        A+=score[i]
        turnsA-=1
        if(A+turnsA<B) or (B+turnsB<A):
            s = i+1
            break

        B+=score[i+1]
        turnsB-=1
        if(A+turnsA<B) or (B+turnsB<A):
            s = i+2
            break

        i+=2

    print(s)

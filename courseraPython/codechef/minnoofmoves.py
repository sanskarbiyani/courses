for _ in range(int(input())):
    N = int(input())
    sal = list(map(int,input().split()))
    steps = 0
    while True:
        sal.sort()
        if sal[0] == sal[N-1]:
            print('maximium number: ',max)
            print(steps)
            break
        steps +=1
        max = sal[N-1]
        sal = [i+1 for i in sal[:N-1]]
        sal.append(max)
        print(sal)

#Another Method to perform thhe solution

for _ in range(int(input())):
    N = int(input())
    sal = list(map(int,input().split()))
    steps = 0
    sal.sort()
    for i in range(1,N):
        steps += (sal[N-i] - sal[N-i-1]) * i
    print(steps)

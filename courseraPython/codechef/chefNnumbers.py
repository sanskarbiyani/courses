test= int(input())
for _ in range(test):
    N = int(input())
    numbers = list(map(int,input().split()))
    checked = []
    count=dish=0
    for i in range(N):
        c=0
        last_location = i
        if numbers[i] in checked:
            continue
        elif i == N-1:
            break
        else:
            checked.append(numbers[i])
            for j in range(N):
                if numbers[j] == numbers[i]:
                    if last_location != j-1:
                        c+=1
                        last_location = j

        if c>count:
            count=c
            dish=numbers[i]
    print(dish)
    print(count)

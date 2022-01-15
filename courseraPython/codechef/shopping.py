for _ in range(int(input())):
    N = int(input())
    prices = list(map(int, input().split()))
    prices.sort(reverse = True)
    sum = 0
    for i in range(0,N,4):
        try:
            sum += prices[i] + prices[i+1]
        except:
            sum += prices[i]
    print(sum)

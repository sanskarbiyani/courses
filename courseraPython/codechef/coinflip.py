for _ in range(int(input("Enter Test cases: "))):
    for _ in range(int(input("Enter Number Of games: "))):
        I,N,Q = map(int,input("Enter data: ").split())
        if N%2!=0:
            if I==Q:
                print(N//2)
            else:
                print((N//2)+1)
        else:
            print(N//2)

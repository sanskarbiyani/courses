for _ in range(int(input())):
    N,M = map(int,input().split())
    m = list(map(int,input().split()))
    m.sort()
    n = [i+1 for i in range(N)]
    for x in m:
        if x in n:
            n.remove(x)
    c = 1
    chef=assistant=''
    for i in n[::2]:
        chef=chef+str(i)+' '
    for i in n[1::2]:
        assistant= assistant+str(i)+' '
    print(chef)
    print(assistant)

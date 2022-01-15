for _ in range(int(input("Enter test cases"))):
    string = input("enter string")
    str1 = str2 = ''
    c=[]
    flag=1
    S = len(string)
    if S%2==0:
        str1 = string[ :S//2]
        str2 = string[S//2: ]
    else:
        str1 = string[ :S//2]
        str2 = string[(S//2)+1: ]
    for ch in str1:
        if ch in c:
            continue
        c.append(ch)
        if str1.count(ch)!=str2.count(ch):
            flag = 0
            break
    if flag:
        print("YES")
    else:
        print("NO")

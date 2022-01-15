'''for _ in range(int(input())):
    feedback = input()
    str=''
    c=False
    for i in range(2,len(feedback)):
        str = feedback[i-2] + feedback[i-1] + feedback[i]
        if str=='010' or str=='101':
            c = True
            break

    if c:
        print('Good')
    else:
        print('Bad')'''

#Another Method

for _ in range(int(input())):
    feedback = input()
    if '101' in feedback or '010' in feedback:
        print('Good')
    else:
        print('Bad')

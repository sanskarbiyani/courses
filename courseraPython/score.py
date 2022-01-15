score = 0.0

try:
    score = float(input("Enter Score : "))
except :
    quit("WARNING!! Please enter a number")

if score <=1.0 and score >=0.0:
    if score >= 0.9:
        print("A")
    elif score >=0.8:
        print("B")
    elif score >= 0.7:
        print("class")
    elif score >= 0.6:
        print("D")
    else :
        print("F")
else:
    print("WARING!! Please enter between 0.0 And 1.0")

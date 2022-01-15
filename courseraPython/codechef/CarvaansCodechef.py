#Codechef Problems: Carvans    Code: CARVANS
for _ in range(int(input("Enter Testcases"))):
    N= int(input("Enter number of cars"))
    maxspeeds = list(map(int,input("Enter max speeds of cars: ").split()))
    maxspeed= None
    cars = 0
    for speed in maxspeeds:
        if maxspeed is None or maxspeed > speed:
            maxspeed = speed
            cars+=1
    print(cars)

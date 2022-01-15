largest = None
smallest = None
num1 = None

while True:
    num1 = input("Enter Number : ")
    if num1 == 'done':
        break
    try:
        num1 = int(num1)
    except:
        print("Invalid Input")
        continue
    if smallest is None and largest is None:
        smallest=largest=num1
    elif smallest>num1:
        smallest=num1
    elif largest<num1:
        largest=num1

print("Maximium is",largest)
print("Minimium is",smallest)

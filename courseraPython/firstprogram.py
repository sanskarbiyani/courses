#To calculate hourly wages
hrs = 0.0
rate = 0.0
gross_pay = 0.0
try:
    hrs = float(input("Enter Number Of Hours"))
    rate = float(input("Enter rate "))
except:
    quit("WARNING!! Please enter a number")
if hrs <= 40 :
    gross_pay = hrs*rate;
else:
    extraHours = hrs - 40
    gross_pay = ((rate * 1.5) * extraHours) + (rate * 40)
print(gross_pay)

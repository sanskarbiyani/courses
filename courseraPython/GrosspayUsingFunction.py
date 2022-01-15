gross_pay=0.0
hrs = 0.0
rate = 0.0

def computepay(h, r):
    if h <= 40 :
        pay = h*r;
    else:
        extraHours = h - 40
        pay = ((r * 1.5) * extraHours) + (r * 40)
    return pay

try:
    hrs = float(input("Enter Number Of Hours : "))
    rate = float(input("Enter rate : "))
except:
    quit("WARNING!! Please enter a number")

gross_pay = computepay(hrs, rate)
print("Pay",gross_pay)

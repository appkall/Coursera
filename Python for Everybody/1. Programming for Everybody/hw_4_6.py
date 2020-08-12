#Assignment 4.6

def computepay(Hours,Rate):
    if Hours > 40:
        pay = 40 * Rate + (Hours - 40) * Rate * 1.5
    
    else:
        pay = Hours * Rate

    return pay

Hours = float(input("Enter Hours: "))
Rate = float(input("Enter Rate: "))

p = computepay(Hours,Rate)

print("Pay " +str(p))
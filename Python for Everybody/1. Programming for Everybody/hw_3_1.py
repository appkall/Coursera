#Assignment 3.1

hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

if hrs <= 40:
    pay = hrs * rate

if hrs > 40:
    pay = 40 * rate + (hrs - 40) * rate * 1.5

print (pay)
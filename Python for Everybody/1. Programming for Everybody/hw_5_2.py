#Assignment 5.2

Numbers = []

while True :
    sval = input('Enter a number: ')
    
    if sval == 'done' :
        break
    
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    
    Numbers.append(fval)

Minimum = int(min(Numbers))
Maximum = int(max(Numbers))

print('Maximum is', Maximum)
print('Minimum is', Minimum)
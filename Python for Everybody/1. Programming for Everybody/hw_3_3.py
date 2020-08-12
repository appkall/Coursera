#Assignment 3.3

score = float(input("Enter Score: "))

if score > 1.0:
    print('Please enter a number between 0.0 and 1.0!\n')
    
elif score >= 0.9:
    print('A')
    
elif score >= 0.8 and score < 0.9:
    print('B')

elif score >= 0.7 and score < 0.8:
    print('C')

elif score >= 0.6 and score < 0.7:
    print('D')

elif score < 0.6:
    print('F')
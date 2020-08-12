#Homework 8.5

#fname = 'mbox-short.txt'
fname = input('Enter file name: ')
fh = open(fname)

counter = []
email_addresses = []

for line in fh :
    if line.startswith('From ') :
    	words = line.split()
    	print(words[1])
    	email_addresses.append(words[1])
    	counter = len(email_addresses)

print('There were', counter, 'lines in the file with From as the first word')
#Homework: Regular Expressions

import re

fname = 'regex_sum_773856.txt'
#fname = 'regex_sum_42.txt'
#fname = input('Enter file name: ')
fh = open(fname)

numbers = list()
tot = 0

for line in fh :
	line = line.rstrip()

	numbers = re.findall('[0-9]+', line)
	
	for i in numbers :
		i = int(i)
		tot = tot + i

print(tot)

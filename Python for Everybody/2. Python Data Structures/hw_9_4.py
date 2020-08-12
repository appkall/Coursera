#Homework 9.4

fname = 'mbox-short.txt'
#fname = input('Enter file name: ')
fh = open(fname)

email_addresses = list()
counts = dict()

for line in fh :
	line = line.rstrip()

	if not line.startswith('From ') :
		continue

	words = line.split()
	email_addresses.append(words[1])
	
for names in email_addresses :
	
	if names not in counts :
		counts[names] = 1

	else :
		counts[names] = counts[names] + 1

for key,value in counts.items() :
	if max(counts.values()) == value :
		print(key, value)
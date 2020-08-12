#Homework 10.2

fname = 'mbox-short.txt'
#fname = input('Enter file name: ')
fh = open(fname)

time = list()
count = dict()

for line in fh :
	line = line.rstrip()

	if not line.startswith('From ') :
		continue

	words = line.split()
	time_1 = words[5]
	time_1 = time_1.split(':')
	time.append(time_1[0])
	
for entry in time :
			
	if entry not in count :
		count[entry] = 1

	else :
		count[entry] = count[entry] + 1

for (k, v) in sorted(count.items())	:
	print(k, v)
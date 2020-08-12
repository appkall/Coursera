#Homework 7.2

#fname = 'mbox-short.txt'
fname = input("Enter file name: ")
fh = open(fname)
counter = []

for line in fh :
    if line.startswith('X-DSPAM-Confidence: ') :
    	#print(line)
    	atpos = line.find('0')
    	sppos = line.find('\n')
    	extract = float(line[atpos:sppos])
    	#print(extract)
    	counter.append(extract)

#print(counter)
#average = sum(counter) / len(counter)

num = 0
for i in counter :
	num = num + i
	dem = len(counter)


average = num / dem
print('Average spam confidence:', average)
#Homework 8.4

#fname = 'romeo.txt'
fname = input('Enter file name: ')
fh = open(fname)

words = fh.read().split()
#print(words)
counter = []

for i in words :

	if i not in counter :
		counter.append(i)

	else :
		continue

counter.sort()
print(counter)
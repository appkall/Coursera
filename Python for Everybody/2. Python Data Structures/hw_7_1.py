#Homework 7.1

# Use words.txt as the file name
fname = input('Enter file name: ')
fh = open(fname)
inp = fh.read().rstrip()
print(inp.upper())
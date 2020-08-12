#Homework 6.5

text = "X-DSPAM-Confidence:    0.8475";
atpos = text.find('0')
sppos = text.find('5')
extract = text[atpos:sppos + 1]
extract = float(extract)
print(extract)
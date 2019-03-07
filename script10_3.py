'''Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. 
Your program should convert all the input to lower case and only count the letters a-z. Your program should 
not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several 
different languages and see how letter frequency varies between languages. Compare your results with the 
tables at https://wikipedia.org/wiki/Letter_frequencies.
'''
import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation)) 
    line = line.lower()
    words = line.split()
    for word in words:
        for ch in word:
            if ch in string.ascii_lowercase:
                if ch not in counts: 
                    counts[ch] = 1
                else:
                    counts[ch] += 1
l = list(counts.values())
sum1 = sum(l)
t = list(counts.items())
t.sort()
for key, value in t:
    print(key, round(value/sum1*100,3),'%')
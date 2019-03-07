'''Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses 
from the line. Count the number of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples
from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195 '''

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'): continue
    words = line.split()
    try:
        day = words[2]
        email = words[1]
        if email not in counts:
            counts[email] = 1
        else:
            counts[email] += 1
    except:
        pass

l = list()
for key, val in counts.items():
    l.append((val,key))
l.sort(reverse=True)
value1, key1 = l[0]
print(key1,value1)

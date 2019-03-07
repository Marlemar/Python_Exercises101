''' Exercise 2: Write a program that categorizes each mail message by which day of the week 
the commit was done. To do this look for lines that start with “From”, then look for the third 
word and keep a running count of each of the days of the week. At the end of the program print 
out the contents of your dictionary (order does not matter).

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
www.py4e.com/code3/mbox.txt
www.py4e.com/code3/mbox-short.txt
'''

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
        if day not in counts:
            counts[day] = 1
        else:
            counts[day] += 1
    except:
        pass
print(counts)
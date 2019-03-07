''' Exercise 4: Add code to the above program to figure out who has the most messages in the file. 
After all the data has been read and the dic- tionary has been created, look through the dictionary 
using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages 
and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
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
        email = words[1]
        if email not in counts:
            counts[email] = 1
        else:
            counts[email] += 1
    except:
        pass
largest_value = None
for key in counts:
    if largest_value is None or counts[key] > largest_value : 
        largest_value = counts[key]
        key_ID = key
print(key_ID, largest_value)
'''Exercise 5: This program records the domain name (instead of the address) where the message 
was sent from instead of who the mail came from (i.e., the whole email address). At the end of 
the program, print out the contents of your dictionary.
python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8} '''

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
        email = str(words[1])
        house = email[email.find('@')+1:]
        if house not in counts:
            counts[house] = 1
        else:
            counts[house] += 1
    except:
        pass
print(counts)
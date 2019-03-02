'''
Exercise 2: Write another program that prompts for a list of numbers as above 
and at the end prints out both the maximum and minimum of the numbers instead of the average.
'''

min=None
max=None
while True:  
    line = input('Enter a number: ')
    try:
        number = float(line)
        if min is None or number < min:
            min = number
        if max is None or number > max:
            max = number
    except:
        if line == 'done':
            break
        else:
            print('Invalid input')         
print(min,max)
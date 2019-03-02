'''Rewrite your pay program using try and except so that your program handles non-numeric 
input gracefully by printing a message and exiting the program. The following shows two 
executions of the program:
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input'''



inp1 = input('Enter Hours: ')
inp2 = input('Enter Rate: ')
try:
    inp1 = float(inp1)
    inp2 = float(inp2)
    pay = inp1*inp2
    print('Pay: ', str(pay))
except:
    print('Error, please enter numeric input')

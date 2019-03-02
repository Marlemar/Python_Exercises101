'''Exercise 6: Rewrite your pay computation with time-and-a-half for over- time and create a function called 
computepay which takes two parameters (hours and rate).
Enter Hours: 45
Enter Rate: 10
Pay: 475.0'''


def computepay(inp1,inp2):
    try:
        inp1 = float(inp1)
        inp2 = float(inp2)
        pay = inp1*inp2
        print('Pay: ', str(pay))
    except:
        print('Error, please enter numeric input')

inp1 = input('Enter Hours: ')
inp2 = input('Enter Rate: ')
computepay(inp1,inp2)

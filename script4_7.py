'''Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes 
a score as its parameter and returns a grade as a string.
 Score
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
<0.6 F
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Run the program repeatedly to test the various different values for input.'''

def computegrade(inp):
    try:
        inp1 = float(inp)
        if (inp1>= 0.9) & (inp1<=1.0):
            print('A')
        elif (inp1>=0.8) & (inp1<0.9):
                print('B')
        elif (inp1 >=0.7) & (inp1<0.8):
            print('C')
        elif (inp1>=0.6) & (inp1<0.7):
            print('D')
        elif (inp1>=0) & (inp1<0.6):
            print('F')
        else:
            print('Bad score')
    except:
        print('Bad score')
        
a = input('Enter score: ')
computegrade(a)

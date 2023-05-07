# Using elif with if, else statements.
# Using elif will make each statements depend upon each other like a ladder.
a=20

if (a<90):
    print("Less than 90") 
elif (a>10):
    print("Greater than 10")

elif (a>5):
    print("Greater than 5")

else:
    print("Lesser Than Every Number..")


# Using if__else statements without elif 
# Using if__else without elif will make each statements independent.

b=12
'''The below if_statement is a nested if_statement'''
if (b>10):                      
    print("Greater than 10") # Note:-'''In order to make the Condition2 print, Condition1 must be true in a nested if-statement'''
    if (b>5):                 
        print("Greater than 5")

if (b>20):
    print("Greater than 20")
           

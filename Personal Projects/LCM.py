# AUTHOR - HIMANK JESHWAR
# WRITTEN ON - 14/12/2021

'''
QUESTION :-
Write a program to find lcm of two numbers entered by the user'''

'''Least Common Multiple (LCM) is the smallest positive integer that
is the multiple of all the given numbers.'''

# FORMULA FOR LCM OF TWO Numbers = (a*b)/GCD
# In this program we will find the gcd first.
def hcf(n1,n2):
    if n2==0:
        return n1
    else:
        return hcf(n2,n1%n2)
        
# Now we will write the method for LCM
def lcm(n1,n2):
    return (n1*n2)/hcf(n2,n1%n2)

num1 = int(input("Enter first number = ")) 
num2 = int(input("Enter second number = "))
print(f"LCM of {num1} and {num2} = {lcm(num1,num2)}")  
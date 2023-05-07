# AUTHOR - HIMANK JESHWAR
# WRITTEN ON - 14/12/2021
'''
QUESTION :-
Write a program to find out gcd of two numbers by 
the user using recursion.'''

'''Greatest Common Divisor (GCD) or Highest Common Factor (HCF) is the 
largest integer that divides the number without a remainder.'''
# FORMULA TO FIND GCD OF TWO NO.s =  (a*b)/LCM

def gcd(n1,n2):
    if n2==0:
        return n1
    return gcd(n2,n1%n2)

num1 = int(input("Enter first number = "))
num2 = int(input("Enter second number = "))
print(f"GCD of {num1} and {num2} = {gcd(num1,num2)}")
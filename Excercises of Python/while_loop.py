# AUTHOR - HIMANK JESHWAR
# DATE -14/08/21

# Find the factorial of n using while loop

def factorial_of_a(n):
    a=1
    factorial=1    
    while a<=n:
        factorial=factorial*a
        a+=1  # Value of (a) increase until it is equal to (n)
    return factorial

numbers=int(input("Enter any Number = "))
print(f"Factorial of {numbers} = {factorial_of_a(numbers)}")

# =====================================================================================    

'''FORMULA that this program use :-
Suppose n=5

As a = 1 and factorial = 1 (Remember value of (a) will increase until it is 5 in this case)

# VALUE OF (factorial) IS ALWAYS GIVEN 1 AND ITS FIXED
So, it will be -  a(1)*factorial x a(2)*factorial x a(3)*factorial x a(4)*factorial x a(5)*factorial'''
# Answer = 120
# AUTHOR - HIMANK JESHWAR
# DATE - 14/08/21

# Find the factorial of n using for loop

def factorial_1(n):
    factorial=1  # factorial should be equal to 1 when defining it first before the loop.
    for number in range(n):
        factorial=factorial*(number+1) 
    print(f"Factorial of {n} = {factorial}")

num=int(input("Enter Number = "))
factorial_1(num)
'''========================================================================='''
# Formula here used :-

# if you want take the factorial of 4 then :-
# # The value of factorial = 1 (Always keep the value 1,like done in the program)
# # so n=5
# # So in the for loop the num will be in the range of (1,5)
# # therefore formula will be 1*1 x 1*2 x 1*3 x 1*4
# '''Answer = 24'''
'''========================================================================='''
# AUTHOR - HIMANK JESHWAR
# DATE - 14/08/21

# Recursion is a function which calls its self.
# You can you use it to directly use a mathematical formula

# Here, its the best way to find factorial
def factorial(r):
    if r==1 or r==0:
        return 1
    else:
        return r*factorial(r-1)

num=int(input("Enter any number = "))
print(f"Factorial of {num} = {factorial(num)}")

# Formula In Recursion works like this :-
# if you want to find the factorial of 6 then :-

# 6 X factorial(5)
# 6 X [5 X factorial(4)]  
#                     ====================================================
#                     = As we have written r*factorial(r-1) ,            =
#                     = the value of r decrease by 1 which is multiplied = 
#                     = with r that is (r*r-1). This continues until     =
#                     = factorial(r-1),the value of r-1 is equal to 1.   =
#                     ====================================================
# 6 X 5 X [4 X factorial(3)]
# 6 X 5 X 4 X [3 X factorial(2)]
# 6 X 5 X 4 X 3 [2 X factorial(1)]
# 6 X 5 X 4 X 3 X 2 X [1] 
'''Answer = 720'''
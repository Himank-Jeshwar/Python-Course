def factorial(f):
    if f==1 or f==0:
        return 1
    else:
        return f*factorial(f-1)
num=int(input("Enter Succeding Number = "))
print(f"Factorial of {num-1} is {factorial(num-1)}.") 
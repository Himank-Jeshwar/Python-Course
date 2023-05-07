a=input("Enter the Dividend = ")
b=input("Enter the divisor = ")
try:
    a=int(a)
    b=int(b)
    print(f"Answer of {a}/{b} = {a/b}")  
except ValueError as e:
    print(f">>> Invalid Value: string literal is given instead of integer")    
except ZeroDivisionError as e:
    print(f">>> ZeroDivisionError: division by zero")
print("Thanks for using the calculator!")    
try:
    a=int(input("Enter first number = "))
    b=int(input("Enter second number = "))
    ans=a/b
    print(ans)
except ValueError as v:
    print(f"ValueError : {v}")
except ZeroDivisionError as z:
    print(f"ZeroDivisionError : {z}")        

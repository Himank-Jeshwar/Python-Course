try:
    a=int(input("Enter the dividend = "))
    b=int(input("Enter the divisor = "))
    div=a/b
    print(f"Answer of {a}/{b} = {div}")
except ZeroDivisionError as z:
    print(f"Infinite")    
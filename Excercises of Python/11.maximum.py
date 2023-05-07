from functools import reduce
def greatest(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2    
num1 = int(input("Enter 5 numbers = \n1. "))
num2 = int(input("2. "))
num3 = int(input("3. "))
num4 = int(input("4. "))
num5 = int(input("5. "))
numbers = [num1,num2,num3,num4,num5]
maximum = reduce(greatest,numbers)
print (f"Greatest = {maximum}")
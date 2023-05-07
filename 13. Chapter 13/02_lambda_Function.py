name = lambda a:a+" Jeshwar"
x="AUTHOR : - Himank"
print(name(x))   

total=lambda i,q,x:i+q+x
a=20
b=12
c=10
print(f"Sum of {a},{b},{c} = {total(a,b,c)}") # Prints 42
square=lambda s:s**2
num=int(input("Enter the Number = "))
print(f"Square of {num} = {square(num)}")

cube= lambda c:c**3
print(f"Cube of {num} = {cube(num)}")

squareroot=lambda sqr:sqr**0.5
print(f"Square Root of {num} = {squareroot(num)} ")

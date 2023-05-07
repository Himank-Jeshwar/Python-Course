class Calculator:
    def square(self):
        print(f"Square of {self.num} = {self.num**2}") # ** act as exponent
    def cube(self):
        print(f"Cube of {self.num} = {self.num**3}") 
    def squareRoot(self):   
        print(f"Square root of {self.num} = {self.num**0.5}")
o=input("What do you want to find [Square ,Cube or Square root] = ")
o=o.lower()
number=Calculator() 
number.num=int(input("Enter Number = "))
if o=="square":
    number.square()  
elif o=="cube":
    number.cube()
elif o=="square root":
    number.squareRoot()        
else:
    print("No such Operation is supported for this calculator .")       
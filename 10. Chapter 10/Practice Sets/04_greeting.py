class Calculator:
    @staticmethod
    def greet():
        print("Hello User!")
    def square(self):
        print(f"Square of this number = {self.num*self.num}")
    def cube(self):
        print(f"Cube of this number = {self.num*self.num*self.num}") 
    def squareRoot(self):   
        print(f"Square root of the number = {self.num**0.5}")
number=Calculator() 
number.greet()
o=input("What do you want to find [Square ,Cube or Square root] = ")
o=o.lower()
number.num=int(input("Enter Number = "))
if o=="square":
    number.square()  
elif o=="cube":
    number.cube()
elif o=="square root":
    number.squareRoot()           
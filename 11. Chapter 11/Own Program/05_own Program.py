class Number:
    def __init__(self,num1):
        self.num1=num1
    def __add__(self,num2):
        print("Adding..")
        return (f"Answer => {self.num1+num2.num1}\n")
    def __sub__(self,num2):
        print("Subtracting...")
        return (f"Answer => {self.num1-num2.num1}\n")
    def __mul__(self,num2):
        print("Multiplying....")
        return (f"Answer => {self.num1*num2.num1}\n")
    def __floordiv__(self,num2):
        print(f"Dividing...{self.num1} by {num2.num1}")
        return (f"Answer => {self.num1//num2.num1}") 
num1=Number(18)
num2=Number(2)
print(num1//num2)  
print(num1+num2)
print(num1*num2)
print(num1-num2)         
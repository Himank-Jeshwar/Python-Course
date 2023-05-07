class Addition:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def __add__(self):
        return(self.num1+self.num2)    
    def __str__(self):
        return(f"{self.num1} + {self.num2} = {self.num1+self.num2}")

class Substraction:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def __sub__(self):
        return(self.num1-self.num2)    
    def __str__(self):
        return(f"{self.num1} - {self.num2} = {self.num1-self.num2}") 

class Multiplication:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def __mul__(self):
        return(self.num1*self.num2)    
    def __str__(self):
        return(f"{self.num1} X {self.num2} = {self.num1*self.num2}")

class Division:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def __truediv__(self):
        return(self.num1/self.num2)    
    def __str__(self):
        return(f"{self.num1} / {self.num2} = {self.num1/self.num2}")

if __name__=="__main__": 
    add=Addition(23,20) 
    print(add) # 23 + 20 = 43
    sub=Substraction(23,20)
    print(sub) # 23 - 20 = 3
    mul=Multiplication(23,20)
    print(mul) # 23 X 20 = 460
    div=Division(400,20)
    print(div) # 400 / 20 = 20.0
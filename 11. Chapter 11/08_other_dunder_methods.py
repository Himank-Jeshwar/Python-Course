class Number:
    def __init__(self,num):
        self.num=num
    def __add__(self,num2):
        print(f"Addition :=") 
        return self.num + num2.num
    def __mul__(self,num2):    
        print(f"Multiplication :=")
        return self.num*num2.num
    def __sub__(self,num2):
        print(f"Substraction :=")
        return self.num-num2.num 
    def __str__(self):
        return(f"Decimal Number = {self.num}") 
    def __len__(self):
        return 1          
n= Number(6)
print(n)        
print(f"Length of n is {len(n)}")
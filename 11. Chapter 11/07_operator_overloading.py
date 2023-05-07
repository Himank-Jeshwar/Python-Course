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
n1=Number(30)
n2=Number(6)       
totalsum=n1+n2 
mul=n1*n2 
sub=n1-n2
print(totalsum)
print(mul) 
print(sub)
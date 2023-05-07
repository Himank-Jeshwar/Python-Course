#1 (a*ai)-(b*bi)
#2 (a*b+b*a)
class Complex:
    def __init__(self,realNo,imagNo):
        self.realNo=realNo
        self.imagNo=imagNo
    def __add__(self,com):
        return Complex(self.realNo+com.realNo,self.imagNo+com.imagNo)
   
    def __mul__(self,com):
        mulReal=self.realNo*com.realNo-self.imagNo*com.imagNo
        mulImagNo=self.realNo*com.imagNo+self.imagNo*com.realNo
        return Complex(mulReal,mulImagNo)
    
    def __str__(self):
        return (f"{self.realNo} + {self.imagNo}i")    
c1=Complex(3,2)            
c2=Complex(1,7)
print(c1+c2)
print(c1*c2)
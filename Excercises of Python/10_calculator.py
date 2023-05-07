# AUTHOR - HIMANK JESHWAR
# DATE - 10/08/21

# This just a normal calculator for beginners. Its a just a initiate.
# This calculator takes 15 numbers for Addition,Substraction & Multiplication.
# It can add,divide,substract and multiply.
# It can be improved! 

# YOU ARE FREE TO IMPROVE AND CUSTOMIZE THIS CALCULATOR

print("WELCOME QUICK Z CALCULATOR !")
print("YOU CAN ADD,MULTIPLY,DIVIDE,SUBSTRACT UPTO 2 NUMBERS")
class Calculator:
    def __init__(self,num):
        self.num=num
    def total(self,num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12,num13,num14,num15):
        return (f"{self.num} + {num2.num} + {num3.num} + {num4.num} + {num5.num} + {num6.num} + {num7.num} + {num8.num} + {num9.num} + {num10.num} + {num11.num} + {num12.num} + {num13.num} + {num14.num} + {num15.num} = {self.num+(num2).num+(num3).num+(num4).num+(num5).num+(num6).num+(num7).num+(num8).num+(num9).num+(num10).num+(num11).num+(num12).num+(num13).num+(num14).num+(num15).num}")
    def mul(self,num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12,num13,num14,num15):
        return (f"{self.num} * {num2.num} * {num3.num} * {num4.num} * {num5.num} * {num6.num} * {num7.num} * {num8.num} * {num9.num} * {num10.num} * {num11.num} * {num12.num} * {num13.num} * {num14.num} * {num15.num} = {self.num*num2.num*num3.num*num4.num*num5.num*num6.num*num7.num*num8.um*num9.num*num10.num*num11.num*num12.num*num13.num*num14.num*num15.num}") 
    def div(self,num2):
        return (f"{self.num} / {num2.num} = {self.num/num2.num}")
    def subt(self,num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12,num13,num14,num15):
        return (f"{self.num} - {num2.num} - {num3.num} - {num4.num} - {num5.num} - {num6.num} - {num7.num} - {num8.num} - {num9.num} - {num10.num} - {num11.num} - {num12.num} - {num13.num} - {num14.num} - {num15.num} = {self.num-num2.num-num3.num-num4.num-num5.num-num6.num-num7.num-num8.um-num9.num-num10.num-num11.num-num12.num-num13.num-num14.num-num15.num}")
operation=input("Which Operation would you like to do (choose the operand) (+),(-),(/),(*) = ")                
if operation=="+" or operation=="-" or operation=="*":
    num1=int(input("Enter 1st Number = "))
    num2=int(input("Enter the 2nd Number = "))
    num3=int(input("Enter 3rd Number = "))
    num4=int(input("Enter 4th Fourth Number = "))
    num5=int(input("Enter 5th Fourth Number = "))
    num6=int(input("Enter 6th Fourth Number = "))
    num7=int(input("Enter 7th Fourth Number = "))
    num8=int(input("Enter 8th Fourth Number = "))
    num9=int(input("Enter 9th Fourth Number = "))
    num10=int(input("Enter 10th Fourth Number = "))
    num11=int(input("Enter 11h Fourth Number = "))
    num12=int(input("Enter 12th Fourth Number = "))
    num13=int(input("Enter 13th Fourth Number = "))
    num14=int(input("Enter 14th Fourth Number = "))
    num15=int(input("Enter 15th Fourth Number = "))
if operation=="+":
      
    num1=Calculator(num1)
    num2=Calculator(num2)
    num3=Calculator(num3)
    num4=Calculator(num4)
    num5=Calculator(num5)
    num6=Calculator(num6)
    num7=Calculator(num7)
    num8=Calculator(num8)
    num9=Calculator(num9)
    num10=Calculator(num10)
    num11=Calculator(num11)
    num12=Calculator(num12)
    num13=Calculator(num13)
    num14=Calculator(num14)
    num15=Calculator(num15)      

    if num2=="":
        print(num1.total(num2)) 
        exit()
    elif (num3)=="":
        print(num1.total(num2,num3))
        exit()
    elif (num4)=="":
        print(num1.total(num2,num3,num4))
        exit()
    elif (num5)=="":
        print(num1.total(num2,num3,num4,num5))
        exit()
    elif (num6)=="":
        print(num1.total(num2,num3,num4,num5,num6)) 
        exit()  
    elif (num7)=="":
        print(num1.total(num2,num3,num4,num5,num6,num7))
        exit()
    elif (num8)=="":
        print(num1.total(num2,num3,num4,num5,num6,num7,num8))
        exit()   
    elif (num9)=="":
        print(num1.total(num2,num3,num4,num5,num6,num7,num8,num9))
        exit()
    elif (num10)=="":
        print(num1.total(num2,num3,num4,num5,num6,num7,num8,num9,num10))
        exit()
    elif (num11)=="":
        print(num1.total(num2,num3,num4,num5,num6,num7,num8,num9,num10,num11))
        exit()
    elif (num12)=="":
        print(num1.total(num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12))
        exit()
    elif (num13)=="":
        print(num1.total(num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12,num13))
        exit()
    elif (num14)=="":
        print(num1.total(num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12,num13,num14))
        exit()   
    elif (num15)=="":
        print(num1.total(num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12,num13,num14,num15))
        exit()                    
elif operation=="-":
    num1=Calculator(num1)
    num2=Calculator(num2)
    num3=Calculator(num3)
    num4=Calculator(num4)
    num5=Calculator(num5)
    num6=Calculator(num6)
    num7=Calculator(num7)
    num8=Calculator(num8)
    num9=Calculator(num9)
    num10=Calculator(num10)
    num11=Calculator(num11)
    num12=Calculator(num12)
    num13=Calculator(num13)
    num14=Calculator(num14)
    num15=Calculator(num15)
    print(num1.subt(num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12,num13,num14,num15))
elif operation=="*":
    num1=Calculator(num1)
    num2=Calculator(num2)
    num3=Calculator(num3)
    num4=Calculator(num4)
    num5=Calculator(num5)
    num6=Calculator(num6)
    num7=Calculator(num7)
    num8=Calculator(num8)
    num9=Calculator(num9)
    num10=Calculator(num10)
    num11=Calculator(num11)
    num12=Calculator(num12)
    num13=Calculator(num13)
    num14=Calculator(num14)
    num15=Calculator(num15)
    print(num1.mul(num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12,num13,num14,num15))
elif operation=="/":
    dividend=int(input("Enter Dividend = "))
    divisor=int(input("Enter Divisor = ")) 
    num1=Calculator(dividend)
    num2=Calculator(divisor)
    print(num1.div(num2))
else:
    print("INVALID OPERAND ! Please Try Again.")    

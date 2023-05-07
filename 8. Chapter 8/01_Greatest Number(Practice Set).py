def greatest(numA,numB,numC):
    if numA>numB:
        if numA>numC:
            return numA
        else:
            return numC  
    if numC>numB:
        return numC
    else:
        return numB

num1=int(input("Enter three numbers:= \n1."))
num2=int(input("2."))
num3=int(input("3."))
print(greatest(num1,num2,num3),"is the greatest number.")
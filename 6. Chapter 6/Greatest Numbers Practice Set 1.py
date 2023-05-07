num1=int(input("Enter 4 Numbers:-\n1."))
num2=int(input("2."))
num3=int(input("3."))
num4=int(input("4."))

if(num1>num4):
    c=num1

else:
    c=num4 

if (num2>num3):
    d=num2 

else:
    d=num3

if(c>d):
    print(str(c),"is greatest")
else:
    print(str(d),"is greatest")            
def printing1():
    return "You have won the lottery !"

def printing2():
    return "Better Luck Next Time!"        
    
q=int(input("Enter Number Between 1 and 10 :-\n"))
if  q==5 or q==7:
    print(printing1())
else:
    print(printing2()) 

def divide(m):
    return m/2
u=int(input("Enter Number = "))
a=divide(u)
print(a)
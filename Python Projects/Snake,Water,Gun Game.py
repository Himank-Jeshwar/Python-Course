import random

print("Computer's Turn:- Snake,Water or Gun ?")
me=input("\nYour Turn:- Snake(press s),Water,(press w) or Gun(press g) = ")
select=random.randint(1,3)

if select==1:
    comp="s"
elif select==2:
    comp="w"
elif select==3:
    comp="g"

def winner(comp,me):            
    if comp=="s":
        if me=="w":
            return False 
        elif me=="g":
            return True      
    elif comp=="w":
        if me=="g":
            return False 
        elif me=="s":
            return True 
    elif comp=="g":
        if me=="s":
            return False 
        elif me=="w":
            return True 
    elif comp==me:
        return None  

win=winner(comp,me) 
if win==False:
    print("YOU LOSE!") 
elif win==True:
    print("YOU WIN!")
else:
    print("OMG !! This is a Tie.")        

if comp=="s":
    comp="Snake"
if comp=="w":
    comp="Water"
if comp=="g":
    comp="Gun"

if me=="s":
    me="Snake"
if me=="w":
    me="Water"
if me=="g":
    me="Gun"
print("\nCOMPUTER Choice ==>> Computer has chosen",comp) 
print("USER'S Choice ==>> You have chosed",me,"\n")  
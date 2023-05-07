# Stone|Paper|Scissor with Computer Game
# RULES:-
''' 1) If suppose,player1 has stone and player2 has paper:=
PLAYER2 wins! or vice versa'''

'''2)If suppose player1 has scissor and player2 has paper
PLAYER1 wins! or vice versa'''

'''3)If suppose player1 has scissor and player2 has stone
PLAYER2 wins! or vice-versa'''

import random
choice=random.randint(1,3)
print("COMPUTER's TURN Done...")
my=input("\nYOUR TURN => Stone[press (s)],paper [press (p)] or scissor [(press (c)] => ")
if choice==1:
    comp="s"
elif choice==2:
    comp="p"
elif choice==3:
    comp="c"

def winner(comp,my):
    if comp=="p":
        if my=="s":
            return False
        elif my=="c":
            return True
    elif comp=="c":
        if my=="p":
            return False
        elif my=="s":
            return True
    elif comp=="s":
        if my=="c":
            return False
        elif my=="p":
            return True      
    elif comp==my:
        return None                         
    

finalwinner=winner(comp,my)

if finalwinner==True:
    print("YOU WIN!")
elif finalwinner==False:
    print("YOU LOSE")    
else:
    print("TIE!")     

if comp=="s":
    comp="Stone"
elif comp=="p":
    comp="Paper"
elif comp=="c":
    comp="Scissor" 

if my=="s":
    my="Stone"
elif my=="p":
    my=="Paper"
elif my=="c":
    my="Scissor"
    
print("Computer has chosen "+ comp) 
print("You have chosen "+ my)   
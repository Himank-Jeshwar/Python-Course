def game():
    return 50
score=game()
with open("Hiscore.txt") as g:
    last_highscore=g.read()    

if last_highscore=="":
    with open("Hiscore.txt","w") as g:
        g.write(str(score))
    
elif int(last_highscore)<score: 
    with open("Hiscore.txt","w") as g:
        f1=g.write(str(score))

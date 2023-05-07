import random
number=random.randint(1,100)
user=int(input("Guess the number = "))
guesses=0
while user!=number:
    if user>number:
        print("Lower number please.")
    elif user<number:
        print("Higher number please.") 
    user=int(input("Guess the number = "))
    guesses=guesses+1

if user==number:
    print("\nIts a Perfect guess!")    
print(f"Number of Guesses Used = {guesses}")  

with open("hiscore.txt","w") as f:
    f.write("20")
with open("hiscore.txt") as f:
    last_score=int(f.read())
with open("hiscore.txt","w") as f:
    if guesses<last_score:
        f.write(str(guesses))         
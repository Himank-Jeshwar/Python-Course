with open("donkey.txt") as w:
    censoring=w.read()
censoring=censoring.replace("donkey","@@@@@@") 
with open("donkey.txt","w") as w:
    censoring=w.write(censoring)   
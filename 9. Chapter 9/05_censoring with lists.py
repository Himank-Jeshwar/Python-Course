slang_list=["idiot","fool","donkey","stupid","duffer"]
with open ("donkey.txt") as sl:
    censor=sl.read()    
for slangs in slang_list:
    censor=censor.replace(slangs,"******")
with open("donkey.txt","w") as sl:
    censor=sl.write(censor) 
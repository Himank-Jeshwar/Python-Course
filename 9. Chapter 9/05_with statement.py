# Context Mode
with open("Para2.txt","r") as p:
    d=p.read()
print(d) 

with open("Para2.txt","a") as p:
    d=p.write("\n\nHimank is a good coder")
print(d) 
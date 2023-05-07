with open("poems.txt") as p:
    file1=p.read()
with open("copy of poems.txt","w") as p:
    p.write(file1)
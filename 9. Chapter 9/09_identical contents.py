with open ("poems.txt") as a:
    f1=a.read()
with open ("copy of poems.txt") as a:
    f2=a.read()
if f1==f2:
    print("The two files are identical ")
else:
    print("The two files are not identical .")    
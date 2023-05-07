poem=open("poems.txt","r")
if "Twinkle" in poem.read():
    print ("This poem contains the word 'twinkle' ")
else:
    print ("This poem does not contain the word 'twinkle' ")    
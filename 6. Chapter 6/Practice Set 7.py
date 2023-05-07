# Harry in variants= HarrY, HARRY , harry , HArry , HaRRY 
# Must not be case-sensitive and detects in any form.
# Harry Is A Good Boy => harry is a good boy. (By uisng .lower())
post=input("Write Something Below :-\n")
post=post.lower()
if "harry" in post:
    print("This post talks about 'Harry' ")
else:
    print("This post does not talks about 'Harry'")    
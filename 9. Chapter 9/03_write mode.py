j=open("Para2.txt","w") # Write mode will replace all the contents
                        #Para2.txt never existed but this function added it.
g=j.write("CSS is a good programming language!")
g=j.write("\nHTML is a good programming language!") # Will add all these contents
g=j.write("\nC++ is a good programming language!")
print(g)
j.close() 
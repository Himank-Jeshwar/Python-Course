# Use open () function to read the content of the file
f=open("Para.txt") # By default the mode is "read mode"
de=f.read(13) 

'''Specifying 12 in the argument will read only first 12 
characters of the file'''

de=f.read()

'''If you write this function again, not all characters will be printed,
as already 13 characters are mentioned so it will directly skip it
and continue from the next line onwards'''

print(de)
f.close() 
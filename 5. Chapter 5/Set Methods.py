# Set Methods
# c.add()
c=set()
c.add(9)
c.add(8)
c.add("Himank")
c.add("Siddharth") 
c.add((10,9,8)) # Hence,Can add tuples, but not lists and dictionaries!
print(c) 

print(len(c)) #Prints the length of this set
c.remove("Siddharth")
c.remove(8)  #Removes the specified number from the set
print(c) 

print(c.pop()) 
print(c.clear()) 
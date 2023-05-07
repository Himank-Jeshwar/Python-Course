# List.sort()
L1=[20,10,34,45,46,60,22,13,9,230] 
L1.sort() 
print(L1)   

# List.reverse()
L2=[90,20,30,21,23,43,40,44,12] 
L2.reverse() 
print(L2) 

# List.append() (adds at the end of the list)  
'''MOST IMPORTANT METHOD IN LIST'''

L3=["Rohan","Divya","Rohit",]
L3.append("Himank") #Can append one at a time
L3.append("Sam") 
print(L3) 

# List.insert()
L3.insert(0,"Harry") # inserts "Harry" in index 0
print(L3) 

# List.pop() 
''' Pop is basically used for removing elements 
                    in the specified index(Index number required)'''
L3.pop(1)  #Rohan will be removed first
L3.pop(1)  
'''Divya will be shifted from index 2 to index 1 and now 
for removing Divya you have to type L3.pop(1) from the next line'''
print(L3)

# List.remove()
'''Remove is used for removing elements in a list. Basically removes
        the element by only specifying the element and 
                                not the index number'''
L3.remove("Sam")
print(L3) 

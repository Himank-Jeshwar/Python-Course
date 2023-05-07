# Dictionary Methods
dicA={
    "Python":"Easy to learn programming language",
    "Java":"Used for making apps",
    "HTML":"Used for making and building websites",
    "Scratch":"Programming tool for kids"
}

# <variable>.keys()
print(list(dicA.keys()))

# <variable>.values()
print(list(dicA.values()))

# <variable>.items()
print(list(dicA.items())) #'''Writing list is not so important''')
                          #Prints keys and values in the form of tuples.

# <variable>.update()
dicB={
    "CSS":"Used for web designing",
    "KaliLinux":"Used by mostly hackers",
    "Scratch":"Drag and drop coding" 
}
 
dicA.update(dicB)  #'''Updates the dictionary by adding (key-value) 
                                                # pairs from dicB'''
print(dicA)

# <variable>.get()
print(dicA.get("Python")) #Prints value associated with Python

'''What is the difference between .get and [] syntax in Dictionaries?'''
# print(dicA.get('Phython')) #Returns "None" as Phython is not present
# print(dicA['Phython']) # Returns an "error message" as Phython is not present
                                                                 
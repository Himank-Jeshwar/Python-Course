a=54 # Global Variable
def func1():
    global a
    print(a) #Prints 54
    a=90 # Local Variable if global keyword not used
func1()
print(a)# prints 90
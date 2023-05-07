def greet(name):
    print("Good Evening, "+name)  

# if __name__== "m06_greet":
'''if the above is written then the next two lines will be printed in the 
other file if it is module'''   
if __name__ == "__main__":    
    n=input("Enter Your Name = ") 
    greet(n)   
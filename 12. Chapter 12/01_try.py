while(True):
    print("Press e to exit")
    a=input(">> Enter a number = ")
    if a=='e':
        break
    try:
        print("Trying...")
        a=int(a)
        if a>6:
            print("You entered the number which is greater than 6.")  
    except Exception as y:
        print(f"Only integer acceptable and not string !")         
print("Thanks for Playing!")        
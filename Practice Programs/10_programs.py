def fileRead(filename):
    try:
        with open(filename) as b:
            content=b.read()
            print(content)
    except FileNotFoundError:
        print(f"{filename} does not exist in this directory !")     
fileRead("1.txt") 
fileRead("2.txt")
fileRead("3.txt")              
def readFile(filename):
    try:
        with open(filename) as a:
            print(a.read())      
    except FileNotFoundError:
        print(f"{filename} is not present in this directory")
readFile("1.txt")
readFile("2.txt")
readFile("3.txt")                    
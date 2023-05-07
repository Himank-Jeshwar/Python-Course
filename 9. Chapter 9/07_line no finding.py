find=True
n=1
with open("log.txt") as f:
    while find:
        find=f.readline()
        if "python" in find:
            print(f"The log file contains 'python' in line no. {n}") 
        n+=1
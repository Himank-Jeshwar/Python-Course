with open("log.txt") as f:
   find=f.read().lower()
if "python" in find:
    print("The log file contains 'python' ") 
else:
    print("The log file does not contain 'python' ")      
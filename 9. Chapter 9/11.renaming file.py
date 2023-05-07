import os
with open("renamed_by_python.py") as r:
    old=r.read()
with open("renamed_by_python.txt","w") as r:
    new=r.write(old)    

os.remove("renamed_by_python.py")    
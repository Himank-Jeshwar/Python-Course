import os
import time
while True:
    os.chdir(f"{os.getcwd()}\\Test")
    keyword = "game"  

    for files in os.listdir():
        if keyword in files:
            f = open(files,"rb")
            os.chdir("..")
            os.chdir(f"{os.getcwd()}\\Test 2")
            destDir=os.getcwd()
            newFile = open(files,"wb")
            for lines in f:
                newFile.write(lines)
            f.close()
            os.chdir("..")
            os.chdir(f"{os.getcwd()}\\Test")
            time.sleep(1)
            os.remove(files)
            print(f"\"{files}\" sent to \"{destDir}\" ")
            
    os.chdir("..")
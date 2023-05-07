import os
dict1 = {
    "oldfiles":["Gta v game.jpg","Gta vice city game.jpg"],
    "newfiles":["image.jpg","new.jpg"]
}
os.chdir(f"{os.getcwd()}\\Test")
oldFiles = dict1["oldfiles"]
newFiles = dict1["newfiles"]
for i in range (0,len(oldFiles)):
    f = open(oldFiles[i],"rb") 
    newFile = open(newFiles[i],"wb")
    for lines in f:
       newFile.write(lines)
    f.close()

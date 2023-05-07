import os
import time

print("\nWelcome to fileMaker, Here you can not only make files but also you can delete,\nopen and even display the contents of the directory.\n\n  Software Made by - Himank Jeshwar")
def open(name):
    print("\n\t\t\t       Opening The File ...")
    time.sleep(2)
    os.startfile(f"{os.getcwd}\\{name}")
    print("\t\t\t       File Opened Successfully.")    

def create(name):
    print("\n\t\t\t       Creating The File ...")
    time.sleep(2)
    with open (name,"w") as file:
        file.write("")
    print("\t\t\t       File Created Successfully.")

def delete(name):
    print("\n\t\t\t       Deleting The File ...")
    time.sleep(2)    
    os.remove(name) 
    print("\t\t\t       File Deleted Successfully.")

def displayContents():
    files = os.listdir()
    print("\n\t\t\t       FILES PRESENT IN THIS DIRECTORY ARE :- \n")
    for items in files:
        print(f"\t\t\t       {items}")
if __name__=="__main__":
    while True :
        print("\n")
        print(f"\n\t\t\t       Current Path :- {os.getcwd()}")
        print("\n")
        print('''                            ========================================================
                                =   Press 1 to create a file                           = 
                                =   Press 2 to delete a file                           =
                                =   Press 3 to open a file                             =
                                =   Press 4 to print the contents of this directory    =
                                =   Press 5 to exit                                    = 
                                ========================================================''')                                 
        choice = int(input("\n\t\t\t       Enter Choice : "))
        print("\n")
        
        
        if choice == 1:
                CreatefileName = input("\n\t\t\t       Enter the file name to create (DO NOT ENTER THE FILE EXTENSION) = ")
                CreatefileType = input("\t\t\t       Enter the file extension to create = ")
                CreatefinalFile = CreatefileName+CreatefileType
                create(CreatefinalFile)     
        
        elif choice == 2:
            try:
                fileNameDelete = input("\n\t\t\t       Enter the file name to delete (DO NOT ENTER THE FILE EXTENSION) = ")
                fileTypeDelete = input("\t\t\t       Enter the file extension to delete = ")
                finalFileDelete = fileNameDelete+fileTypeDelete
                if finalFileDelete == "fileMaker.py":
                    print("\n\t\t\t       This File Cannot Be Deleted !")
                else:
                    delete(finalFileDelete)
            except FileNotFoundError:
                    print(f"\n\t\t\t       The File '{finalFileDelete}' does not exist.")    
        elif choice == 3:
            try:
                openFilename = input("\n\t\t\t       Enter the file name to open (DO NOT ENTER THE FILE EXTENSION) = ")
                openFileType = input("\t\t\t       Enter the file extension to open = ")
                openFile = openFilename+openFileType
                open(openFile)

            except FileNotFoundError :
                print(f"\n\t\t\t       The File '{openFile}' does not exist in this directory !")
        elif choice == 4:
            displayContents()
        elif choice == 5:
            exit()      
        else:
            print("\n\t\t\t       Invalid Input !")
print("\n\t                                               ================== NATIONAL LIBRARY ==================")
# Work From Library's Side ..
class Library:
    def __init__(self,bookList):
        self.bookList=bookList

    def showBookList(self):
        print("Books Available In Our Library :- \n")
        for indexNo,oneBook in enumerate(self.bookList,start=1):
            print(f"   {indexNo}. {oneBook} ")

    def giveBooks(self,oneBook):
        if oneBook == " "or oneBook == "":
            print("\n\t\t\t\t\t\tFIELDS CANNOT HAVE SPACES OR BLANKS !")
        else:    
            if oneBook in self.bookList:
                self.bookList.remove(oneBook) 
                print(f'''\n   \t\t\t\t\t\t\t\t******************************************************************************************* \n  \t\t\t\t\t\t\t\t\t\t The book '{oneBook}' is issued to you. Enjoy Reading !                 \n  \t\t\t\t\t\t\t\t\t\t Date of returning :- 16/08/2021                                                  \n  \t\t\t\t\t\t\t\t\t\t Please return on time or a fine of 100/- will be charged.                        \n  \t\t\t\t\t\t\t\t*******************************************************************************************''')
            else:
                print(f"The book '{oneBook}' is not available in our library at this moment.")
    def getBackBooks(self,oneBook):
        if oneBook == "" or oneBook ==" ":
            print("\n\t\t\t\t\t\tFIELDS CANNOT HAVE SPACES OR BLANKS !")
        else:    
            self.bookList.append(oneBook)
            print('''   \n   \t\t\t\t\t\t\t\t**********************************************\n   \t\t\t\t\t\t\t\t*  Given on :- 13/08/2021                    *\n   \t\t\t\t\t\t\t\t*  Thanks For Giving Us the Book.            *\n   \t\t\t\t\t\t\t\t*\t\tHave Nice Day !               *
   \t\t\t\t\t\t\t\t**********************************************                       ''') 

# Work from Student's Side....
class Student:
    def requestBook(self):
        nameOfBooks=input("\t\t\t\t\t\t Enter The Book Name to borrow = ")    
        return nameOfBooks
        
    def returnBook(self):
        nameOfBooks=input("\t\t\t\t\t\t Enter The Book Name to return/donate = ")   
        return nameOfBooks              
nationalLibrary=Library(["Harry Potter","Concise Chemistry","Understanding Mathematics","The 80/20 Principle Book","Quantum Physics","Arabian Nights","Huckleberry Finn","Tom Sawyer","Up For Air","Pride and Prejudice"])
students=Student()

# We Make A Menu Driven System Here For the user to perform any task 

while True:
    print('''
    \t\t\t\t\t\t\t\t =========================================
    \t\t\t\t\t\t\t\t = Press A to See the Book List          = 
    \t\t\t\t\t\t\t\t = Press B to Request a Book             =
    \t\t\t\t\t\t\t\t = Press C to Donate/Return a Book       = 
    \t\t\t\t\t\t\t\t = Press D to exit                       =
    \t\t\t\t\t\t\t\t ========================================= ''')
    action=input("\n\t\t\t\t\t\t Enter Your Choice = ")
    action=action.upper()

    # Assigning Buttons For Choices

    if action=="A":
        nationalLibrary.showBookList()
    elif action=="B":
        nationalLibrary.giveBooks(students.requestBook())
    elif action=="C":
        nationalLibrary.getBackBooks(students.returnBook())
    elif action=="D":
        print("\n\t\t\t\t\t\t\t\tThanks For Visiting Our Library.\n\t\t\t\t\t\t\t\tHope You Enjoyed !")
        exit()
    elif action == "":
        print("\t\t\t\t\t\t\t\tFIELDS CANNOT HAVE BLANKS !")
    elif " " in action :
        print("\t\t\t\t\t\t\t\tFIELDS CANNOT HAVE SPACES !")  
    else:
        print("(A),(B),(C),(D) is acceptable !!!\n  Try Again !")      
    
# REMARKS :-
# requestBook and returnBook only takes the name of the book to request or return that book.
# giveBooks removes the name of the book given in requestBook ,from the bookList.
# getBackBooks appends the name of the book given in returnBook , to the bookList.
class School:
    def __init__(self,name,_class,subject):
        self.name=name
        self._class=_class
        self.subject=subject
        if subject=="Science":
            print("\nSTUDENT ADDED!!\n")
        else:
            print("\nSTUDENT NOT ADDED!\n")    
    def confirmAdmission(self):
        print(f"Name = {self.name}")
        print(f"Class = {self._class}") 
        print(f"Subject = {self.subject}")
name=input("Enter Name = ")
_class=int(input("Enter Your Class = "))
subject=input("Enter Your Subject Stream = ") 
worker=School(name,_class,subject) 
worker.confirmAdmission()       
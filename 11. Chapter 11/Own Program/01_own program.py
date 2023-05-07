class Rajesh:
    country="India"
    def getStatus(self):
        print(f"This man lives in {self.country}")    
class Employee(Rajesh):
    company="Microsoft"
    def getStatus(self):
        super().getStatus()
        print(f"I am an Employee")
class Programmer(Employee):
    def getStatus(self):
        super().getStatus()
        print("Life of a programmer is C++") 
r=Rajesh()
emp=Employee()
prog=Programmer()
prog.getStatus()
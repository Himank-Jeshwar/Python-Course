# Base Class
class Employee:
    company="Google"
    def getStatus(self):
        print(f"This employee works in {self.company} .")
# Child Class        
class Programmer(Employee):
    salary=78000
    def getSalary(self):
        print(f"Salary of employee is {self.salary}.")
    def getStatus(self):
        print(f"This employee does not works in {self.company} .")    

emp=Employee()
prog=Programmer()
prog.getStatus()
emp.getStatus()

'''Employee.company="Microsoft"'''
 # Changes will be seen in both Classes as it is the base class

Programmer.company="Youtube"# Changes will be seen in the child class
print(prog.company) 
print(emp.company)
'''As there is no company attribute so it will print from the parent 
class which is Employee''' 
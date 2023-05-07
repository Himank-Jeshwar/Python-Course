class Employee:
    company="Microsoft"
    def getSalary(self):
        print(f"Your Salary will be {self.salary} for working in {self.company}")
himank=Employee()
himank.salary=140000
himank.getSalary() # This means => Employee.getSalary(himank)        
# Here "self" is "himank"
# Also works for instance attributes

class Employee:
    company="Microsoft"
    salary=45000
    def getSalary(self):
        print(f"Your Salary will be {self.salary} for working in {self.company}")
himank=Employee()
himank.getSalary()
# Also works with class attributes..
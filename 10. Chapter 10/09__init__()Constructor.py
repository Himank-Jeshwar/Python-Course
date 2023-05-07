class Employee:
    company="Microsoft"
    
    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee added!")
    def getDetails(self):
        print(f"Name of Employee = {self.name}")    
        print(f"Name of Salary = {self.salary}")
        print(f"Name of Subunit = {self.subunit}")
    @staticmethod
    def greet():
        print(f"Good Morning Sir,")
    @staticmethod
    def time():
        print("Sent at 7 a.m")    
    def getSalary(self,sign):
        print(f"Your Salary will be {self.salary} for working in {self.company}.\n{sign}")

himank=Employee("Himank Jeshwar",90000,"Google")        
himank.getDetails()

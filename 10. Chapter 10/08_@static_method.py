class Employee:
    company="Microsoft"
    salary=45000
    @staticmethod
    def greet():
        print(f"Good Morning Sir,")
    @staticmethod
    def time():
        print("Sent at 7 a.m")    
    def getSalary(self,sign):
        print(f"Your Salary will be {self.salary} for working in {self.company}.\n{sign}")
himank=Employee()
himank.salary=70000
himank.greet()
himank.getSalary("- Himank Jeshwar")
himank.time()
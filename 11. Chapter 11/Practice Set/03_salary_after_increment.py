class Employee:
    salary=3000
    increment=500
    @property
    def salaryAfterIncrement(self):
        return self.salary+self.increment
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,totsal):
        self.total=totsal
        self.increment=self.total-self.salary
emp=Employee()
emp.salaryAfterIncrement=4500
print(f"Salary After Increment = {emp.salaryAfterIncrement}")
print(f"Salary = {emp.salary}")
print(f"Increment = {emp.increment}") 
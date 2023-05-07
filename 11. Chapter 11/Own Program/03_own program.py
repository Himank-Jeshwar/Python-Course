class Worker:
    salary=4500
    bonus=500
    @property
    def totalSalary(self):
        return self.salary+self.bonus
    @totalSalary.setter
    def totalSalary(self,totsal):
        self.totalsalary=totsal
        self.bonus=self.totalSalary-self.salary
wo=Worker()
wo.totalSalary=4500
print(f"Total Salary = {wo.totalSalary}") 
print(f"Salary = {wo.salary}")
print(f"Bonus = {wo.bonus}") 
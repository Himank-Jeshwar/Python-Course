class Worker:
    company="Hershey's"
    salary=60000
    bonusSalary=450
    @property
    def totalSalary(self):
        return self.salary+self.bonusSalary
    @totalSalary.setter
    def totalSalary(self,totalSal):
        self.bonusSalary=totalSal-self.salary
        
w=Worker()
w.totalSalary=145670
print(f"Total Salary = {w.totalSalary}")
print(f"Salary = {w.salary}")
print(f"Bonus = {w.bonusSalary}")
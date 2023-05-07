class Worker:
    company="Microsoft"
    eCode=120
class Freelancer:
    company="Fiverr" 
    level=0
    def upGradelevel(self):
        self.level=self.level+1
class Coder(Worker,Freelancer):
    name="Himank"

c=Coder()
c.upGradelevel()
print(c.level)
print(c.company) 
''' As "Worker" is written first in the child class argument so 
company will be printed from "Worker" because Worker is then given 
the first priority and its attributes and property will be printed 
 first if the variables are both same in "Worker" and "Freelancer" ''' 
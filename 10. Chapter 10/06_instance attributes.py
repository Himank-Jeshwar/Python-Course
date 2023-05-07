# INSTANCE ATTRIBUTES
class Worker:
    company="Youtube"
Himank=Worker()
Siddharth=Worker()
Himank.salary=65000
Siddharth.salary=50000
Worker.company="Microsoft" 
print(f"Himank works in {Himank.company}")
print(f"Siddharth works in {Siddharth.company}")
print(f"Salary of Himank = {Himank.salary}")
print(f"Salary of Siddharth = {Siddharth.salary}")

'''Will print Siddharth's and Himank's salary differently as we have 
mentioned the salary as instance attributes'''

class Worker:
    company="Youtube"
    salary=34000
Himank=Worker()
Siddharth=Worker()
Himank.salary= 65000
Siddharth.salary= 70000
Worker.company="Microsoft" 
print(f"Himank works in {Himank.company}")
print(f"Siddharth works in {Siddharth.company}")
print(f"Salary of Himank = {Himank.salary}")
print(f"Salary of Siddharth = {Siddharth.salary}")

# You can say object as instance
'''IMPORTANT:=
If salary is defined as a class attribute, the program will first
check for the instance attribute that is :=
Instance attribute is given the first priority than class attributes.If instance attribute is also defined than the program will print that
otherwise it will print the attribute which is defined in class
IF CLASS ATTRIBUTE IS ALSO NOT THERE IT WILL SHOW AN ERROR !'''
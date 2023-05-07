class Employee:
    company="ABC coding"
    salary=10000
    location="Kolkata"
    @classmethod
    def changeCompany(cls,cmp):
        # self.__class__.company=cmp #Using the dunder method
        cls.company=cmp
e=Employee()
print(e.location)        
e.changeCompany("Blogger")
print(e.company) # Created an instance attribute
print(Employee.company) # With changed class using class method
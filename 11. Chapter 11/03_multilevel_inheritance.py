class Human:
    country="America"
    def takeBreath(self):
        print("I am breathing...")
class Student(Human):
    school="St.Joseph College" 
    def getBooks(self):
        print(f"I study in {self.school}.")
    def takeBreath(self):
        print("I am a student but I have no time to even breathe...")
    
class Coder(Student):
    company="Blogger"
    def getMoney(self):
        print("Money is here!")
h=Human() 
st=Student()
co=Coder()
h.takeBreath()
st.takeBreath()
co.takeBreath() # Implements from Student as it is latest
print(co.company)
print(co.country)
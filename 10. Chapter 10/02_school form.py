class SchoolForm:
    form="School Admission Form" 
    def printinfo(self):
        print(f"Name = {self.name}")
        print(f"Class = {self.whichClass}")
        print(f"Age = {self.age}")
student_form=SchoolForm()
student_form.name=input("Enter Your Name = ") 
student_form.whichClass=input("Which Class You Study Now = ")
student_form.age=input("What is your age = ")
student_form.printinfo()
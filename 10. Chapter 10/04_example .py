class Admission:
    form="Teacher Admission Form" 
    def admission_final(self):
        print(f"Name = {self.name}")
        print(f"Phone Number = {self.Phno}")
        print(f"E-mail Id = {self.email}") 
        print(f"Address = {self.address}") 
        print(f"Education = {self.edu}")
        print(f"School Studied= {self.school}")  
admission_form=Admission()
admission_form.name=input("Enter Your Name = ")         
admission_form.Phno=input("Enter Your Phone Number = ")      
admission_form.email=input("Enter Your E-mail = ")   
admission_form.address=input("Enter Your Address = ")   
admission_form.edu=input("Enter Your Education = ")   
admission_form.school=input("Enter Your School Name = ")  
print("\n")
admission_form.admission_final()  

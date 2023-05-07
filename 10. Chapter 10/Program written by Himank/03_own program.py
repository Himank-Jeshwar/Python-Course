class Info:
    name="<name>"
    _class="<class>"
    roll="<roll>" 
    section="<section>"
    age="<age>"
    subject_stream="<subject stream>"
    def template(self):
        print(f"\nName = {self.name}")
        print(f"Class = {self._class}")
        print(f"Section = {self.section}")
        print(f"Roll Number = {self.roll}")
        print(f"Subject Stream = {self.subject_stream}")
        print(f"Age = {self.age}")  
student=Info()
print("FIll OUT THE GIVEN FORM USING THE TEMPLATE BELOW:= ")
Info.template(student)
student.name=input("\nEnter Your Name = ")
student._class=input("Enter Your Class = ")
student.section=input("Enter Your Section = ")
student.roll=input("Enter Your Roll No. = ")
student.subject_stream=input("Enter Your Subject_stream = ")
student.age=input("Enter Your Age = ")
student.template()         
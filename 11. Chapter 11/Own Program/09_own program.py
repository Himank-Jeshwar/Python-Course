class Humans:
    legs=2
    hands=2
    def __init__(self):
        print(f"My name is Himank ")
    def no_Hands(self):
        print(f"Humans Have {self.hands} hands")
class Students(Humans):
    school="St.Joseph's College"
    name="Himank Jeshwar"
    def my_Name(self):
        print(f"My Name is {self.name}")
    def __init__(self):
        super().__init__()
        print(f"I study in {self.school}")
class Programmers(Students):
    def __init__(self,language):
        self.lang=language
        super().__init__()
        print(f"I like {self.lang}") 
prog=Programmers("Python")        
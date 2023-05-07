class Humans:
    legs=2
    hands=2
    def no_Hands(self):
        print(f"Humans Have {self.hands} hands")
class Students(Humans):
    school="St.Joseph's College"
    name="Himank Jeshwar"
    def my_Name(self):
        print(f"My Name is {self.name}")
    def name_school(self):
        super().no_Hands()
        print(f"I study in {self.school}")
class Programmers(Students):
    lang="Python"
    def name_lang(self):
        super().name_school()
        print(f"I like {self.lang}") 
prog=Programmers()
prog.name_lang()                       
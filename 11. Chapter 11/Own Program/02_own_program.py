class Person1:
    def __init__(self):
        super().__init__()
        print("First I am a person")
class Human(Person1):
    country="United States of America"
    def __init__(self):
        super().__init__()
        print(f"My name is Himank")
class Student(Human):
    school="St.Jospeh's College"
    def __init__(self):
        super().__init__()
        print("He likes coding")   
class Programmer(Student):
    lang="Python"
    def __init__(self):
        super().__init__()
        print(f"This code written in Python by programmer.") 
prog=Human()                  
class Text:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return (f"My Name is {self.name}")
t=Text("Himank")
print(t)            
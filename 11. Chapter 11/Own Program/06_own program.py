class Text:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return (f"My Name is {self.name}")
    def __len__ (self):
           return 1 
t=Text("Himank")      
print(t)  
print(f"The length of t is = {len(t)}")
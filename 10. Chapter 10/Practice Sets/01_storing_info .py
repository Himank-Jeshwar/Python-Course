class Programmer:
    company="Microsoft"   
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def getInfo(self):
        print(f"Name = {self.name}")
        print(f"Company = {self.company}")
        print(f"Product = {self.product}")    
siddharth=Programmer("Siddharth Som","Microsoft Teams")
himank=Programmer("Himank Jeshwar","Microsoft Office 2019")
shaurya=Programmer("Shaurya Jaiswal","Blogger")
siddharth.getInfo()
print("\n")
himank.getInfo()
print("\n")
shaurya.getInfo()
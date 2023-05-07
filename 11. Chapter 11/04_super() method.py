class Ritesh:
    def __init__(self):
        print("Intializing Ritesh...\n")
    # def text(self):
    #     print("I am parent of Himank")
class Himank(Ritesh):
    def __init__(self):
        super().__init__()
        print("Intializing Himank...\n")
    # def text(self):
    #     print("I am parent of Himank2") 
class Himank2(Himank):
    def __init__(self):
        super().__init__()
        print("Intializing Himank2 ....")
    # def text(self):
    #     print("I am Himank2") 

# ri=Ritesh()
# hi=Himank()
hi2=Himank2()
# print("\n")
# hi2.text()
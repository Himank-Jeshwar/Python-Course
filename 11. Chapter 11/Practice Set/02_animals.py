class Animals:
    leg=4
class Pets(Animals):
    food="meat"
class Dogs(Pets):
    @staticmethod
    def barkDog():
        print("Bhow! Bhow Bhow...")   
a=Dogs()
a.barkDog()        
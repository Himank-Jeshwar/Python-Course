class Teacher:
    country="India"
    @classmethod
    def changeCountry(self,country):
        self.country=country
te=Teacher()
te.changeCountry("Switzerland")
# print(te.country)
print(Teacher.country)
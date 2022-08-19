class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def description(self):
        self.name = "ram"
        print( {self.name})

class Boy(Human): #pass human class as argument
     def __init__(self):
         print("child init")

     def schoolName(self, schoolname):
        print(f"I study in {schoolname}")


b = Boy("rahul", 20, "male")
b.description()
#b.schoolName("SDVP")

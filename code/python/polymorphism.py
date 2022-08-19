#polymorphism method overloading
class Shape:
    def no_of_sides(self):
        pass

    def two_dimensional(self):
        print("I am a 2D object")
class Square(Shape):
    def no_of_sides(self):
        print("I have 4 sides")

class Triangle(Shape):
    def no_of_sides(self):
        print("I have 3 sides")

sq = Square()
sq.no_of_sides()
tr = Triangle()
tr.no_of_sides()

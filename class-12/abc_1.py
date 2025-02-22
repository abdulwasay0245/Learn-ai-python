from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area():
        print("pass")

# shape_1 = Shape()
# shape_1.area()

class Circle(Shape):

    name: str = "Circle"
    radius : int

    def __init__(self,radius) :
        self.radius = radius  
    def area(self):
        print(3.14 * self.radius ** 2)



circle_1 = Circle(2)

circle_1.area()
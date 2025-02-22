from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area():
        print("pass")

# shape_1 = Shape()
# shape_1.area()

class Rectangle(Shape):

    name: str = "Rectangle"
    W : int
    L : int
    

    def __init__(self,W,L) :
        self.W = W
        self.L = L
    def area(self):
        print(f"Area = {self.W * self.L}")



circle_1 = Rectangle(2 , 4)

circle_1.area()
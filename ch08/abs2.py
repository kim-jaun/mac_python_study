from abc import *
class Shape(metaclass=ABCMeta):
    @abstractclassmethod
    def draw(self):
        pass

class Triangle(Shape):
    def draw(self):
        print("삼각형을 그린다")
class Rectangle(Shape):
    def draw(self):
        print("사각형을 그린다")
class Circle(Shape):
    def draw(self):
        print("원형을 그린다")

sh = [Triangle(), Rectangle(), Circle()]
for s in sh:
    s.draw()
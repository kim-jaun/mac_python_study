class Shape:
    def prt(self):
        pass

class Triangle(Shape):
    def prt(self):
        print("삼각형을 출력한다")

class Circle(Shape):
    def prt(self):
        print("원형을 출력한다")

class Rectangle(Shape):
    def prt(self):
        print("사각형을 출력한다")

x1 = [Triangle(), Circle(), Rectangle()]
for x in x1:
    x.prt()
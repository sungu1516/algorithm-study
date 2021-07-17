class Shape:
    def area(self):
        return 0

class Squre(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

squre =Squre(3)
print("정사각형의 면적: {0}".format(squre.area()))
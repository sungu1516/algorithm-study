class Rectangle:
    def __init__(self, hor, ver):
        self.hor = hor
        self.ver = ver

    def get_area(self):
        return self.hor * self.ver

rectangle = Rectangle(4, 5)
print("사각형의 면적: {0}".format(rectangle.get_area()))
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return (self.radius ** 2) * 3.14

circle = Circle(2)
print("원의 면적: {0}".format(circle.get_area()))
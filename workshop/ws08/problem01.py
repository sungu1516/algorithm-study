# 도형 만들기
# 해당 내용을 읽고, 클래스를 활용하여 점과 사각형을 표현

# Point class 정의
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Rectangle class 정의
class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def get_area(self):
        return abs(self.p1.x - self.p2.x) * abs(self.p1.y - self.p2.y)

    def get_perimeter(self):
        return 2 * (abs(self.p1.x - self.p2.x) + abs(self.p1.y - self.p2.y))

    def is_square(self):
        return abs(self.p1.x - self.p2.x) == abs(self.p1.y - self.p2.y)


# 결과 확인
p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())
p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())


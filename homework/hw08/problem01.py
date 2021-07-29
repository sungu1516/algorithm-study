# Circle 인스턴스 만들기

# 클래스 정의
class Circle:
    pi = 3.14
    x = 0
    y = 0
    r = 0

    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

    def area(self):
        return self.pi * self.r * self.r

    def circumference(self):
        return 2 * self.pi * self.r

    def center(self):
        return (self.x, self.y)

# 인스턴스 생성
circle1 = Circle(3, 2, 4)
# 생성된 인스턴스를 사용하여 원의 넓이와 둘레 출력
print(f'원의 넓이 : {circle1.area()}')
print(f'원의 둘레 : {circle1.circumference()}')
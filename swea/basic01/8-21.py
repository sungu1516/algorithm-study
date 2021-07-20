# _*_ coding: utf-8 _*_

# 반지름이 5인 원의 면적과 둘레의 길이를 구하는 함수를 정의해보아라.

# 반지름 변수
PI = 3.14

# 함수 정의
def input_radius():
    radius_str = input("반지름을 입력하세요: ")
    return float(radius_str)

def calc_circle_area(r):
    return r ** 2 * PI

def clac_circumference(r):
    return r * 2 * PI

# 변수에 값 저장
radius = input_radius()
circle_area = calc_circle_area(radius)
clac_circumference = clac_circumference(radius)

print("원의 면적:{0:.2f}, 원의 둘레: {1:.2f}".format(circle_area, clac_circumference))
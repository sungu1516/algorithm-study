## 1. 예외 처리 방법

#### 1) if문을 이용한 예외 처리 - 정상적인 흐름을 제어할 경우에만 사용 가능 (예외발생상황을 사전에 제어하는 방식)

#### 예외 발생 시 해별방법

#### 2) try ~ except문
print("사각형의 면적을 구해봅시다.")

width = input("폭을 입력하세요: ")
height = input("높이를 입력하세요: ")
area = 0

try:
    area = int(width) * int(height)
    print("{0} * {1} = {2}".format(width, height, area))
except:
    print("숫자가 아닌 값이 입력되었습니다.")
    print("{0} * {1} = {2}".format(width, height, area))

print("프로그램을 종료합니다.")

#### 3) try ~ except ~ else문 - 예외가 발생하지 않는 경우도 추가
print("사각형의 면적을 구해봅시다.")

width = input("폭을 입력하세요: ")
height = input("높이를 입력하세요: ")
area = 0

try:
    area = int(width) * int(height)
except:
    print("숫자가 아닌 값이 입력되었습니다.")
else:
    print("{0} * {1} = {2}".format(width, height, area))

print("프로그램을 종료합니다.")


#### 4) try ~ except ~ else ~ finally문 - 예외 발생 여부와 상관 없이 실행
print("사각형의 면적을 구해봅시다.")

width = input("폭을 입력하세요: ")
height = input("높이를 입력하세요: ")
area = 0

try:
    area = int(width) * int(height)
except:
    print("숫자가 아닌 값이 입력되었습니다.")
else:
    print("{0} * {1} = {2}".format(width, height, area))
finally:
    print("finally 코드 블록은 예외 발생 여부에 상관없이 실행됩니다.")

print("프로그램을 종료합니다.")
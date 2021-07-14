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

## 2. 예외 객체
#### 1) 예외 객체 참조
print("사각형의 면적을 구해봅시다.")

width = input("폭을 입력하세요: ")
height = input("높이를 입력하세요: ")
area = 0

try:
    area = int(width) * int(height)
except Exception as ex:
    print("{0}: {1}}".format(type(ex), ex))
else:
    print("{0} * {1} = {2}".format(width, height, area))
finally:
    print("finally 코드 블록은 예외 발생 여부에 상관없이 실행됩니다.")

print("프로그램을 종료합니다.")

#### 2) 다중 except문
print("나누기 연산의 결과를 구해봅시다.")

x, y, result = 0, 0, 0

try:
    x = int(input("피제수를 입력하세요: "))
    y = int(input("제수를 입력하세요: "))
    result = x / y
except ValueError as ve:
    print("입력 값은 반드시 숫자를 사용해야 합니다.")
    print("{0}: {1}".format(type(ve), ve))
except ZeroDivisionError as ze:
    print("제수로 0을 사용할 수 없습니다.")
    print("{0}: {1}".format(type(ze), ze))
else:
    print("{0} * {1} = {2}".format(width, height, area))
finally:
    print("finally 코드 블록은 예외 발생 여부에 상관없이 실행됩니다.")

print("프로그램을 종료합니다.")

## 3. 강제 예외 발생
def calc_area(w, h):
    if w.isdigit() and h.isdigit():
        return int(w) * int(h)
    else:
        raise ValueError("숫자가 아닌 갑이 입력되었습니다.")

print("사각형의 면적을 구해봅시다.")

width = input("폭을 입력하세요: ")
height = input("높이를 입력하세요: ")

try:
    area = calc_area(width, height)
except ValueError as ve:
    print("{0}: {1}".format(type(ve), ve))
except Exception as ex:
    print("{0}: {1}".format(type(ex), ex))
else:
    print("{0} * {1} = {2}".format(width, height, area))
finally:
    print("finally 코드 블록은 예외 발생 여부에 상관없이 실행됩니다.")

print("프로그램을 종료합니다.")

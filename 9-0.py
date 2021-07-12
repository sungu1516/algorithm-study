#파이썬 기본 내장함수

## 1. 수치 연산 함수

print(divmod(9, 5))
print(pow(2, 3))

## 2. 시퀀스형/반복 가능한 자료형을 다루는 함수

#### 1) any, all
val = [True, True, True]
print("all({0}) => {1}".format(val, all(val)))

val2 = [True, False, True]
print("any({0}) => {1}".format(val, any(val)))

#### 2) enumerate
data_list = [10, 20, 30, 40, 50]

for idx, val in enumerate(data_list):
    print("data_list[{0}]: {1}".format(idx, val))

for obj in enumerate(data_list):
    print(obj)

#### 3) filter
def iseven(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ret_val = filter(iseven, numbers)
# 아래와 같이 람다식도 이용 가능
ret_val2 = filter(lambda x: x % 2 == 0, numbers)

print("{0}".format(list(ret_val)))
print("{0}".format(list(ret_val2)))

#### 4) list(), tuple(), set(), dict()
data_str = "SSAFY"

data_list = list(data_str)
data_tuple = tuple(data_str)
data_set = set(data_tuple)
data_dict = dict(enumerate(data_set))

print("list({0}) => {1}".format(data_str, data_list))
print("tuple({0}) => {1}".format(data_str, data_tuple))
print("set({0}) => {1}".format(data_tuple, data_set))
print("dict({0}) => {1}".format(data_set, data_dict))

#### 5) map()
data_list = list("abcdef")

result = list(map(lambda x: x.upper(), data_list))

print("list(map(lambda x: x.upper(), {0})) => {1}".format(data_list, result))

#### 5) range() - 시퀀스형 객체를 생성하는 함수
data_list1 = list(range(1, 11))

#### 6) sorted()
data_list = [3, 8, 12, 2, 5, 11]

asc_result = sorted(data_list)
desc_result = list(reversed(asc_result))

print("오름차순 정렬 : {}".format(asc_result))
print("내림차순 정렬 : {}".format(desc_result))

#### 7) zip()

data_list1 = [1, 2, 3]
data_list2 = [4, 5, 6]
data_list3 = ["a", "b", "c"]

print("list(zip({}, {}, {})) => {}".format(data_list1, data_list2, data_list3, list(zip(data_list1, data_list2, data_list3))))
print("dict(zip({}, {})) => {}".format(data_list3, data_list1, dict(zip(data_list3, data_list1))))

#-----------------------------------------------------------------------------------------------------

## 3. 변환함수

#### 1) char()
val = 65
val2 = 0xac00
print("char({}) => '{}'".format(val, chr(val)))
print("char({0:x}) => '{1}'".format(val2, chr(val2)))

#### 2) ord()
val = "A"
val2 = "가"
print("ord({0}) => '{1}'".format(val, ord(val)))
print("ord({0}) => '{1}'".format(val2, hex(ord((val2)))))

#### 3) hex()

#### 4) int(), float(), str()
x = "10"
y = "3C"
z= 4.5

print("2진수 표현인 문자열 '{0}'은 10진수 {1}로 변환됩니다.".format(x, int(x, 2)))
print("16진수 표현인 문자열 '{0}'은 10진수 {1}로 변환됩니다.".format(y, int(y, 16)))


#---------------------------------------------------------------------------

## 4. 객체 조사를 위한 함수
#### 1) dir()
print("dir() => {0}".format(dir()))
data_str = "Hello, Python!"
print("dir(data_str) => {0}".format(dir(data_str)))

data_list = [10, 20, 30, 40, 50]
print("dir(data_list) => {0}".format(dir(data_list)))

#### 2) globals()
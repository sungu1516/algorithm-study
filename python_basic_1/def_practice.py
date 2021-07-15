# 매개변수와 반환 값이 있는 함수
def calc_sum(x, y):
    return x + y

# 매개변수는 없고, 반환 값이 있는 함수
def func_noparameters_return():
    return "Hello, Python!"

# 매개변수는 있고 반환 값이 없는 함수
def func_parameters_noreturn(x, y, z):
    print("반환값이 없는 함수입니다.")

# 매개변수도 없고 반환 값도 없는 함수
def func_noparameter_noreturn():
    print("매개변수와 반환값이 없는 함수입니다.")


#---------------------------------------------

# 언팩 연산자(*) - 가변형 매개변수의 사용(하나만 지정 가능하고, 가장 마지막 매개변수로 지정해야 함)
def calc_sum(*parms):
    total = 0
    for val in parms:
        total += val
    return total

# 명시적 매개변수와 가변 매개변수의 혼합사용
def calc_sum(precision, *params):
    if precision == 0:
        total = 0
    elif 0 < precision < 1:
        total = 0.0

    for val in params:
        total += val
    return val

# 언팩 연산자(*) - 하나 이상의 값을 리턴하는 함수의 경우
def calc_sum(precision1, precision2, *params):
    if precision1 == 0:
        total1 = 0
    elif 0 < precision2 < 1:
        total1 = 0.0

    if precision2 == 0:
        total2 = 0
    elif 0 < precision2 < 1:
        total2 = 0.0

    for val in params:
        total1 += val
        total2 += val

    return total1, total2

# 키워드 언팩 연산자(*) - 매개변수를 딕셔너리 형식으로 처리함
def use_keyword_arg_unpacking(**params):
    for k in params.keys():
        print("{0}: {1}".format(k, params[k]))

use_keyword_arg_unpacking(a = 1, b = 2, c = 3)


# 기본 값을 갖는 매개변수 - 이 경우의 매개변수는 일반 매개변수 앞에 존재할 수 없음!!
def calc(x, y, operator="+"):
    if operator == "+":
        return x + y
    else:
        return x - y

# 변수 접근 순서 - 함수 내 변수를 먼저 찾는다.
a = 1
def scope():
    a = 2
    print(a)

scope()

# 변수 접근 순서 - 만약 전역변수에 접근하고 싶다면? global 사용
def change_global_var():
    global x
    x += 1
    print(x)

x = 5

change_global_var()

#고급함수---------------------------------------------------------

# 중첩함수
def calc(operator_fn, x, y):
    return operator_fn(x,y)

def plus(op1, op2):
    return op1 + op2

def minus(op1, op2):
    return op1 - op2

ret_val = calc(plus, 10, 5)
print("calc(10, 5)의 결과 값: {0}".format(ret_val))

# 람다함수 - 중첩함수를 보다 더 효율적으로 사용하기 위해
def calc(operator_fn, x, y):
    return operator_fn(x, y)

ret_val = calc(lambda a, b: a + b, 10, 5)
print("람다함수의 결과값 : {0}".format(ret_val))

# 클로저 - 중첩함수 자체를 반환값으로 사용
def outer_func():
    id = 0

    def inner_func():
        nonlocal id    # 변수 id가 중첩함수인 inner_func 함수의 지역변수가 아님. 따라서 변수 id 접근 시, outer_func 함수 스코프에서 찾게 만든다.
        id += 1
        return id

    return inner_func # 이 때 주의할 것은 함수를 호출하는 것이 아니라 함수에 대한 참조를 반환한다는 것이다.

make_id = outer_func() # outer_func 함수가 호출되면 중첩함수인 inner_func 이 반환되어, make_id는 함수가 된다.
print("make_id() 호출의 결과 : {}".format(make_id()))

import sys
sys.stdin = open('input.txt', "r")
# 계산 함수 정의
def calculate(oper, a, b):
    if oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '*':
        return a * b
    else:
        return int(a / b)

# 연산자
operator = ['+', '-', '*', '/']

T = int(input())
for tc in range(1, T + 1):
    express = list(input().split())  # 식을 배열 형태로 저장
    stack = []

    try: # try 문을 통해 연산이 불가능한 경우 error 출력
        for elem in express:
            if elem in operator:  # 연산자인 경우
                b = stack.pop()
                a = stack.pop()
                stack.append(calculate(elem, a, b)) # 두 개의 숫자를 꺼내 연산 후 다시 스택에 쌓는다.

            elif elem == '.':  # . 인 경우
                result = stack.pop()
                if stack: # 출력 이후 만약 스택 안에 또 다른 숫자가 있으면 error 처리가 필요함 
                    result = 'error'

            else: # 숫자의 경우
                stack.append(int(elem))
    except:
        result = 'error'

    print('#{} {}'.format(tc, result))






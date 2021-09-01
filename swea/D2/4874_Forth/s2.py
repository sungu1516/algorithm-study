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
    print('#{}'.format(tc), end=' ')
    express = list(input().split())  # 식을 배열 형태로 저장
    stack = []

    for elem in express: # 식의 요소들을 순회
        if elem in operator:  # 연산자인 경우
            try:
                b = stack.pop()
                a = stack.pop()
                stack.append(calculate(elem, a, b)) # 두 개의 숫자를 꺼내 연산 후 다시 스택에 쌓는다.
            except:
                print('error')
                break

        elif elem == '.':  # . 인 경우
            if stack:
                print(stack.pop())
            else:
                print('error')

        else: # 숫자의 경우
            stack.append(int(elem))







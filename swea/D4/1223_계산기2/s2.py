import sys
sys.stdin = open('input.txt', "r")
# 계산 함수 정의
def calculate(oper, a, b):
    if oper == '+':
        return a + b
    else:
        return a * b

T = 10
for tc in range(1, T+1):
    N = int(input())    # tc의 길이
    express = list(input())    # 식을 문자열로 받는다
    stack = []  # 연산자를 쌓을 스택
    postfix = []    # 후위표기식을 담을 배열 (출력)
    operator = {'+': 0, '*': 1} # operator 의 우선순위

    # 후위표기식으로 변환
    for elem in express:
        if elem in operator:    # 만약 연산자인 경우
            while stack and operator[elem] <= operator[stack[-1]]:
                postfix.append(stack.pop()) # stack이 모두 비거나 우선순위가 높아질 때까지 stack의 모든 연산자를 출력
            stack.append(elem) # 위 작업을 마치면 스택에 현재 연산자를 누적
        else: # 피연산자의 경우
            postfix.append(elem)
    while stack: # stack에 남은 모든 연산자를 후위표기식에 더해주기
        postfix.append(stack.pop())

    # 후위표기식의 값들을 계산하기 - stack 이용
    for elem in postfix:
        if elem in operator:    # 요소가 연산자일 경우, stack의 top, top-1 에 위치한 숫자를 꺼내 계산 후 다시 stack에 쌓는다.
            b = stack.pop()
            a = stack.pop()
            stack.append(calculate(elem, a, b))
        else:
            stack.append(int(elem))     # 숫자들은 계산가능한 자료형으로 변환 후 stack 에 누적

    print('#{} {}'.format(tc, stack[0]))



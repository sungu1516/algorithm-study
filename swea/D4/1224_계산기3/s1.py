import sys
sys.stdin = open('input.txt', "r")
# 계산 함수 정의
def calculate(oper, a, b):
    if oper == '+':
        return a + b
    else:
        return a * b

T = 10
for tc in range(1, T + 1):
    N = int(input())    # tc의 길이
    express = list(input())     # 식
    stack = []
    postfix = []    # 후위표기식
    operator = {'(': 0, '+': 1, '*': 2}     # operator 우선순위

    # 후위표기식 만들기
    for elem in express:
        if elem == '(':   # 여는 괄호인 경우
            stack.append(elem)  # 스택에 들어가기 전엔 순위가 가장 높기 때문에, 일단 stack 에 쌓아줌

        elif elem in operator:    # 연산자인 경우
            while stack and operator[elem] <= operator[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(elem)

        elif elem == ')':    # 닫는 괄호인 경우
            while stack[-1] != '(':    # '(' 가 나오기 전까지의 모든 연산자를 postfix 에 누적한 후, '(' 를 스택에서 제거
                postfix.append(stack.pop())
            stack.pop() # '(' 을 제거해준다.

        else:   # 피연산자, 여는 괄호인 경우
            postfix.append(elem)

    while stack: # 식을 다 돌면 stack 에 남은 연산자들을 후위표기식에 모두 누적해준다.
        postfix.append(stack.pop())

    # 후위표기식 내용 계산하기 - 빈 스택을 다시 이용
    for elem in postfix:
        if elem in operator:
            b = stack.pop()
            a = stack.pop()
            stack.append(calculate(elem, a, b))
        else:
            stack.append(int(elem))

    print('#{} {}'.format(tc, stack[0]))




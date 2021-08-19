import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 필요함수 정의
def is_completed(pattern):
    stack = [] # 빈 스택 초기화
    brackets = ['(', ')', '{', '}']

    for elem in pattern: # 패턴 하나하나를 순회
        if elem not in brackets:
            continue
        else:
            if elem == '{' or elem == '(':
                stack.append(elem) # 괄호가 시작되는 경우 stack 에 누적
            else:
                if stack: # 스택에 괄호가 존재하는 경우
                    if elem == ')' and stack.pop() != '(':
                        return 0
                    elif elem == '}' and stack.pop() != '{':
                        return 0
                else: # 스택이 빈 경우
                    return 0

    if stack: # 반복문이 끝나고도 스택에 괄호가 남은 경우
        return 0
    return 1

T = int(input())

for _ in range(1, T + 1):
    tc = input()

    # 출력
    print('#{} {}'.format(_, is_completed(tc)))

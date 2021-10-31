# 인자로 들어온 괄호 문자열을 뒤집어 리턴하는 함수
def get_reversed(p):
    result = ''
    for elem in p:
        if elem == '(':
            result += ')'
        else:
            result += '('
    return result


# 인자로 들어온 괄호 문자열이 올바른 문자열인지 판단하는 함수
def is_correct(p):
    if p[0] == ')' or p[-1] == '(':
        return False
    return True


# 재귀함수 정의
def func(p):
    if not p:
        return ''

    # p를 u, v로 분리 - stack 이용
    stack = [p[0]]

    i = 1
    while stack:
        curr = p[i]

        if stack[-1] != curr:
            stack.pop()
        else:
            stack.append(curr)

        i += 1

    # while문이 종료되면, 균형잡힌 괄호 문자열을 발견한 직후의 인덱스가 i에 저장
    u = p[:i]
    v = p[i:]

    # u가 올바른 괄호 문자열인가? - if 분기
    # u가 올바른 문자열인 경우
    if is_correct(u):
        return u + func(v)
    # u가 올바른 문자열이 아닌 경우
    else:
        result = f'({func(v)}){get_reversed(u[1:-1])}'
        return result


def solution(p):
    answer = func(p)
    return answer
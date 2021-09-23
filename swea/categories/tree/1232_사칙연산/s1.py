import sys
sys.stdin = open('input.txt', 'r')

# 후위순회
def postorder(n):
    if n:
        postorder(left[n])
        postorder(right[n])
        # 후위순회를 하며, 방문지점 stack에 쌓기
        if tree[n] in operators:    # 방문 노드가 연산자인 경우
            result = calculate(tree[n], stack.pop(), stack.pop())
            stack.append(result)  # 연산결과를 다시 스택에 쌓는다.
        else:
            stack.append(tree[n])       # 방문노드가 숫자인 경우 stack 에 누적

# 연산자별 결과를 계산해 리턴하는 함수
def calculate(operater, a, b):
    if operater == '+':
        return b + a
    elif operater == '-':
        return b - a
    elif operater == '/':
        return b / a
    else:
        return b * a

# 연산자
operators = ['+', '-', '/', '*']

T = 10
for tc in range(1, T+1):
    N = int(input())  # 정점의 총 수
    # 자식 노드 번호 - 부모 노드의 번호를 인덱스로, 자식노드의 번호를 값으로 갖는 배열
    left = [0] * (N+1)
    right = [0] * (N+1)
    # 노드번호 별 노드값(연산자 or 피연산자)
    tree = [0] * (N+1)
    # 계산을 위한 빈 스택
    stack = []

    # 입력받아 필요한 배열 만들기
    for _ in range(N):
        input_list = input().split()
        if input_list[1] in operators:   # 정점이 연산자인 경우
            nn, oper, ch1, ch2 = input_list[0], input_list[1], input_list[2], input_list[3] # 노드번호, 연산자, 자식노드번호1, 번호2
            nn, ch1, ch2 = int(nn), int(ch1), int(ch2)  # 연산자를 제외하고 숫자로 변환
            tree[nn] = oper # value에 노드번호별 연산자 삽입
            left[nn] = ch1
            right[nn] = ch2
        else:
            nn, number = int(input_list[0]), int(input_list[1])
            tree[nn] = number # value에 노드번호별 숫자 삽입

    postorder(1)
    print(f'#{tc} {int(stack[0])}')
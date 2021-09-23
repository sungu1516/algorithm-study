import sys
sys.stdin = open('input.txt', 'r')

# 후위순회
def postorder(n):
    if n: # 해당 노드가 존재하는 경우에만
        postorder(tree[n][1])
        postorder(tree[n][2])
        # 후위순회를 하며, 방문지점 stack에 쌓기
        if tree[n][0] in operators:    # 방문 노드가 연산자인 경우
            result = calculate(tree[n][0], stack.pop(), stack.pop())
            stack.append(result)  # 연산결과를 다시 스택에 쌓는다.
        else:
            stack.append(tree[n][0])       # 방문노드가 숫자인 경우 stack 에 누적

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
    tree = [[0, 0, 0] for _ in range(N+1)]
    # 계산을 위한 빈 스택
    stack = []

    # 입력받아 필요한 배열 만들기
    for i in range(1, N+1):     # 정점 하나하나 순회
        input_list = input().split()
        if input_list[1] in operators:   # 정점이 연산자인 경우
            for j in range(1, len(input_list)):
                if input_list[j] not in operators:
                    input_list[j] = int(input_list[j])
                tree[i][j-1] = input_list[j]   # tree의 해당 정점에 operator, child1, child2 삽입
        else:
            nn, number = map(int, input_list)
            tree[nn][0] = number    # 자식노드 X, 노드값만 존재

    postorder(1)
    print(f'#{tc} {int(stack[0])}')
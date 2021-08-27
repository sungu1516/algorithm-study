import sys
sys.stdin = open('input.txt', 'r')
# 함수 정의 - Tree의 노드를 중위순회하며 출력
def in_order(n):
    if n:
        in_order(left[n])
        print(alphas[n], end='')
        in_order(right[n])

T = 10
for tc in range(1, T+1):
    V = int(input())
    left = [0] * (V+1)      # 왼쪽 자식 배열
    right = [0] * (V+1)     # 오른쪽 자식 배열
    alphas = [0] * (V+1)    # 노드번호가 인덱스로, 대응하는 알파벳이 값으로 존재하는 배열

    for _ in range(V):      # 입력값 받아서 left, right, alphas 만들어주기
        edge = input().split()
        par, alpha = int(edge.pop(0)), edge.pop(0)     # 우선 왼쪽 두 개의 원소를 빼서 부모노드, 알파벳 변수에 담아둠

        alphas[par] = alpha # 노드번호를 인덱스로 갖고, 알파벳을 값으로 가짐

        if edge:            # 만약, edge 에 원소가 남았다면 (연결된 자식 노드가 있는 경우)
            left[par] = int(edge.pop(0))     # 왼쪽 자식 요소를 넣어준다.

            if edge:        # 오른쪽 자식노드도 있다면
                right[par] = int(edge.pop())

    print('#{}'.format(tc), end=' ')
    in_order(1)
    print()

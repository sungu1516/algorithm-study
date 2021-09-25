import sys
sys.stdin = open('input.txt', 'r')

# 후위순회 함수 정의
def postorder(n):
    if n <= N:
        postorder(2*n)  # 왼쪽자식으로 이동
        postorder(2*n + 1)  # 오른쪽자식으로 이동
        visit(n)                    # 방문 후 처리

def visit(n):      # 노드에 방문 시 처리 내용
    if n != 1:
        tree[n//2] += tree[n]

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1) # tree 초기화

    # tree 에 리프노드값 삽입
    for _ in range(M):
        idx, val = map(int, input().split())
        tree[idx] = val

    # 완전이진트리 완성
    postorder(1)
    print(tree[L])
import sys
sys.stdin = open('input.txt', 'r')

# 중위순회 - 방문지점을 tree 의 인덱스로 활용
def inorder(n):
    global cnt
    if n < N + 1:
        inorder(2*n)        # 왼쪽 자식으로 이동
        tree[n] = cnt       # 방문노드 - 처리 : 노드값에 cnt 삽입
        cnt += 1
        inorder(2*n + 1)    # 오른쪽 자식으로 이동

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)  # 완전이진트리를 나타내는 배열을 초기화
    cnt = 1             # 트리의 노드에 채울 값 초기화

    inorder(1)

    print(tree[1], tree[N//2])




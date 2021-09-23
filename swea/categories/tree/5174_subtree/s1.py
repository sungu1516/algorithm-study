import sys
sys.stdin = open('input.txt', 'r')
# 전위 순회 함수 정의
def preorder(n):
    global cnt
    if n:
        cnt += 1
        preorder(left[n])
        preorder(right[n])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())    # 간선의 개수, 루트로 삼을 노드
    arr = list(map(int, input().split()))
    cnt = 0     # subtree 의 노드 개수 초기화

    left = [0] * (E+2)  # 왼쪽 자식노드 번호가 담긴 배열
    right = [0] * (E+2)

    for i in range(E):
        if left[arr[2*i]]:   # 만약 왼쪽 자식노드가 존재한다면
            right[arr[2*i]] = arr[2*i + 1]
            continue
        left[arr[2*i]] = arr[2*i + 1]

    preorder(N)
    print(f'#{tc} {cnt}')
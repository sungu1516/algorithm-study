import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for _ in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # N < M 이라고 가정
    if N > M: # 만약 N이 M보다 크다면 값을 서로 바꿔줌
        N, M = M, N
        A, B = B, A

    # 최댓값 초기화 (숫자범위가 주어지지 않음)
    max_val = 0
    for i in range(N):
        max_val += A[i] * B[i]

    # 반복문 통해 최댓값 탐색
    for i in range(1, M-N+1):
        temp = 0
        for j in range(0, N):
            temp += A[j] * B[i]
            i += 1
        if max_val < temp:
            max_val = temp

    print('#{} {}'.format(_, max_val))

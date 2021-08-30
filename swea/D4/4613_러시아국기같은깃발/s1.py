import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())    # N = 줄(칸) 수, M = 문자열의 길이
    arr = [input() for _ in range(N)]

    min_value = N*M     # 최솟값 초기화
    for i in range(1, N-1):
        for j in range(1, N-1):
            for k in range(1, N-1):
                if i + j + k == N:
                    total = 0
                    # white
                    for w in range(i):
                        total += M - arr[w].count('W')
                    # blue
                    for b in range(i, i + j):
                        total += M - arr[b].count('B')
                    # red
                    for r in range(i + j, N):
                        total += M - arr[r].count('R')
                    # 최솟값 갱신?
                    if total < min_value:
                        min_value = total

    print('#{} {}'.format(tc, min_value))
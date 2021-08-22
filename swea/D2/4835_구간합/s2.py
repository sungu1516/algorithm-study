import sys
sys.stdin = open('input.txt')

# test case
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 최솟값, 최댓값 구하기
    max_val = 0
    min_val = 10000 * M
    for i in range(N-M+1):
        total = 0
        for j in range(i, i+M):
            total += arr[j]
        if max_val < total:
            max_val = total
        if min_val > total:
            min_val = total

    # 차이값 출력
    ans = max_val - min_val
    print('#{} {}'.format(tc, ans))
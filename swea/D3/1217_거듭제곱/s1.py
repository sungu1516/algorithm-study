import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 함수 정의
def power(n, m):
    # 종료조건
    if m == 1:
        return n
    else:
        return n * power(n, m-1)
T = 10
for _ in range(1, T + 1):
    tc = input()
    N, M = map(int, input().split())
    ans = power(N, M)
    print('#{} {}'.format(tc, ans))
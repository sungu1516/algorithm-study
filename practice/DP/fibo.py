# 피보나치 수열 함수
# DP로 구현

# 하향식
d = [0] * 100
def fibo_topDown(n):
    # 종료조건
    if n == 1 or n == 2:
        return 1

    if d[n]:
        return d[n]

    return fibo_topDown(n - 1) + fibo_topDown(n - 2)

# 상향식
def fibo_bottomUp(n):
    memo = [0] * 100
    # f(1), f(2) value 채워주기
    memo[1] = 1
    memo[2] = 1
    # 피보나치 수열 완성 (n까지)
    for i in range(3, n + 1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]

print(fibo_topDown(6))
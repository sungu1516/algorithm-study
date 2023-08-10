# input
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# main
dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    t = a[i][0]     # time

    # i번째 날에 일하는 경우
    if i + t <= n:
        p = a[i][1]   # profit
        dp[i] = max(dp[i + 1], dp[i + t] + p)

    # i번째 날에 일하지 않는 경우
    else:
        dp[i] = dp[i + 1]

print(dp[0])
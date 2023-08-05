# input
n = int(input())

# main
dp = [[0] * 2 for _ in range(n + 1)]

# init
dp[1][1] = 1

# bottom-top
for i in range(2, n + 1):
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
    dp[i][1] = dp[i - 1][0]

print(sum(dp[n]))
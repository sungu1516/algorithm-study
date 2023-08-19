# input
n = int(input())
wine = [int(input()) for _ in range(n)]

# main
dp = [[0] * 3 for _ in range(n)]

# init
dp[0][0] = 0
dp[0][1] = wine[0]
dp[0][2] = wine[0]

# bottom-top
for i in range(1, n):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i-1][0] + wine[i]
    dp[i][2] = dp[i-1][1] + wine[i]

print(max(dp[n-1]))
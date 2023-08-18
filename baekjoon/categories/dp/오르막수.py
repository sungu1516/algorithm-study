# input
n = int(input())

# main
dp = [[0] * (10) for _ in range(n + 1)]
mod = 10007

# init
for i in range(10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        for k in range(j + 1):
            dp[i][j] += dp[i - 1][k]

print(sum(dp[n]) % mod)
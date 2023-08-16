# input
t = int(input())

# main
mod = 1000000009
dp = [0] * 1000001
dp[0] = 1

for i in range(1, 1000001):
    if i - 1 >= 0:
        dp[i] += dp[i - 1]
    if i - 2 >= 0:
        dp[i] += dp[i - 2]
    if i - 3 >= 0:
        dp[i] += dp[i - 3]
    dp[i] %= mod

for _ in range(t):
    n = int(input())
    print(dp[n])
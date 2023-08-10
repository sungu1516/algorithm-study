# input
n = int(input())
a = list(map(int, input().split()))

# main
dp = [0] * n
dp[0] = a[0]    # init

for i in range(1, n):
    if dp[i - 1] > 0:
        dp[i] = a[i] + dp[i - 1]
    else:
        dp[i] = a[i]

print(max(dp))
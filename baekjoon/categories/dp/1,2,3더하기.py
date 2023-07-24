# input
t = int(input())

nums = [int(input()) for _ in range(t)]
n = max(nums)

# dp - bottomTop
dp = [0] * (n + 1)
dp[0] = 1
dp[1], dp[2] = 1, 2

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for num in nums:
    print(dp[num])
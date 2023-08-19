# input
n = int(input())
a = list(map(int, input().split()))

# main
dp = [0] * n

for i in range(n):
    dp[i] = a[i]
    for j in range(i):
        if a[j] < a[i] and dp[j] + a[i] > dp[i]:
            dp[i] = dp[j] + a[i]

# max 의 idx 찾기
max_val = max(dp)

print(max_val)

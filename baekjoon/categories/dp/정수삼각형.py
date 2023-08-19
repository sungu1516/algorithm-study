# input
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# main
dp = [[0] * n for _ in range(n)]

# init
dp[0][0] = a[0][0]

# bottom-top
for i in range(1, n):
    for j in range(len(a[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j] + a[i][j]
        elif j == len(a[i]) - 1:
            dp[i][j] = dp[i-1][j-1] + a[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + a[i][j]

# print answer
print(max(dp[n-1]))
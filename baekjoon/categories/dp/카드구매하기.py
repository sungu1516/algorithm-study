# input
n = int(input())
price = list(map(int, input().split()))
price.insert(0, 0)

# main
# dp - bottomTop
dp = [0] * (n + 1)
dp[0] = 0
dp[1] = price[1]


for i in range(2, n + 1):
    max_val = 0
    for j in range(1, i + 1):
        tmp_val = dp[i - j] + price[j]
        if tmp_val > max_val:
            max_val = tmp_val

    dp[i] = max_val

print(dp[n])
# input
n = int(input())
a = list(map(int, input().split()))

# main
dp = [0] * n
v = [-1] * n   # 이전 수의 인덱스

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if a[j] < a[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            v[i] = j

# max 의 idx 찾기
max_val = max(dp)
idx = dp.index(max_val)
result = []

print(max_val)

while idx != -1:
    result.append(a[idx])
    idx = v[idx]

for i in range(len(result) - 1, -1, -1):
    print(result[i], end=' ')
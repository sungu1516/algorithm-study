# 6089 : [기초-종합] 수 나열하기2

a, d, n = map(int, input().split())

result = a * d ** (n - 1)
print(result)
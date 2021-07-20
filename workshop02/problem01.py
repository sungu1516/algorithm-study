# 1. 간단한 N의 약수 (SWEA #1933)

n = int(input())
factors = []

for number in range(1, n//2 + 1):
    if n % number:
        continue
    else:
        factors.append(number)
factors.append(n)

for factor in factors:
    print(factor, end = ' ')

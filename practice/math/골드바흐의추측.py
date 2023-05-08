# prime arr 생성
MAX = 1000000
check = [0] * (MAX + 1)
check[0] = check[1] = True  # 소수가 아닌 경우 True
prime = []

for i in range(2, MAX + 1):
    if not check[i]:
        prime.append(i)
        j = i + i
        while j <= MAX:
            check[j] = True
            j += i

prime = prime[1:]

# 골드바흐의 추측 검증
while True:
    n = int(input())
    if n == 0:
        break
    for p in prime:
        # a + b = n 에서, a가 소수라면 b가 소수라는 것만 증명하면 됨
        if not check[n-p]:
            print("{0} = {1} + {2}".format(n, p, n - p))
            break
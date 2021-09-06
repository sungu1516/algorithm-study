N, K = map(int, input().split())
currency = [int(input()) for _ in range(N)]
cnt = 0
i = N-1

while K > 0:
    cnt += K // currency[i]
    K %= currency[i]
    i -= 1

print(cnt)


N = int(input())
prices = [int(input()) for _ in range(N)]
total = 0   # 최소비용 초기화

# 내림차순으로 정렬
prices.sort(reverse=True)

# (인덱스 + 1) 이 3의 배수인 경우를 제외하고 모두 더하기
for i in range(N):
    if (i + 1) % 3 == 0:
        total += prices[i]

print(sum(prices) - total)
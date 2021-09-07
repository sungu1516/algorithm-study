N = int(input())    # 줄 서있는 사람의 수
tips = [int(input()) for _ in range(N)]   # 각 사람의 팁

# 팁이 줄어드는 것을 최소화해야 > 내림차순 정렬
tips.sort(reverse=True)

# 순서에 따른 팁 계산
for i in range(N):
    temp = tips[i] - i
    if temp < 0:    # 결과값이 0보다 작은 경우, 0으로 대체
        tips[i] = 0
        continue
    tips[i] = temp

print(sum(tips))
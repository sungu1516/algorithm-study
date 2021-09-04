N = int(input())    # 줄 선 사람의 수
P = list(map(int, input().split()))     # 사람당 걸리는 시간
P.sort()

wating_time = [0] * (N + 1)
for i in range(N):
    wating_time[i+1] = wating_time[i] + P[i]

print(sum(wating_time))
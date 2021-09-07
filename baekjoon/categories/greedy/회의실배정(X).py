N = int(input())

meetings = [tuple(map(int, input().split())) for _ in range(N)]

# 시작시간을 기준으로 selection sort
for i in range(N-1):
    min_idx = i
    for j in range(i+1, N):
        if meetings[min_idx][0] > meetings[j][0]:
            min_idx = j

    meetings[i], meetings[min_idx] = meetings[min_idx], meetings[i]


# 재귀함수 정의 - 특정 회의 시간정보와 cnt를 넣으면, 최대 회의 수 리턴
def get_max(idx, cnt):
    min_idx = 100
    for i in range(idx, N):
        if meetings[idx][1] <= meetings[i][1] and meetings[i][1] < min_idx:
            min_idx = i
    # 이후의 시간대 중 최선의 회의 시간대를 찾았으므로
    if min_idx == 100:
        return cnt
    get_max(idx, cnt+1)

print(get_max(0, 0))
import sys
sys.stdin = open('input.txt', 'r')

# dfs
def dfs(idx):   # 탐색할 idx
    global cnt
    cnt += 1     # 작업횟수 추가

    end = schedule[idx][1]  # 종료시간
    for i in range(idx+1, N):   # 현재 작업시간대 이후부터 탐색
        if end <= schedule[i][0]:   # 특정 작업대의 시작시간이 현재 작업의 종료시간 이후라면
            dfs(i)  # 해당 작업시간대로 이동 후 탐색
            break   # 만약 최적의 다음 시간대를 찾았다면, 반복문 탈출

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    schedule = [tuple(map(int, input().split())) for _ in range(N)] # 신청서
    cnt = 0     # 최대 작업횟수 초기화
    # 작업 종료시간을 기준으로 schedule 배열을 오름차순 정렬한다.
    schedule.sort(key = lambda a_schedule : a_schedule[1])

    # 탐색
    dfs(0)

    print('#{} {}'.format(tc, cnt))
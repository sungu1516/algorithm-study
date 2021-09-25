import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
# 우하좌상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]   # 물, 땅

    dist = [[0] * M for _ in range(N)]  # 방문 겸 거리 기록

    que = deque()   # 큐 초기화

    # Water 의 좌표를 모두 que 에 삽입
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                que.append((i, j))

    # que가 빌 때까지 반복하며, dist 에 거리 기록
    while que:
        i, j = que.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if ni < 0 or ni >= N or nj < 0 or nj >= M or dist[ni][nj] or arr[ni][nj] == 'W': continue

            que.append((ni, nj))    # que에 누적
            dist[ni][nj] = dist[i][j] + 1

    # 거리의 합 출력
    total = 0
    for row in dist:
        for elem in row:
                total += elem

    print('#{} {}'.format(tc, total))
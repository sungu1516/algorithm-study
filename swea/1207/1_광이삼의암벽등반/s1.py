import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

# delta
dr =  (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

# dfs
def dfs(coordinate, duration, cnt):
    global min_cnt

    if cnt >= min_cnt:
        return
    r, c = coordinate

    # 도착지점까지의 맨해튼 거리
    dist = r + (N - 1 - c)

    # 만약 현재 지점부터 도착지점까지 고리 교체없이 갈 수 있는 경우
    if dist <= duration:
        min_cnt = min(cnt, min_cnt)
        return

    # 고리교체 로직
    if graph[r][c] == 1:
        if L >= dist:
            min_cnt = min(cnt+1, min_cnt)
            return

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= M or nc < 0 or nc >= N or visited[nr][nc]: continue

            visited[nr][nc] = 1
            dfs((nr, nc), L - 1, cnt + 1)
            visited[nr][nc] = 0

    # 탐색
    if duration <= 0:
        return
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or nr >= M or nc < 0 or nc >= N or visited[nr][nc]: continue

        visited[nr][nc] = 1
        dfs((nr, nc), duration - 1, cnt)
        visited[nr][nc] = 0


T = int(input())
for tc in range(1, T+1):
    M, N, L = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(M)]

    visited = [[0] * N for _ in range(M)]
    min_cnt = 987654321

    # 만약 한 번에 갈 수 있는 경우
    if L >= M + N - 2:
        print(f'#{tc} 0')
        continue

    # bfs 로 도착지점까지의 거리 구하기
    dist_arr = [[0] * N for _ in range(M)]

    que = deque()
    que.append((0, N-1))
    dist_arr[0][N-1] = 1

    while que:
        r, c = que.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= M or nc < 0 or nc >= N or dist_arr[nr][nc]: continue
            dist_arr[nr][nc] = dist_arr[r][c] + 1
            que.append((nr, nc))

    min_val = 987654321
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                if dist_arr[i][j] - 1 < min_val:
                    min_val = dist_arr[i][j] - 1

    if min_val > L:
        print(f'#{tc} -1')
        continue

    visited[M-1][0] = 1
    dfs((M-1, 0), L, 0)

    if min_cnt == 987654321:
        min_cnt = -1

    print(f'#{tc} {min_cnt}')
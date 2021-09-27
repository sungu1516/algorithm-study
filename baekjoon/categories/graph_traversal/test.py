from collections import deque

dr = [0, 1, 0, -1]  # 우하좌상
dc = [1, 0, -1, 0]

# delta 탐색 - 우하좌상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# bfs 함수 정의
def bfs(graph, start, visited):
    # queue 에 시작지점 삽입
    queue = deque([start])
    # 시작지점 방문처리
    visited[start[0]][start[1]] = 1
    # queue 가 빌 때까지 반복
    while queue:
        # queue 의 가장 앞의 원소(좌표) 빼기
        curr = queue.popleft()
        # 유효범위 내에 있고, 1이고, 아직 방문하지 않은 좌표들을 queue 에 삽입
        for i in range(4):
            next_i, next_j = curr[0] + di[i], curr[1] + dj[i]
            if 0 <= next_i < N and 0 <= next_j < M and not visited[next_i][next_j] and graph[next_i][next_j]:
                if next_i == N - 1 and next_j == M - 1:     # 도착 지점인 경우, 함수 종료
                    return visited[curr[0]][curr[1]] + 1
                visited[next_i][next_j] = visited[curr[0]][curr[1]] + 1
                queue.append([next_i, next_j])
    for row in graph:
        print(*row)
    print()

def dfs(r, c, brick_cnt):
    visited[r][c] = 1
    graph[r][c] = 1

    if brick_cnt == 0:  # 벽 3개를 모두 세운 경우
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 2:    # 만약 바이러스라면,
                    new_visited = [[0] * M for _ in range(N)]
                    bfs(graph, (i, j), [[0] * M for _ in range(N)])
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and graph[nr][nc] == 0:
            dfs(nr, nc, brick_cnt - 1)
            visited[nr][nc] = 0
            graph[nr][nc] = 0

    visited[r][c] = 0
    graph[r][c] = 0

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            dfs(i, j, 2)



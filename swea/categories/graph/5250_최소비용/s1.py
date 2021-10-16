import sys
sys.stdin = open('input.txt')

from collections import deque

# delta
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

# bfs
def bfs(r, c):
    visited[r][c] = 0
    que = deque()
    que.append((r, c))

    while que:
        r, c = que.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue

            # 연료 소비량을 비교 후, 만약 더 작은 경우만 갱신
            # 높은 곳으로 이동하는 경우
            if graph[r][c] < graph[nr][nc]:
                cost = graph[nr][nc] - graph[r][c] + visited[r][c] + 1
                if cost < visited[nr][nc]:
                    # 기존의 cost보다 더 작은 경우
                    visited[nr][nc] = cost
                    que.append((nr, nc))
            # 낮은 곳으로 이동하는 경우
            else:
                cost = visited[r][c] + 1
                if cost < visited[nr][nc]:
                    # 기존의 cost보다 더 작은 경우
                    visited[nr][nc] = cost
                    que.append((nr, nc))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[987654321] * N for _ in range(N)]

    bfs(0, 0)

    print('#{} {}'.format(tc, visited[N-1][N-1]))
from collections import deque
# input
m, n = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

# function
def bfs(start, dist):
    # init
    q = deque([start])
    dist[0][0] = 0

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            if dist[nr][nc] == -1:
                if graph[nr][nc] == 0:
                    dist[nr][nc] = dist[r][c]
                    q.appendleft((nr, nc))
                else:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

# main
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)
dist = [[-1] * m for _ in range(n)]

bfs((0,0), dist)

print(dist[n - 1][m - 1])
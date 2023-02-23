N = 4
M = 5

ices = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

from collections import deque
def solution(N, M, ices):
    dr = (1, 0, -1, 0)
    dc = (0, 1, 0, -1)
    answer = 0

    def bfs(graph, start, visited):
        que = deque([start])
        visited[start[0]][start[1]] = True

        while que:
            r, c = que.popleft()
            for i in range(4):
               nr, nc = r + dr[i], c + dc[i]
               if(nr > -1 and nc > -1 and nr < N and nc < M and not visited[nr][nc] and not graph[nr][nc]):
                   que.append((nr, nc))
                   visited[nr][nc] = True

    visited = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and not ices[i][j]:
                answer += 1
                bfs(ices, (i, j), visited)

    return answer

print(solution(N, M, ices))

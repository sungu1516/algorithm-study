import sys
sys.stdin = open('input.txt')
from collections import deque

# delta
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

# bfs
def bfs(r, c):
    que = deque([(r, c)])

    while que:
        r, c = que.popleft()
        tmp = graph[r][c]
        graph[r][c] = 0

        for i in range(4):
            nr, nc = r, c
            for _ in range(tmp-1):
                nr += dr[i]
                nc += dc[i]
                # 인덱스 검사 & 벽돌이 있는 경우만
                if 0 <= nr < H and 0 <= nc < W and graph[nr][nc]:
                    que.append((nr, nc))

    # arrange
    #arrange(graph)



def arrange(graph):
    for j in range(W):
        for i in range(H-1, -1, -1):
            if graph[i][j] == 0:
                for k in range(i-1, -1, -1):
                    if graph[i][k]:
                        # 위치 교환
                        graph[i][j], graph[i][k] = graph[i][k], graph[i][j]
                        break


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(H)]

    for row in graph:
        print(*row)
    print()

    bfs(2, 2)

    bfs(1, 2)
    for row in graph:
        print(*row)
    print()

    bfs(2, 2)

    for row in graph:
        print(*row)
    print()
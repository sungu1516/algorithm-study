import sys
sys.stdin = open('input.txt')

# delta
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

# bfs
def bfs():
    r = c = 0
    fuel[r][c] = 0
    que = [0] * 100000
    front = rear = -1
    rear += 1
    que[rear] = (r, c)

    while front != rear:
        front += 1
        r, c = que[front]

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue

            # 연료 소비량을 비교 후, 만약 더 작은 경우만 갱신
            cost = graph[nr][nc] - graph[r][c] + 1 if graph[nr][nc] > graph[r][c] else 1
            if fuel[r][c] + cost < fuel[nr][nc]:
                # que에 삽입
                rear += 1
                que[rear] = (nr, nc)
                # fuel 갱신
                fuel[nr][nc] = fuel[r][c] + cost


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    fuel = [[987654321] * N for _ in range(N)]

    bfs()

    print('#{} {}'.format(tc, fuel[N-1][N-1]))
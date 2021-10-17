import sys
sys.stdin = open('input.txt')

from collections import deque

# delta
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

# bfs
def bfs():
    time[0][0] = 0
    que = deque()
    que.append((0, 0))

    # 최소 시간 갱신
    while que:
        r, c = que.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue

            # 만약 현재칸까지의 소요시간 + 다음칸의 공사 시간이 기존 다음칸의 소요시간보다 작다면
            if time[r][c] + arr[nr][nc] < time[nr][nc]:
                time[nr][nc] = time[r][c] + arr[nr][nc] # 기존 소요시간 갱신
                que.append((nr, nc))    # que에 삽입

    return time[N-1][N-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    time = [[987654321] * N for _ in range(N)]

    print('#{} {}'.format(tc, bfs()))
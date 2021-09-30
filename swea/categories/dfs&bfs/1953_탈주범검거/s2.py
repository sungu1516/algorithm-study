from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
# delta
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 구조물 타입별 이동가능 방향 (우, 하, 좌, 상)
dir = [
    (0, 0, 0, 0),
    (1, 1, 1, 1),
    (0, 1, 0, 1),
    (1, 0, 1, 0),
    (1, 0, 0, 1),
    (1, 1, 0, 0),
    (0, 1, 1, 0),
    (0, 0, 1, 1),
]

# bfs
def bfs(r, c):
    visited = [[0] * M for _ in range(N)]   # 방문기록 및 경과한 시간 기록
    visited[r][c] = 1
    que = deque([(r, c)])
    cnt = 0     # 탈주범이 위치할 수 있는 장소의 개수 초기화

    while que:
        r, c = que.popleft()
        cnt += 1
        if visited[r][c] == L:  # 주어진 시간이 경과했을 경우
            continue

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            # 다음 칸으로 이동할 수 있는지 확인
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and graph[nr][nc] != 0:
                if  dir[graph[nr][nc]][(i+2)%4] and dir[graph[r][c]][i]:
                    visited[nr][nc] = visited[r][c] + 1
                    que.append((nr, nc))
    return cnt

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(tc, bfs(R,C)))
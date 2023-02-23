# input
n, m = 5, 6
mirro = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]
###############################

# 답
from collections import deque
# delta - 우하좌상
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def bfs(sr, sc):
    # 첫 방문 노드를 que에 삽입
    que = deque([(sr, sc)])
    # que가 빌 때까지 pop
    while que:
        # que의 top 노드 꺼내기
        r, c = que.popleft()
        # delta 이동
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            # 만약 목표 지점인 경우
            if nr + 1 == n and nc + 1 == m:
                return mirro[r][c] + 1
            # 검증 - 1. 범위를 초과할 경우
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            # 검증 - 2. 0이 아니고 해당 노드를 처음 방문하는 경우만
            if mirro[nr][nc] == 1:
                # 거리 기록
                mirro[nr][nc] = mirro[r][c] + 1
                # que에 삽입
                que.append((nr, nc))

print(bfs(0, 0))
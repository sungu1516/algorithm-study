# 입출력
n = int(input())
height_arr = [list(map(int, input().split())) for _ in range(n)]

# 구현
# bfs
from collections import deque
def bfs(start, height, visited):
    # que 초기화
    que = deque([start])
    # 첫 노드 방문처리
    r, c = start[0], start[1]
    visited[r][c] = 1
    # que가 빌 때까지 실행
    while que:
        # que의 front 뽑기
        v = que.popleft()
        r, c = v[0], v[1]   # 뽑은 노드의 좌표값
        # 뽑은 노드의 모든 인접노드 탐색
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]   # 방문 예정인 노드의 좌표
            # 방문 조건
            # 1.그래프 범위 내 2.방문하지 않은 곳 3.안전영역인 곳
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            if not visited[nr][nc] and height_arr[nr][nc] > height:
                # 방문 시
                # que에 삽입
                que.append((nr, nc))
                # 방문처리
                visited[nr][nc] = 1

# main
# delta - 우하좌상
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

# 2차원 배열 내 최대값 구하기
max_height = 0
for row in height_arr:
    temp_val = max(row)
    if temp_val > max_height:
        max_height = temp_val

# 0 <= h < 최대값 범위의 모든 강수 높이를 탐색
max_cnt = 1
for h in range(max_height):
    # 안전영역 수
    cnt = 0
    # visited 배열 초기화
    visited = [[0] * n for _ in range(n)]
    # height_arr에 대해 bfs 탐색
    for i in range(n):
        for j in range(n):
            # 1. 안전영역만 탐색
            # 2. 방문하지 않은 영역만 탐색
            if height_arr[i][j] > h and not visited[i][j]:
                bfs((i, j), h, visited)
                cnt += 1

    # 안전 영역 최대 개수 초기화
    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)
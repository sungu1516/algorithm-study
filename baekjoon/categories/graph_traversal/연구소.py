from collections import deque
import copy
import sys
input = sys.stdin.readline

# delta 탐색 - 우하좌상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# bsf 함수
def bfs(new_graph):
    global max_safe_area
    queue = deque()  # 시작지점 queue 삽입

    # 바이러스의 좌표 큐에 담기 & 방문처리
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                queue.append((i,j))

    while queue:
        curr = queue.popleft()
        for i in range(4):
            n_i, n_j = curr[0] + di[i], curr[1] + dj[i]
            if 0 <= n_i < N and 0 <= n_j < M  and new_graph[n_i][n_j] == 0:    # 유효한 인덱스 범위 내에 있는 경우
                    queue.append([n_i, n_j])
                    new_graph[n_i][n_j] = 2  # 바이러스 감염

    safe_area = 0
    for row in new_graph:
        safe_area += row.count(0)

    if max_safe_area < safe_area:
        max_safe_area = safe_area

# 그래프에 벽을 설치한 후, 3개 설치 완료 시 bfs 를 통해 안전지대 최대값을 갱신
def set_wall(cnt):

    if cnt == 3: # 3개 설치한 경우
        copied_graph = copy.deepcopy(graph)
        bfs(copied_graph)  # 벽이 설치된 그래프를 넣는다.

    else:
        for i in range(N): # brute force
            for j in range(M):
                if graph[i][j] == 0: # 해당 구역이 0인 경우에
                    graph[i][j] = 1 # 벽으로 선택
                    set_wall(cnt+1) # 다음 벽 선택
                    graph[i][j] = 0 # 되돌리기


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
max_safe_area = 0

set_wall(0)

print(max_safe_area)
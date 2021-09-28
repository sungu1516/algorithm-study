from collections import deque

# 좌표가 유효한 범위 내에 있는지 확인하는 함수
def is_valid(idx_i, idx_j):
    if 0 <= idx_i < N and 0 <= idx_j < M:
        return True
    return False

# delta 탐색 - 우하좌상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# bfs 함수 정의
def bfs(graph, start, visited):
    # queue 에 시작지점 삽입
    queue = deque([start])
    # 시작지점 방문처리
    visited[start[0]][start[1]] = 1
    # queue 가 빌 때까지 반복
    while queue:
        # queue 의 가장 앞의 원소(좌표) 빼기
        curr = queue.popleft()
        # 유효범위 내에 있고, 1이고, 아직 방문하지 않은 좌표들을 queue 에 삽입
        for i in range(4):
            next_i, next_j = curr[0] + di[i], curr[1] + dj[i]
            if is_valid(next_i, next_j) and not visited[next_i][next_j] and graph[next_i][next_j]:
                if next_i == N - 1 and next_j == M - 1:     # 도착 지점인 경우
                    return visited[curr[0]][curr[1]] + 1
                visited[next_i][next_j] = visited[curr[0]][curr[1]] + 1
                queue.append([next_i, next_j])

N, M = map(int, input().split())    # 도착 지점 입력받기
graph = [[int(x) for x in input()] for _ in range(N)]    # 그래프 입력받기

visited = [[0]*M for _ in range(N)]       # 방문지점 초기화

# bfs 실행
print(bfs(graph, [0, 0], visited))

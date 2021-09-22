from collections import deque
# 좌표가 유효한 범위 내에 있는지 확인하는 함수
def is_valid(idx_i, idx_j):
    if 0 <= idx_i < N and 0 <= idx_j < M:
        return True
    return False

# bsf 함수
def bsf(start):
    cnt = 0 # 바이러스가 정복한 빈칸 개수 초기화
    visited = [[0] * M for _ in range(N)]     # 방문지점
    queue = deque([start])  # 시작지점 queue 삽입
    visited[start[0]][start[1]] = 1 # 시작지점 방문처리

    while queue:
        curr = queue.popleft()
        cnt += 1    # 바이러스가 정복가능한 빈 공간의 개수를 count
        for i in range(4):
            n_i, n_j = curr[0] + di[i], curr[1] + dj[i]
            if is_valid(n_i, n_j) and not visited[n_i][n_j]:    # 유효한 인덱스 범위 내에 있고 방문하지 않은 경우
                if graph[n_i][n_j] == 0:    # 해당 영역이 빈 공간일 경우
                    queue.append([n_i, n_j])
                    visited[n_i][n_j] = 1

    return cnt

di = [0, 1, 0, -1]  # 우하좌상
dj = [1, 0, -1, 0]

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 벽 설치 위치 선정 - 조합 사용하여 brute force
graph[0][1], graph[1][0], graph[3][5] = 1, 1, 1

# 함수 실행 - 바이러스가 전염된 영역의 수 구하기
total = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            start = [i, j]
            total += bsf(start)

print(total)
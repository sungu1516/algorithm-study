import sys
sys.stdin = open('input.txt', 'r')

# delta
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# dfs
def dfs(v, visited, dist, able):    # 현재 좌표, 방문지점, 거리, 공사 가능여부
    global max_dist

    # 좌표
    i, j = v
    # 방문처리
    visited[i][j] = True

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            # 다음 지점의 높이가 더 낮은 경우
            if graph[i][j] > graph[ni][nj]:
                dfs((ni, nj), visited, dist + 1, able)
            # 다음 지점의 높이가 같거나 높은 경우
            else:
                if able and graph[i][j] > graph[ni][nj] - K:
                    temp = graph[ni][nj]
                    graph[ni][nj] = graph[i][j] - 1
                    dfs((ni, nj), visited, dist + 1, False)
                    # 공사처리 원상복구
                    graph[ni][nj] = temp
                # 공사를 해도 이동 불가인 경우
                else:
                    # 거리 비교 후 최대거리 갱신
                    if dist > max_dist:
                        max_dist = dist

    visited[i][j] = False # 방문처리 해제

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    max_dist = 0

    # 최대 높이 찾기
    max_h = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > max_h:
                max_h = graph[i][j]

    # 최대 높이에서 등산로 조성 시작
    for i in range(N):
        for j in range(N):
            if graph[i][j] == max_h:
                dfs((i, j), visited, 1, True)

    print('#{} {}'.format(tc, max_dist))
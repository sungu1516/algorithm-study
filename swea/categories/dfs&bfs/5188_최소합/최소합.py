import sys
sys.stdin = open('input.txt', 'r')
# delta
dr = [1, 0] # 우하
dc = [0, 1]

def dfs(r, c, total):
    global min_value
    if total >= min_value:
        return

    if r == c == N-1:
        # 최소값을 갱신
        if total < min_value:
            min_value = total

    for i in range(2):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            # 방문처리
            visited[nr][nc] = 1
            # 누적합 후 dfs
            dfs(nr, nc, total + graph[nr][nc])
            # 방문처리 해제
            visited[nr][nc] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1
    min_value = 10 * N

    dfs(0, 0, graph[0][0])

    print('#{} {}'.format(tc, min_value))
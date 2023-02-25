# 1. DFS 풀이
# 경로의 수
cnt = 0

def solution(m, n, puddles):
    # delta - 우하
    dr = (0, 1)
    dc = (1, 0)

    # dfs 함수 정의
    def dfs(v, visited):
        global cnt
        # 종료조건
        if v[0] == n - 1 and v[1] == m - 1:
            cnt += 1
            return

        # 방문 기록
        visited[v[0]][v[1]] = 1

        # 방문 - 우, 하 방향으로만
        for i in range(2):
            # 이동 예정 노드의 좌표
            nr, nc = v[0] + dr[i], v[1] + dc[i]
            # 이동 가능 검증 - 유효 범위, 웅덩이 x, 방문하지 않은 곳
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            if not visited[nr][nc]:
                # 재귀적 방문
                dfs((nr, nc), visited)
                # 복귀 이후 방문처리 원복
                visited[nr][nc] = 0

    # 방문 기록
    visited = [[0 for _ in range(m)] for _ in range(n)]

    # 웅덩이 표시
    for puddle in puddles:
        visited[puddle[1] - 1][puddle[0] - 1] = 9

    # dfs 실행
    dfs((0, 0), visited)

    return cnt % 1000000007

# 2. DP 풀이
def solution(m, n, puddles):
    # dp table 생성 - padding
    dp = [[0 for i in range(m + 1)] for _ in range(n + 1)]
    # 출발지점 및 웅덩이 처리
    dp[1][1] = 1
    for puddle in puddles:
        dp[puddle[1]][puddle[0]] = -1

    # dp table 완성
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 만약 웅덩이라면
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue
            dp[i][j] += dp[i - 1][j] + dp[i][j - 1]

    return dp[n][m] % 1000000007
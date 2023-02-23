N = 4
M = 5

ices = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

# 결과값
result = 0

# delta
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def dfs(r, c):
    # 범위에서 벗어나는 경우 False
    if r < 0 or r >= N or c < 0 or c >= M:
        return False

    # 방문 체크
    if ices[r][c] == 0:
        # 인접한 모든 노드를 방문처리
        ices[r][c] = 1
        for i in range(4):
            dfs(r+dr[i], c+dc[i])
        return True
    return False

for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)

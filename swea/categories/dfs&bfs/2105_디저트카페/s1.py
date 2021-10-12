import sys
sys.stdin = open('input.txt')

# delta
dr = (1, 1, -1, -1)
dc = (1, -1, -1, 1)

# dfs
def dfs(r, c, dir):
    global start, max_val
    if dir == 3 and (r, c) == start:
        # 먹은 디저트 수 세기
        val = 0
        for dessert in desserts:
            if dessert:
                val += 1
        # 최대값 갱신
        if val > max_val:
            max_val = val

    if r < 0 or r >= N or c < 0 or c >= N or desserts[arr[r][c]]:
        return

    desserts[arr[r][c]] = 1

    # 현재 방향으로 이동
    nr1, nc1 = r + dr[dir], c + dc[dir]
    dfs(nr1, nc1, dir)
    # 다음 방향으로 이동
    if dir != 3:
        nr2, nc2 =  r + dr[dir+1], c + dc[dir+1]
        dfs(nr2, nc2, dir+1)

    # 원상복구
    desserts[arr[r][c]] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_val = -1
    desserts = [0] * 101

    for i in range(N-1):
        for j in range(1, N-1):
            start = (i, j)
            dfs(i, j, 0)


    print('#{} {}'.format(tc, max_val))
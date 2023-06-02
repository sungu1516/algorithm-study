# input
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# func
def go(start_r, start_c, cnt, s):
    # 종료조건
    if cnt == k:
        global ans
        if ans < s:
            ans = s
        return

    # 선택
    for r in range(start_r, n):
        start = 0
        if r == start_r:
            start = start_c
        for c in range(start, m):
            # 해당 칸을 선택했다면 continue
            if selected[r][c]:
                continue

            isAble = True   # 선택 가능 여부
            # 기존 선택한 칸들과의 인접여부 확인
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                # 해당 칸이 유효 범위 내에 있을 경우
                if 0 <= nr and nr < n and 0 <= nc and nc < m:
                    # 해당 칸을 선택한 경우
                    if selected[nr][nc]:
                        isAble = False

            if isAble:
                selected[r][c] = 1  # 해당 칸 선택
                go(r, c, cnt + 1, s + arr[r][c])  # 재귀 방문
                selected[r][c] = 0  # 원복

# main
ans = -40000 # 최댓값 초기화
selected = [[0 for _ in range(m)] for _ in range(n)]    # 선택 배열 초기화
# 우하좌상
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

go(0, 0, 0, 0)
print(ans)

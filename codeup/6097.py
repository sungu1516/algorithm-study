# 6097 : [기초-리스트] 설탕과자 뽑기

# 격자판 크기, 막대기 개수
h, w = map(int, input().split())
n = int(input())

# 기본 격자판 만들기
grid = [[0 for _ in range(w)] for _ in range(h)]

# 막대별 정보를 순차적으로 입력받아, 격자판에 표시
for _ in range(n):
    l, d, x, y = map(int, input().split())
    x, y = x - 1, y - 1

    # d = 0 일 때
    if d == 0:
        for i in range(l):
            grid[x][y + i] = 1
    # d = 1
    else:
        for i in range(l):
            grid[x + i][y] = 1

for row in grid:
    print(*row)


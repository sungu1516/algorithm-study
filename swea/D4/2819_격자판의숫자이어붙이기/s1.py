import sys
sys.stdin = open('input.txt')

# delta
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# dfs
def dfs(r, c, cnt, number):
    if cnt == 7:    # 7개 숫자를 붙인 경우
        numbers.add(number) # set에 누적
        return

    # 탐색
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < 4 and 0 <= nc < 4: # 거쳐간 곳으로 돌아갈 수 있으므로, visited 불필요
            dfs(nr, nc, cnt + 1, number + graph[r][c])

T = int(input())
for tc in range(1, T+1):
    graph = [input().split() for _ in range(4)]
    numbers = set() # 탐색한 숫자를 중복없이 저장
    # 2차원 배열의 모든 숫자를 대상으로 시작
    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, '')

    print('#{} {}'.format(tc, len(numbers)))

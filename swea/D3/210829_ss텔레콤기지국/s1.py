import sys
sys.stdin = open('input.txt')
# 델타탐색
di = [-1, 0, 1, 0]      # 상우하좌
dj = [0, 1, 0, -1]

# 함수 정의 - 인덱스 범위 내에 있는지 확인
def is_able(i, j):
    return 0 <= i < N and 0 <= j < N

# 함수 정의 - 2차원 배열을 받아 특정 기지국을 발견했을 때, 커버 가능한 H를 O로 변환하여 표시
def cover(arrs):
    for i in range(N):
        for j in range(N):
            if arrs[i][j] == 'A':   # 만약 기지국의 종류가 A라면
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    if is_able(ni, nj):
                        if arrs[ni][nj] == 'H':     # 만약 상우하좌를 탐색하여 커버가능한 집이 있다면 'O' 로 변환
                            arrs[ni][nj] = 'O'

            elif arrs[i][j] == 'B':     # B라면
                for k in range(4):
                        ni, nj = i, j   # 델타탐색을 각각 두 칸씩 해야하므로 임시변수를 초기화
                        for _ in range(2):  # 두 칸 이동을 위해
                            ni, nj = ni + di[k], nj + dj[k]
                            if is_able(ni, nj):
                                if arrs[ni][nj] == 'H':  # 만약 상우하좌를 탐색하여 커버가능한 집이 있다면 'O' 로 변환
                                    arrs[ni][nj] = 'O'

            elif arrs[i][j] == 'C':     # C라면
                for k in range(4):
                        ni, nj = i, j
                        for _ in range(3):  # 세 칸 이동을 위해
                            ni, nj = ni + di[k], nj + dj[k]
                            if is_able(ni, nj):
                                if arrs[ni][nj] == 'H':  # 만약 상우하좌를 탐색하여 커버가능한 집이 있다면 'O' 로 변환
                                    arrs[ni][nj] = 'O'

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 배열의 크기
    map = [list(input()) for _ in range(N)]     # 기지국, 집의 위치가 표현된 2차원 배열

    cover(map)      # 함수를 호출하여, 기지국이 커버하는 H를 O로 변환
    # 남은 H의 개수를 세어준다.
    ans = 0
    for row in map:
        ans += row.count('H')

    print('#{} {}'.format(tc, ans))





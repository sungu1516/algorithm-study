import sys
sys.stdin = open('input.txt')
# 탐색
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

# 함수정의
def is_able(*args):
    for idx in args:
        if idx < 0 or idx >= N:
            return False
    return True

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())        # 보드의 한 변의 길이 N, 돌을 놓는 횟수 M
    # 보드 초기화
    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1] = 2
    board[N // 2][N // 2] = 2
    board[N // 2 - 1][N // 2] = 1
    board[N // 2][N // 2 - 1] = 1

    for _ in range(M):      # 정해진 횟수만큼 돌을 놓기
        i, j, stn = map(int, input().split())       # 돌을 놓을 좌표, 돌의 색 (1 or 2)
        i, j = i - 1, j - 1
        board[i][j] = stn       # 입력값으로 받은 위치에 돌 삽입

        # 델타탐색을 통해 적절한 위치를 찾아 돌 변경
        for k in range(8):
            ni, nj = i + di[k], j + dj[k]

            while is_able(ni, nj) and board[ni][nj] != 0:

                if board[ni][nj] == stn:    # 조건 내에서 같은 돌을 발견한다면
                    break
                ni, nj = ni + di[k], nj + dj[k]

            if is_able(ni, nj) and board[ni][nj] != 0: # 중간에 같은 돌을 찾은 경우
                ni, nj = ni - di[k], nj - dj[k]
                while ni != i or nj != j:
                    board[ni][nj] = stn
                    ni, nj = ni - di[k], nj - dj[k]


        # 흑돌, 백돌 개수
        black = 0
        white = 0
        for row in board:
            black += row.count(1)
        for row in board:
            white += row.count(2)

    print('#{} {} {}'.format(tc, black, white))
import sys
sys.stdin = open('input.txt', encoding='UTF-8')

di = [1, 1]    # 왼오, 오왼
dj = [1, -1]

# 함수
def is_omok(arrs):
    cnt = 0

    # 가로세로 탐색
    for i in range(N+2):
        # 가로방향 탐색
        for j in range(N+2):
            if arrs[i][j] == 'o':
                cnt += 1
            else:
                if cnt >= 5:
                    return 'YES'
                cnt = 0     # cnt 초기화

        # 세로방향 탐색
        for j in range(N+2):
            if arrs[j][i] == 'o':
                cnt += 1
            else:
                if cnt >= 5:
                    return 'YES'
                cnt = 0     # cnt 초기화

    cnt = 0
    for i in range(N+2):
        for j in range(N+2):
            for k in range(2):
                ni, nj = i, j
                while 0 <= ni < N + 2 and 0 <= nj < N + 2:
                    test = arrs[nj][ni]
                    if arrs[nj][ni] == 'o':
                        cnt += 1
                    else:
                        if cnt >= 5:
                            return 'YES'
                        cnt = 0  # cnt 초기화
                    ni, nj = ni + di[k], nj + dj[k]



    return 'NO'     # 만약 탐색 중 오목을 발견하지 못한다면

T = int(input())
for tc in range(1, T + 1):
    N = int(input())        # 오목판 크기
    board = [['.']*(N+2)] + [['.'] + list(input()) + ['.'] for _ in range(N)] + [['.']*(N+2)]       # 패딩

    print('#{} {}'.format(tc, is_omok(board)))
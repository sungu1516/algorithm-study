import sys
# input을 파일로 받아오는 설정
sys.stdin = open('input.txt')

T = int(input())

for _ in range(1, T + 1):
    N = int(input())
    # 빈 2차원 리스트 만들기
    arrs = [[0] * N for _ in range(N)]

    # 델타 탐색 - 우, 하, 좌, 상 순으로 이동
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    i = k = 0
    j = -1

    # 입력될 숫자 초기화
    num = 1

    while num <= N*N:
        # 다음 이동 좌표가 유효한 범위 내에 있는지 확인
        i_temp = i + di[k]
        j_temp = j + dj[k]

        # 다음 좌표가 유효한 범위 내에 있다면 실제 좌표인 i, j 최신화
        if i_temp < N and j_temp < N and arrs[i_temp][j_temp] == 0:
            i = i_temp
            j = j_temp
            # 배열에 숫자 넣어주기
            arrs[i][j] = num
            num += 1
        else:
            # 유효 범위를 벗어나거나 다음 위치에 숫자가 존재하는 경우, 방향을 변경
            k = (k + 1) % 4

    print('#{}'.format(_))
    for arr in arrs:
        print(*arr)

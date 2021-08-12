import sys
# input을 파일로 받아오는 설정
sys.stdin = open('input.txt')

# delta 탐색을 위한 리스트
di = [-1, 0, 0]
dj = [0, 1, -1]

for _ in range(1, 11):
    # test case 번호
    N = int(input())

    # 입력값으로 2차원 배열 만들기
    arrs = [[0] + list(map(int, input().split())) + [0] for _ in range(100)] # 이후 인덱스 이동의 편의를 위해 0으로 padding

    # 시작 좌표(=2) 및 델타탐색을 위한 k 초기화
    j = arrs[99].index(2) # 2는 항상 마지막 행에 존재하므로, index() 를 통해 2의 위치를 저장
    i = 100 # 이후 인덱스 이동의 편의를 위해
    k = 0

    # 좌표 이동 시작
    while i > 0: # 가장 위쪽의 리스트에 도달하면 반복문 탈출
        i += di[k]
        j += dj[k]

        # 도착한 자리는 0으로 변환해주기 (이후 조건을 통해 이동하기 위함)
        arrs[i][j] = 0

        if arrs[i][j + 1] == 1: # 현재 위치에서 오른쪽에 1이 존재한다면
            k = 1 # 방향 변환 (우로 이동)
        elif arrs[i][j - 1] == 1: # 현재 위치에서 왼쪽에 1이 존재한다면
            k = 2 # 방향 변환 (좌로 이동)
        else:
            k = 0 # 방향 변환 (위로 이동)

    print('#{} {}'.format(_, j - 1)) # 위에서 패딩한 것을 고려하여 -1 하고 출력
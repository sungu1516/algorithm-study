import sys
sys.stdin = open('input.txt')

# 필요 함수 정의
def is_duplicate(arrs):
    # 가로줄 확인
    for i in range(0, 9):
        cnts = [0]*10 # 각 숫자의 개수를 담을 리스트 초기화
        for j in range(0, 9):
            cnts[arrs[i][j]] += 1
        for cnt in cnts[1:]:
            if cnt != 1: # 만약 개수가 1이 아닌 경우가 있을 경우
                return 0

    # 세로줄 확인
    for j in range(0, 9):
        cnts = [0]*10  # 각 숫자의 개수를 담을 리스트 초기화
        for i in range(0, 9):
            cnts[arrs[i][j]] += 1
        for cnt in cnts[1:]:
            if cnt != 1:  # 만약 개수가 1이 아닌 경우가 있을 경우
                return 0

    # 작은 격자 확인
    for i_1 in range(0, 7, 3):
        for j_1 in range(0, 7, 3):
            cnts = [0] * 10  # 각 숫자의 개수를 담을 리스트 초기화
            for i_2 in range(i_1, i_1+3):
                for j_2 in range(j_1, j_1 + 3):
                    cnts[arrs[i_2][j_2]] += 1
            for cnt in cnts[1:]:
                if cnt != 1:  # 만약 개수가 1이 아닌 경우가 있을 경우
                    return 0

    # 모든 탐색에서 중복되는 숫자가 없을 경우
    return 1

T = int(input())

for _ in range(1, T + 1):
    arrs = [list(map(int, input().split())) for _ in range(9)]
    print('#{} {}'.format(_, is_duplicate(arrs)))
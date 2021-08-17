import sys
sys.stdin = open('input.txt')

# 필요 함수 정의
def is_duplicate(arrs):
    # 가로줄 확인
    for i in range(0, 9):
        for j in range(0, 8):
            if arrs[i][j] == arrs[i][j + 1]: # 만약 같은 수가 존재한다면
                return 0

    # 세로줄 확인
    for j in range(0, 9):
        for i in range(0, 8):
            if arrs[i][j] == arrs[i + 1][j]:
                return 0

    # 작은 격자 확인
    for i_1 in range(0, 7, 3):
        for j_1 in range(0, 7, 3):
            temp = 0 # 비교 값을 임시적으로 저장(다음 줄로 넘어갈 때 활용 가능)
            for i_2 in range(i_1, i_1+3):
                for j_2 in range(j_1, j_1 + 3):
                    if temp == arrs[i_2][j_2]:
                        return 0
                    else:
                        temp = arrs[i_2][j_2]

    # 모든 탐색에서 동일한 경우가 없을 때
    return 1

T = int(input())

for _ in range(1, T + 1):
    arrs = [list(map(int, input().split())) for _ in range(9)]

    print('#{} {}'.format(_, is_duplicate(arrs)))
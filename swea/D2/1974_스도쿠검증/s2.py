import sys
sys.stdin = open('input.txt')

def check(): # 행 검사와 열 검사를 동시에
    for i in range(9):
        # 숫자 사용을 체크를 위한
        row = [0] * 10
        col = [0] * 10

        for j in range(9):
            # 행을 검사
            num_row = sudoku[i][j]
            # 열을 검사
            #######################
            num_col = sudoku[j][i]

            # 이미 사용한 숫자라면 멈춰!
            if row[num_row]: return 0
            if col[num_col]: return 0

            row[num_row] = 1
            row[num_col] = 1

            ################################
            # 3x3 검사도 한 번에 처리해보자!!
            if i % 3 == 0 and j % 3 == 0:
                square = [0] * 10
                for r in range(i, i+3):
                    for c in range(j, i+3):
                        num = sudoku[r][c]
                        if square[num]: return 0 # 중복된 숫자가 나온다면 멈춰!
                        square[num] = 1

    return 1


T = int(input())

for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    print('#{} {}'.format(tc, check()))

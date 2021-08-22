import sys
# input을 파일로 받아오는 설정
sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc = int(input()) # test case number
    arrs = [list(map(int, input().split())) for _ in range(100)]
    # 대각선 합을 먼저 구해 최댓값 초기화
    total_right = total_left = 0
    for i in range(100):
        total_right += arrs[i][i]
        total_left += arrs[i][100 - 1 - i]
    max_val = total_right if total_right > total_left else total_left
    # 모든 행, 열을 탐색하며 최댓값 갱신
    for i in range(100):
        # 행의 합
        total_row = sum(arrs[i])
        if max_val < total_row:
            max_val = total_row
        # 열의 합
        total_col = 0
        for j in range(100):
            total_col += arrs[j][i]
        if max_val < total_col:
            max_val = total_col
    print('#{} {}'.format(tc, max_val))
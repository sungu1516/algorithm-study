import sys
sys.stdin = open('input.txt')

def rotate(arrs):
    n = len(arrs)
    arrs_90 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arrs_90[i][j] = arrs[n-1-j][i]
    return arrs_90

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 행렬 크기
    A = [list(input().split()) for _ in range(N)]
    result_90 = rotate(A)  # 90도 회전한 결과를 변수에 저장
    result_180 = rotate(result_90)  # 180 도 회전한 결과를 변수에 저장
    result_270 = rotate(result_180)  # 270 도 회전한 결과를 변수에 저장
    print('#{}'.format(tc))
    for i in range(N):
        print(''.join(result_90[i]), end=' ')
        print(''.join(result_180[i]), end=' ')
        print(''.join(result_270[i]))

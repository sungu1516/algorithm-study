import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(1, T + 1):
    N = int(input()) # 행렬 크기

    arrs = [''.join(input().split()) for _ in range(N)]

    # 90도 회전한 결과
    arrs_90 = []
    for a_tuple in zip(*arrs):
        temp = ''.join(a_tuple)[::-1]
        arrs_90.append(temp)

    # 180도 회전한 결과
    arrs_180 = []
    for i in range(N-1, -1, -1):
        arrs_180.append(arrs[i][::-1])

    # 270도 회전한 결과
    arrs_270 = []
    for a_tuple in zip(*arrs_180):
        temp = ''.join(a_tuple)[::-1]
        arrs_270.append(temp)

    # 모든 결과를 하나의 리스트에 담기
    result = []
    result.extend([arrs_90, arrs_180, arrs_270])

    # 결과 출력
    print('#{}'.format(_))
    for j in range(N):
        for i in range(3):
            print(result[i][j], end = ' ')
        print()
import sys
sys.stdin = open('input.txt')

T = 1
for _ in range(1, T+1):
    tc = input()
    arrs = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]
    # 출발위치 초기화
    i = 99
    j = arrs[99].index(2)

    while i > 0:
        i -= 1

        if arrs[i][j-1] == 1:
            while arrs[i][j-1] == 1:
                j -= 1

        elif arrs[i][j+1] == 1:
            while arrs[i][j+1] == 1:
                j += 1

    print('#{} {}'.format(tc, j-1))
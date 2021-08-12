import sys
# input을 파일로 받아오는 설정
sys.stdin = open('input.txt')

T = int(input())

for _ in range(1, T + 1):
    N, M = map(int, input().split())
    arrs = [list(map(int, input().split())) for _ in range(N)]

    # 최댓값 초기화
    max_val = 0

    # 반복문을 통해 모든 영역을 훑는다.
    for i_1 in range(N-M+1):
        for j_1 in range(N-M+1):
            total = 0 # 한 번의 파리채로 잡을 수 있는 파리 수 초기화
            for i_2 in range(i_1, i_1 + M):
                for j_2 in range(j_1, j_1 + M):
                    total += arrs[i_2][j_2]
                    if max_val < total:
                        max_val = total

    print('#{} {}'.format(_, max_val))



import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for _ in range(1, T + 1):
    tc = int(input())
    scores = list(map(int, input().split()))
    # 각 점수를 인덱스로, 빈도를 값으로 갖는 배열을 만든다.
    cnts = [0] * 101
    for score in scores:
        cnts[score] += 1

    # 최대 빈도를 갖는 점수를 구하기
    max_idx = 0
    for idx in range(1, 101):
        if cnts[max_idx] <= cnts[idx]:
            max_idx = idx
    print('#{} {}'.format(tc, max_idx))
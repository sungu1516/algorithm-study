import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 카드의 개수
    arr = [int(x) for x in input()]
    # counts 배열 만들어주기
    counts = [0] * 10
    for i in range(N):
        counts[arr[i]] += 1

    # counts 배열의 max_idx(가장 많은 카드의의 숫자) 구하기
    max_idx = 0
    for i in range(1, len(counts)):
        if counts[max_idx] <= counts[i]:
            max_idx = i

    print('#{} {} {}'.format(tc, max_idx, counts[max_idx]))
import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    corrider = [0] * 201

    for _ in range(N):
        start, end = map(lambda x: (int(x)+1)//2, input().split())
        if start > end:
            start, end = end, start
        for i in range(start, end+1):
            corrider[i] += 1

    max_val = 1
    for val in corrider:
        if max_val < val:
            max_val = val
    print('#{} {}'.format(tc, max_val))
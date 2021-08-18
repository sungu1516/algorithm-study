import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for _ in range(1, T + 1):
    N = int(input())
    arr = list(map(abs, map(int, (input().split())))) # abs 처리를 입력값 받아오면서 바로 해주기
    min_val = 100000  # min_val 초기화

    for elem in arr:
        if min_val > elem:
            min_val = elem

    print('#{} {} {}'.format(_, min_val, arr.count(min_val)))
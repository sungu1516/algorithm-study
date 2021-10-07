import sys
sys.stdin = open('input.txt')

def dfs(stop, cnt):
    global min_cnt

    if cnt >= min_cnt:
        return
    if stop + arr[stop] >= N - 1:
        if cnt < min_cnt:
            min_cnt = cnt

    for i in range(stop + 1, stop + arr[stop] + 1):
        dfs(i, cnt + 1)

T = int(input())
for tc in range(1, T+1):
   arr = list(map(int, input().split()))
   N = arr.pop(0)
   min_cnt = N - 2

   dfs(0, 0)

   print('#{} {}'.format(tc, min_cnt))
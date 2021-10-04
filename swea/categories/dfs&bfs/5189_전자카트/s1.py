import sys
sys.stdin = open('input.txt', 'r')

def dfs(row,  consum):
    global min_consum

    if consum > min_consum:
        return

    if visited.count(1) == N:
        consum += arr[row][0]
        if consum < min_consum:
            min_consum = consum

    for i in range(N):
        if arr[row][i] != 0 and not visited[i]:
            visited[i] = 1
            dfs(i, consum + arr[row][i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    visited[0] = 1
    min_consum = 100 * N

    dfs(0, 0)

    print('#{} {}'.format(tc, min_consum))
import sys
sys.stdin = open('input.txt', 'r')

def solve(k):
    global ans
    if k == N:
        val = 1
        for i in range(N):
            val *= mat

    else:
        pass

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    mat = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    perm = [x for x in range(N)]
    solve(0)
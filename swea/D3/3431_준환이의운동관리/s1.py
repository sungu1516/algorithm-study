import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())

for tc in range(1, T + 1):
    L, U, X = map(int, input().split())
    if X < L:
        result = L - X
    elif L <= X <= U:
        result = 0
    else:
        result = -1
    print('#{} {}'.format(tc, result))
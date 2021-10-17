import sys
sys.stdin = open('input.txt')

# union
def union(n1, n2):
    p[find_set(n2)] = find_set(n1)

# find_set
def find_set(n):
    while n != p[n]:
        n = p[n]
    return n

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # make-set
    p = list(range(N+1))
    # union
    for _ in range(M):
        p1, p2 = map(int, input().split())
        union(p1, p2)

    # 무리의 개수 세기
    represent = set()
    for i in range(1, N+1):
        represent.add(find_set(i))

    print('#{} {}'.format(tc, len(represent)))

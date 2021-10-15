import sys
sys.stdin = open('input.txt')

# find_set
def find_set(x):
    while p[x] != x:
        x = p[x]
    return x

# union
def union(x, y):
    p[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())    # V: 마지막 번호 / E: 간선의 수

    edges = [list(map(int, input().split())) for _ in range(E)]

    edges.sort(key=lambda x:x[2])

    p = list(range(V+1))    # make-set 과정

    cnt = 0 # 간선을 선택한 횟수
    ans = 0 # 가중치를 더한 값
    idx = 0 # edges 인덱스

    while cnt < V:
        n1 = edges[idx][0]
        n2 = edges[idx][1]

        # 노드의 대표가 다를 때
        if find_set(n1) != find_set(n2):
            union(n1, n2)
            cnt += 1
            ans += edges[idx][2]

        idx += 1

    print('#{} {}'.format(tc, ans))
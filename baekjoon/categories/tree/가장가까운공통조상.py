def find_ancester(n1, n2):
    if n1:
        tmp = n2
        while n2:
            if n1 == n2:
                print(n1)
                return

            n2 = parent[n2]

        find_ancester(parent[n1], tmp)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    parent = [0] * (N+1)    # 자식의 노드를 인덱스로, 부모노드를 원소로 갖는 배열

    for _ in range(N-1):
        p, c = map(int, input().split())
        parent[c] = p

    node1, node2 = map(int, input().split())  # 공통의 조상을 찾을 두 노드

    find_ancester(node1, node2)
from collections import deque

# parent 배열을 완성하는 함수 정의 (BFS)
def make_parent(n):
    parent = [0] * (N + 1)  # 배열의 인덱스를 노드 값으로, 배열의 원소를 부모노드의 값으로 갖는 배열
    parent[1] = 1  # 1번 노드의 부모로 임의의 값(1)을 넣어준다.
    que = deque([n])

    while que:
        curr = que.popleft()
        for ve in tree[curr]:
            if not parent[ve]:
                que.append(ve)
                parent[ve] = curr

    for i in range(2, N + 1):
        print(parent[i])

N = int(input())    # 노드의 개수

tree = [[] for _ in range(N+1)]

# 입력값 받아 트리 완성
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)     # 양방향으로 삽입해준다.

# 함수 호출 & 출력
make_parent(1)




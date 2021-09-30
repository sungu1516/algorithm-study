N = int(input())    # 노드의 개수
parent = [0] * (N + 1)  # 배열의 인덱스를 노드 값으로, 배열의 원소를 부모노드의 값으로 갖는 배열
for _ in range(N-1):
    par, ch = map(int, input().split())
    parent[ch] = par

print(parent)
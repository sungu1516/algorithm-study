from collections import deque

# bfs 함수
def bfs(graph, start):
    _visited = [0] * (N+1)
    # 시작지점 queue 에 삽입
    queue = deque([start])
    # 시작지점 방문처리
    _visited[start] = 1
    # queue 가 빌 때까지 실행
    while queue:
        curr = queue.popleft()      # queue 의 맨 앞 원소를 꺼낸다.
        print(curr, end=' ')
        for ve in graph[curr]:      # 인접노드 순회
            if not _visited[ve]:
                queue.append(ve)    # queue 삽입
                _visited[ve] = 1     # 방문처리

# dfs 함수
def dfs(graph, start, _visited):
    # 방문처리
    _visited[start] = 1
    print(start, end=' ')
    # 정점 번호가 작은 것부터 방문
    for ve in graph[start]:     # 인접노드 순회
        if not _visited[ve]:
            dfs(graph, ve, _visited)     # 다음 방문 노드와, 현재까지 방문 기록이 담긴 _visited 배열을 인자로 재귀호출

# 입력받기
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)      # 간선은 양방향이다.
    graph[node2].append(node1)

for _list in graph:     # 작은 정점부터 방문하기 위해 정렬작업
    _list.sort()

# 함수 실행
visited = [0] * (N+1)
dfs(graph, V, visited)
print()
bfs(graph, V)
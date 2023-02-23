from collections import deque

def bfs(graph, start, visited):
    # que 초기화
    que = deque([start])
    # 방문 노드 방문처리
    visited[start] = True
    # que가 빌 때까지 반복
    while que:
        # 큐위 top 원소 뽑기
        v = que.popleft()
        print(v, end=' ')
        # 방문 노드의 모든 인접 노드를 순회
        for i in graph[v]:
            # 아직 방문하지 않은 인접 노드를 모두 큐에 삽입하고 방문처리
            if not visited[i]:
                que.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
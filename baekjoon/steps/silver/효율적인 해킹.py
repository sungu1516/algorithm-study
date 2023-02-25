import sys
from collections import deque
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)

def bfs(start):
    cnt = 0
    # que에 시작노드 삽입
    que = deque([start])
    # 방문기록
    visited = [0 for _ in range(n + 1)]
    # 방문 처리
    visited[start] = 1
    # 근접 노드 방문
    while que:
        v = que.popleft()
        for i in graph[v]:
            if not visited[i]:
                cnt += 1
                visited[i] = 1
                que.append(i)

    return cnt

result = []
max_cnt = 0
# bfs 실행
for i in range(1, m+1):
    cnt = bfs(i)
    if cnt == max_cnt:
        result.append(i)
    if cnt > max_cnt:
        result.clear()
        result.append(i)
        max_cnt = cnt


# 출력
for res in result:
    print(res, end=' ')
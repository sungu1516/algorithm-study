import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# input
n, m  = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# main
# dfs
def dfs(v, visited):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)

ans = 0
visited = [0] * (n + 1)
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, visited)
        ans += 1

print(ans)
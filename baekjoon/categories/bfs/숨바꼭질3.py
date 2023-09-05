from collections import deque
# input
n, k = map(int, input().split())
max = 100001

# function
def bfs(start, target, dist):
    # init
    q = deque([start])
    dist[start] = 0

    while q:
        loc = q.popleft()
        if loc == target:
            print(dist[target])
            break
        if 0 <= loc - 1 < max and dist[loc - 1] == -1:
            dist[loc - 1] = dist[loc] + 1
            q.append(loc - 1)
        if 0 <= loc * 2 < max and dist[loc * 2] == -1:
            dist[loc * 2] = dist[loc]
            q.appendleft(loc * 2)
        if 0 <= loc + 1 < max and dist[loc + 1] == -1:
            dist[loc + 1] = dist[loc] + 1
            q.append(loc + 1)



# main
dist = [-1] * max

bfs(n, k, dist)
# func
def dfs(depth, r):
    global ans

    if depth == r:
        print(result)

    for i in range(len(arr)):
        if not visited[i]:
            result[depth] = arr[i]
            visited[i] = 1
            dfs(depth + 1, r)
            visited[i] = 0

# main
n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
arr = list(range(n))
result = [0 for _ in range(n)]
visited = [0 for _ in range(n)]
ans = 1e9

dfs(0, n)

print(ans)
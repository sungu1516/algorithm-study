# func
def dfs(depth, start, r):
    if depth == r:
        print(*result)
        return

    for i in range(start, len(s)):
        result.append(s[i])
        dfs(depth + 1, i + 1, r)
        result.pop()

# main
while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    s = arr[1:]
    if k == 0:
        break
    result = []
    dfs(0, 0, 6)
    print()
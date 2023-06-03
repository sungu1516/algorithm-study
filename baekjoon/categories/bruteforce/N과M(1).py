# input
n, m = map(int, input().split())

# func
def perm(idx, n, m):
    # 종료 조건
    if idx > m:
        print(*arr[1:])
        return

    for i in range(1, n + 1):
        if visited[i]:
            continue
        visited[i] = 1  # 방문처리
        arr[idx] = i

        perm(idx + 1, n, m)  # 재귀적 방문

        # 원복
        visited[i] = 0

# main
arr = [0 for _ in range(m + 1)]
visited = [0 for _ in range(n + 1)]

perm(1, n, m)
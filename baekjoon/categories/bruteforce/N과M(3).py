# input
n, m = map(int, input().split())

# func
def perm(idx, n, m):
    # 종료 조건
    if idx > m:
        print(*arr[1:])
        return

    for i in range(1, n + 1):
        arr[idx] = i
        perm(idx + 1, n, m)  # 재귀적 방문

# main
arr = [0 for _ in range(m + 1)]

perm(1, n, m)
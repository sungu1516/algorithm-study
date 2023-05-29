# input
t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    i = x

    while i < m*n:
        if i % n == y:
            print(i + 1)
            break
        i += m
    else:
        print(-1)
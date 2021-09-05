def return_min(n):
    for n in range(N // 3 + 1):
        for m in range(N // 3 + 1):
            if N == (3 * n + 5 * m):
                return n + m

    return -1

N = int(input())

ans = return_min(N)
print(ans)
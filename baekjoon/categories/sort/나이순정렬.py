N = int(input())

arr = [tuple(input().split()) for _ in range(N)]
arr = sorted(arr, key = lambda arr: int(arr[0]))

for _tuple in arr:
    print(*_tuple)
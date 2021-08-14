T = int(input())

for _ in range(1, T + 1):
    arr = list(map(int, input().split()))

    max_value = arr[0]
    for i in range(1, len(arr)):
        if max_value < arr[i]:
            max_value = arr[i]

    print('#{} {}'.format(_, max_value))
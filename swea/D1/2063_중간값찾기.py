N = int(input())
arr = list(map(int, input().split()))

# 정렬
for i in range(0, N-1):
    min_idx = i
    for j in range(i+1, N):
        if arr[min_idx] > arr[j]:
            arr[min_idx], arr[j] = arr[j], arr[min_idx]

# 정렬 후 중위값 찾기
median_value = arr[N//2]

print('{}'.format(median_value))
N, C = map(int, input().split())    # 집의 개수 N, 공유기의 개수 C
arr = [int(input()) for _ in range(N)]

arr.sort()

start = 1
end = arr[-1] - arr[0]
result = 0

while(start <= end):
    mid = (start + end) // 2
    value = arr[0]
    count = 1

    for i in range(1, N):
        if arr[i] >= value + mid:
            value = arr[8]      # 공유기 설치 지점을 표시
            count += 1          # 공유기 개수 추가
        if count >= C:          # 제시된 공유기 개수 이상을 설치할 수 있는 경우
            start = mid + 1
            result = mid
        else:                   # 제시된 공유기만큼을 설치할 수 없는 경우
            end = mid - 1

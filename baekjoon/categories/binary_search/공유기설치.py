N, C = map(int, input().split())    # 집의 개수 N, 공유기의 개수 C
arr = [int(input()) for _ in range(N)]

# 이진탐색을 위한 정렬
arr.sort()

start, end = 1, arr[-1]  - arr[0]  # 집 간 최대, 최소 거리 구하기
result = 0      # 인접한 두 공유기의 최대거리 초기화

while start <= end:     # 탐색 시작 지점과 종료지점이 같거나 시작지점이 더 커질 때까지
    mid = (start + end) // 2    # 이진탐색 - 최소거리를 최대거리의 2로 나눠 탐색 시작
    installed = arr[0]          # 마지막 공유기 설치 지점을 기록  - 배열의 첫 원소는 반드시 들어갈 수 있음
    cnt = 1    # 공유기를 설치한 집의 수

    for i in range(1, N):     # 탐색을 시작할 지점부터 끝까지
        if arr[i] >= mid + installed:   # 만약 마지막 설치 지점 + 간격보다 좌표가 크다면
            installed = arr[i]      # 공유기 설치 지점 최신화
            cnt += 1

    if cnt >= C:            # 특정 간격으로 설치했을 때, 주어진 개수보다 공유기를 많이 설치했다면
        start = mid + 1     # 간격을 늘리기 위해 최소간격을 변경
        result = mid        # 최대 간격을 갱신해준다.

    else:       # 공유기를 조건만큼 설치할 수 없을 때
        end = mid - 1       # 최대 간격을 줄인다.

print(result)
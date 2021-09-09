N, C = map(int, input().split())    # 집의 개수 N, 공유기의 개수 C
arr = [int(input()) for _ in range(N)]
# 집의 위치 1로 표시
home = [0] * (max(arr)+1)
for i in arr:
    home[i] = 1

def binary_search(start, end):
    middle = (start + end) // 2

    if start == middle:                 # 만약 가운데 지점이 없고, 1을 못찾은 경우
        return 0

    if home[middle] == 1:               # 1을 찾은 경우 - 해당 인덱스 리턴
        return middle
    else:
        p1 = binary_search(start, middle)    # 중간점의 왼쪽 탐색
        p2 = binary_search(middle, end)      # 중간점의 오른쪽 탐색

        return p1 if abs(p1-middle) < abs(p2-middle) else p2 # middle과 가까운 놈을 출력


start_p, end_p = min(arr), max(arr)

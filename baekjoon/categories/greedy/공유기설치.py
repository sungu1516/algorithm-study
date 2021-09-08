N, C = map(int, input().split())    # 집의 개수 N, 공유기의 개수 C
home = [int(input()) for _ in range(N)]

def binary_search(start, end):
    middle = (start + end) // 2

    if start == middle:                 # 만약 가운데 지점이 없고, 1을 못찾은 경우
        return 0

    if home[middle] == 1:               # 1을 찾은 경우 - 해당 인덱스 리턴
        return middle
    else:
        binary_search(start, middle)    # 중간점의 왼쪽 탐색
        binary_search(middle, end)      # 중간점의 오른쪽 탐색
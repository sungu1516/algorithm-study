import sys
# input을 파일로 받아오는 설정
sys.stdin = open('input.txt')

T = int(input())

for _ in range(1, T + 1):
    N = int(input()) # 숫자의 개수
    arr = list(map(int, input().split()))

    # 선택 정렬
    for i in range(0, N-1):
        min_idx = i
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print('#{}'.format(_), *arr)
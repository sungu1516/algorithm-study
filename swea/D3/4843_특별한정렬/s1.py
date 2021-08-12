import sys
# input을 파일로 받아오는 설정
sys.stdin = open('input.txt')

T = int(input())

for _ in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 선택 정렬 사용
    for i in range(0, len(arr)-1):
        # 최대, 최솟값의 인덱스를 초기화
        max_idx = min_idx = i # 탐색 구간의 첫 번째 값을 min & max idx 로 지정

        # 탐색 시작 인덱스가 짝수라면 최댓값을 찾는다
        if i % 2 == 0:
            for j in range(i+1, len(arr)):
                if arr[max_idx] < arr[j]:
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i] # 탐색 시작 위치와 최댓값이 있는 위치 변경

        # 시작 인덱스가 홀수라면 최솟값을 찾는다.
        else:
            for j in range(i+1, len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i] # 탐색 시작 위치와 최솟값이 있는 위치 변경

    print('#{}'.format(_), *arr[:10]) # 10개까지만 출력
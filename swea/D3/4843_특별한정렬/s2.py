import sys
# input을 파일로 받아오는 설정
sys.stdin = open('input.txt')

T = int(input())

for _ in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 결과값을 저장할 빈 리스트
    sorted_arr = []

    # max(), min(), remove() 활용
    for i in range(len(arr)):
        if i % 2: # 최솟값을 탐색하는 경우
            min_val = min(arr)
            sorted_arr.append(min_val) # 기존 arr 의 최솟값을 새로운 리스트에 추가
            arr.remove(min_val) # 다음 탐색을 위해 기존 arr 에서 해당값 제거
        else:
            max_val = max(arr) # 최댓값을 탐색하는 경우
            sorted_arr.append(max_val) # 기존 arr 의 최댓값을 새로운 리스트에 추가
            arr.remove(max_val) # 다음 탐색을 위해 기존 arr 에서 해당값 제거

    print('#{}'.format(_), *sorted_arr[:10])
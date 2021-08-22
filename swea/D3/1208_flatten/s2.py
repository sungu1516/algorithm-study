import sys
sys.stdin = open('input.txt')

# 함수정의
def return_diff():
    max_val = 0
    min_val = 100
    for val in arr:
        if max_val < val:
            max_val = val
        if min_val > val:
            min_val = val
    return max_val - min_val

for tc in range(1, 11):
    N = int(input()) # 덤프 횟수
    arr = list(map(int, input().split()))

    # 반복문 - 평탄화 작업 : N번만큼 반복
    for _ in range(N):
        ## 1) max, min_idx 구하기
        max_idx = 0
        min_idx = 0
        for i in range(1, 100):
            if arr[max_idx] < arr[i]:
                max_idx = i
            if arr[min_idx] > arr[i]:
                min_idx = i

        ## 2) 평탄화 작업 실시
        arr[max_idx] -= 1
        arr[min_idx] += 1

        ## 3) 주어진 횟수 이전에 완료되는 경우
        if return_diff() <= 1:
            break

    # 작업 종료 후 높이 차 출력
    ans = return_diff()
    print('#{} {}'.format(tc, ans))
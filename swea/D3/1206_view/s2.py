import sys
sys.stdin = open('input.txt')
T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0 # 조망권 확보 세대 수 초기화

    for i in range(2, N-2):
        # 중앙의 높이 - arr[i] 를 제외한 최댓값 구하기
        max_val = 0
        for j in range(i-2, i+3):
            if j != i:
                if max_val < arr[j]:
                    max_val = arr[j]

        # arr[i] 과의 비교 후 count
        if arr[i] > max_val:
            cnt += arr[i] - max_val # 세대 수 더해주기

    print('#{} {}'.format(tc, cnt))
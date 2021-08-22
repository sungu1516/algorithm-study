import sys
sys.stdin = open('input.txt')

# test case
T = int(input())

for _ in range(1, T+1):
    N = int(input())
    arr = [2, 3, 5, 7, 11]

    # a,b,c,d,e 값을 담을 리스트 초기화
    counts = [0] * 5

    i = 0
    # 반복문을 통해 결과값을 저장
    while i < len(arr):
        if N % arr[i] == 0:
            counts[i] += 1
            N //= arr[i]
            continue
        i += 1

    # 결과 출력
    print('#{} {} {} {} {} {}'.format(_, *counts))
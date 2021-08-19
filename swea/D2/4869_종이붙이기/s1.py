import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# DP 로 접근
arr = [0] * 31  # N 별로 값이 담길 배열 초기화 : N <= 300 이므로
arr[0] = 0
arr[1] = 1
arr[2] = 3  # N=20 까지의 결과를 배열에 담아둠

T = int(input())

for _ in range(1, T + 1):
    n = int(input()) // 10 # 인덱싱으로 배열을 채우기 위해 n을 10으로 나눠줌

    if arr[n] == 0: # 기존 배열에 해당 인덱스의 값이 없는 경우에만 반복문 실행
        for i in range(3, n + 1): # 입력값까지 배열을 완성
            arr[i] = arr[i-1] + arr[i-2] * 2 # 점화식  - n-1 의 경우에 수에 1*2 를 오른쪽에 하나씩 더하고, n-2의 경우에 2*(1*2), 2*2 를 각각 더하는 경우를 합

    print('#{} {}'.format(_, arr[n]))

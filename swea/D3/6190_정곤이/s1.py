import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 함수 정의
def is_monotonic(n):    # 정수를 넣으면 단조증가 여부를 리턴
    if n // 10 == 0:     # 일의자리인 경우
        return True

    n1 = n % 10         # 일의자리 수
    n2 = (n//10) % 10   # 십의자리 수

    if n1 < n2:         # 단조증가가 아닌 경우
        return False

    # 만약 확인한 부분까지 단조증가인 경우
    return is_monotonic(n//10)



T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 수열의 길이
    numbers = list(map(int, input().split())) # 수열

    # brute force
    max_value = -1      # 만약 단조증가 수가 없다면 -1를 리턴하기 위함
    for i in range(N-1):
        for j in range(i+1, N):
            value = numbers[i] * numbers[j]
            if is_monotonic(value):     # 단조증가하는 수인 경우
                if max_value < value:   # 최댓값보다 큰 경우
                    max_value = value

    print('#{} {}'.format(tc, max_value))


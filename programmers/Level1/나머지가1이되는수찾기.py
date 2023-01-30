def solution(n):
    # n-1 의 약수 중 최소값을 구한다.
    target_n = n - 1
    for number in range(2, target_n // 2 + 1):
        if target_n % number == 0:
            return number

    return target_n
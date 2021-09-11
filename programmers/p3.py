import math

# 정수 n을 k진수 (문자열 형태)로 변환하여 반환하는 함수
def transfer(N, K):
    result = ''
    while N:
        N, remain = divmod(N, K)
        result = str(remain) + result
    return result

# 소수 판별 함수
def is_prime(N):
    if N == 1:
        return False
    for num in range(2, int(math.sqrt(N)) + 1):
        if N % num == 0:
            return False
    return True

def process(N):     # '' 과 같은 문자열은 1로 변환하도록 함
    if N:
        return int(N)
    else:
        return 1

def solution(n, k):
    cnt = 0
    n_transfed = transfer(n, k)
    # 정수형으로 변환
    numbers = list(map(process, n_transfed.split('0')))

    # 소수의 개수 세기
    for number in numbers:
        if is_prime(number):
            cnt += 1
    return cnt
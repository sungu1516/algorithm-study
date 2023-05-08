# 소수 판별 알고리즘
# O(N**(1/2)) 의 시간복잡도를 가진다.
def isPrime(num):
    if num < 2:
        return False

    i = 2
    while i*i <= num:
        if num % i == 0:
            return False

        i += 1

    return True

print(isPrime(int(input())))
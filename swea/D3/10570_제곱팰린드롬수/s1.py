import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 함수 정의
def is_palindrome(number):
    # number 의 제곱근이 양의 정수인지 아닌지를 판별


    origin = str(number)
    sqrt = str(number**(0.5))

    print(number, sqrt)
    if origin == origin[::-1] and sqrt == sqrt[::-1]:
        return True

T = int(input())
for tc in range(1, T + 1):
    A, B = map(int, input().split())
    total = 0
    for i in range(A, B+1):
        if is_palindrome(i):
            total += 1

    print('#{} {}'.format(tc, total))
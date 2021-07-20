# 함수 정의
def return_int():
    number = input()
    return int(number)

def examine_prime(number):
    if number == 2 or number == 3:
        print("소수입니다.")
    else:
        for i in range(2, (number // 2) + 1):
            if number % i == 0:
                print("소수가 아닙니다.")
                return

        print("소수입니다.")

number = return_int()
examine_prime(number)

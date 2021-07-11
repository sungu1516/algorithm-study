input_number = int(input())

# 특정 위치의 피보나치 수열값을 리턴하는 함수 정의
def get_fibo(n):
    if n <= 2:
        return 1
    return get_fibo(n-1) + get_fibo(n-2)

# 리스트로 출력
list = []
for i in range(0, input_number + 1):
    list.append(get_fibo(i))
print(str(list))


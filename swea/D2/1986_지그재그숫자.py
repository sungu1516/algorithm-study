# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.


# [예제 풀이]

# N이 5일 경우,

# 1 – 2 + 3 – 4 + 5 = 3

# N이 6일 경우,

# 1 – 2 + 3 – 4 + 5 – 6 = -3


# [제약사항]

# N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

## 풀이
# 테스트 케이스의 수를 입력받는다 
test_case = int(input())

# 반복문을 활용
for i in range(test_case):
    n = int(input())
    # 1 ~ 입력받은 숫자까지 담겨진 numbers라는 새로운 리스트 생성
    numbers = range(1, n+1)
    # 결과값을 저장할 result 변수 초기화
    result = 0

    # 반복문을 활용, 리스트 내의 숫자를 조건에 맞게 더하고 뺀다
    # enumberate 를 활용하여 각 숫자별 인덱스를 부여
    for idx, number in enumerate(numbers, start=1):
        if idx % 2:
            # idx가 홀수일 때
            result += number
        else:
            result -= number
    
    print(f'#{i+1} {result}')



# 10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.

# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)

## 풀이

cnt = int(input())

for i in range(1, cnt + 1):
    numbers = list(map(int, input().split()))
    total = sum(numbers)
    mean = round(total / len(numbers))

    print(f'#{i} {mean}')
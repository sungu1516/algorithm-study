# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

number = int(input())
total = 0

for n in range(1, number + 1):
    if n % 2 == 0:
        total += n

print(total)
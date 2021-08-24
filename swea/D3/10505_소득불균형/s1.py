import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    incomes = list(map(int, input().split())) # 소득

    # 소득의 평균 구하기
    total = 0
    for income in incomes:
        total += income
    mean = total / N

    # 평균치보다 소득이 적은 사람들의 수 구하기
    cnt = 0
    for income in incomes:
        if income <= mean:
            cnt += 1

    print('#{} {}'.format(tc, cnt))
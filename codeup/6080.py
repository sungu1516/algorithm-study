# 6080 : [기초-종합] 주사위 2개 던지기
dice1, dice2 = map(int, input().split())

for num1 in range(1, dice1 + 1):
    for num2 in range(1, dice2 + 1):
        print(num1, num2)
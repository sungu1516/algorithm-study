import sys
sys.stdin = open('input.txt')

# 화폐
money = [
    50000,
    10000,
    5000,
    1000,
    500,
    100,
    50,
    10
]

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    print('#{}'.format(tc))
    for m in money:
        cnt = N // m    # 교환횟수
        print('{}'.format(cnt), end = ' ')
        N %= m  # 거스름돈 저장 후 반복
    print()
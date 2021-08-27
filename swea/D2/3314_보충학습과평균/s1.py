import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())
for tc in range(1, T + 1):
    scores = list(map(int, input().split()))
    total = 0
    for score in scores:
        if score < 40:
            score += 40 - score
        total += score
    mean = total // 5
    print('#{} {}'.format(tc, mean))

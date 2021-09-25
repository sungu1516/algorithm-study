import sys
sys.stdin = open('input.txt', 'r')

# 재귀함수 정의
def min_cost(month, cost):
    global min_val
    if month > 12:
        if cost < min_val:
            min_val = cost
        return

    min_cost(month + 1, cost + plan[month] * d)
    min_cost(month + 1, cost + m1)
    min_cost(month + 3, cost + m3)

T = int(input())
for tc in range(1, T+1):
    d, m1, m3, y = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    min_val = y
    min_cost(1, 0)
    print('#{} {}'.format(tc, min_val))
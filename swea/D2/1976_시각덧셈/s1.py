import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())
    h_total, m_total = h1 + h2, m1 + m2

    if m_total >= 60: # 60분 이상일 떄
        m_total -= 60
        h_total += 1
    if h_total > 12: # 13시 이상일 때
        h_total -= 12

    print('#{} {} {}'.format(tc, h_total, m_total))
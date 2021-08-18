import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for _ in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())

    # A 사
    A = P * W

    # B 사
    if W <= R:
        B = Q
    else:
        B = Q + (W-R)*S

    result = A if A < B else B
    print('#{} {}'.format(_, result))
T = int(input())

for _ in range(1, T+1):
    a, b = map(int, input().split())
    quotient, remainder = divmod(a, b)

    print('#{} {} {}'.format(_, quotient, remainder))
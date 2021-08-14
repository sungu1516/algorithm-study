T = int(input())

for _ in range(1, T + 1):
    num1, num2 = map(int, input().split())
    result = '>' if num1 > num2 else '<' if num1 < num2 else '='

    print('#{} {}'.format(_, result))
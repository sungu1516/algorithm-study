T = int(input())

for _ in range(1, T + 1):
    tc= list(map(int, input().split()))
    odds = list(filter(lambda x: x % 2, tc))

    print('#{} {}'.format(_, odds))
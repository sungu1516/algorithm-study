import itertools
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = set()
    min_diff = 987654321

    for comb in itertools.combinations(range(N), N//2):
        ingred_a = comb
        ingred_b = []

        # B 식재료 추가
        for i in range(N):
            if i not in ingred_a:
                ingred_b.append(i)

        # 만약 확인했던 조합이라면 지나가기
        if ingred_a in used:
            continue

        used.add(ingred_a)
        used.add(tuple(ingred_b))

        # A 음식의 맛 구하기
        val_a = 0
        for ca in itertools.combinations(ingred_a, 2):
            val_a += arr[ca[0]][ca[1]] + arr[ca[1]][ca[0]]

        # B 음식의 맛 구하기
        val_b = 0
        for cb in itertools.combinations(ingred_b, 2):
            val_b += arr[cb[0]][cb[1]] + arr[cb[1]][cb[0]]

        # 맛 차이 최소값 갱신
        diff = abs(val_a - val_b)

        if diff < min_diff:
            min_diff = diff

    print('#{} {}'.format(tc, min_diff))
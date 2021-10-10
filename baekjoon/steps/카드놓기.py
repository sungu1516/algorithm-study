from itertools import combinations, permutations

n = int(input())    # 카드의 개수
k = int(input())    # 선택할 개수
cards = [input() for _ in range(n)]
unique = set()


for comb in combinations(cards, k):
    for perm in permutations(comb, len(comb)):
        unique.add(''.join(perm))

print(len(unique))
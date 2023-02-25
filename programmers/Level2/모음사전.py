from itertools import combinations, permutations, product


def solution(word):
    vows = ['A', 'E', 'I', 'O', 'U']
    result = []

    for i in range(1, 6):
        for p in product(vows, repeat=i):
            result.append(''.join(p))

    result.sort()

    return result.index(word) + 1
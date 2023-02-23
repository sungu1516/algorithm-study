from itertools import combinations
# input
l, c = map(int, input().split())
arr = input().split()
arr.sort()

vowel = ('a', 'e', 'i', 'o', 'u')

for pwd in combinations(arr, l):
    # 모음의 개수
    cnt = 0
    for i in pwd:
        if i in vowel:
            cnt += 1

    # 모음, 자음의 개수가 조건에 맞는 경우만 출력
    if cnt >= 1 and l - cnt >= 2:
        res = ''.join(pwd)
        print(res)